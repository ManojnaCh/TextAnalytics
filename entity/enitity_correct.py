__author__ = 'root'
import nltk
from flask import Flask, request, jsonify

app = Flask(__name__)
def named_entity(text):
    def extract_entity_names(chunk):
        if hasattr(chunk, 'label') and chunk.label:
            if chunk.label() == 'NE':
                entity_names.append(' '.join([child[0] for child in chunk]))
            else:
                for child in chunk:
                    entity_names.extend(extract_entity_names(child))
        return entity_names
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.chunk.ne_chunk_sents(tagged_sentences,binary=True)
    entity_names = []
    for tree in chunked_sentences:
        entity_names.extend(extract_entity_names(tree))
    response = set(entity_names)
    return jsonify(output=str(response))

@app.route('/')
def Sentiment():
    return 'Welcome to Entity Extraction'

@app.route('/entity/<message>', methods=['GET'])
def entities(message):
    output = named_entity(message)
    return output

@app.route('/entity', methods=['POST'])
def entities_post():
    message=request.form('text')
    output_post = named_entity(message)
    return output_post

if __name__ == '__main__':
    app.run(debug=True,port=2080)


