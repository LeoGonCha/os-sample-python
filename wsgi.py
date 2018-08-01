from flask import Flask
from flask import request

import logging
import subprocess
from subprocess import call

logging.basicConfig(filename='program.log',level=logging.DEBUG)

application = Flask(__name__)

@application.route("/")
def hello():
    logging.info("Hello World!") 
    return "Hello World!"

@application.route('/', methods = ['POST'])
def JsonHandler():
    if request.is_json:
        content = request.get_json()
        logging.info(content['event_name'])
        # Handle project changes
        if content['event_name'] == "project_create":
            logging.info('Project created. ' + content['name'])
            your_call = call("./sleep.sh", shell=True)
            return "OK"
        elif content['event_name'] == "push":
            logging.info('Project push. ' + content['name'])
            return "OK"
        elif content['event_name'] == "project_destroy":
            logging.info('Project destoried. ' + content['name'])
            return "OK"
        elif content['event_name'] == "project_rename":
            logging.info('Project renamed de ' + content['old_path_with_namespace'] + ' para ' + content['name'])
            return "OK"
        elif content['event_name'] == "project_transfer":
            logging.info('Project {0} transferd')
            return "OK"
        else:
            logging.info(content)
            return "Ok"
    else:
        logging.inf("else")
        return "JSON Only"

if __name__ == "__main__":
    application.run()
