#Supervisor Conf Directory

All the process of Text Analytics are maintained using supervisor utility of linux. The required supervisor configuration files of each subprojects are available here.

Please copy all conf files of this folder to supervisor's conf folder.(i.e. /etc/supervisor/conf.d)

##For Ubuntu:

__Use following commands:__

    $sudo apt-get install supervisor
    $sudo cp *.conf /etc/supervisor/conf.d/
    $sudo service supervisor restart
    
__Open your web-browser and go to following link:__<br>
The port number can be configured in __supervisor_web.conf__

    http://localhost:9005/
    
