from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)
@app.route('/')
def Sentiment():
    return 'Welcome to Sentiment Analytics'

@app.route('/sentiments/<message>',methods=['GET'])
def sentiment_get(message):
    if request.method == 'GET':
        text = TextBlob(message)
        response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity}
    return jsonify(response)

@app.route('/sentiments',methods=['POST'])
def sentiment_post():
    if request.method == 'POST':
        text = request.form['text']
        result = TextBlob(text)
        response = {'polarity' : result.polarity , 'subjectivity' : result.subjectivity}
    return jsonify(response)

if __name__ == '__main__':
   app.run(port=1501)

