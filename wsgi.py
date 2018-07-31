from flask import Flask
from flask import request

import logging

logging.basicConfig(filename='program.log',level=logging.DEBUG)

application = Flask(__name__)

@application.route("/")
def hello():
    logging.info("Hello World!") 
    return "Hello World!"

@application.route('/', methods = ['POST'])
def JsonHandler():
    if request.is_json:
        logging.info("if")
        content = request.get_json()
        logging.info(content)
        # Handle project changes
        if content['event_name'] == "project_create":
            #pipe = store.pipeline()
            #pipe.hmset(content['name'], {"group": content['owner_name']})
            #pipe.hmset(content['name'], {"branches": map_branches })
            #pipe.execute()
            logging.info('Project {0} Created.' content['name'])
            return "OK"
        elif content['event_name'] == "push":
            #update_consul_last_push(content)
            logging.info('Project {0} push.')
            return "OK"
        elif content['event_name'] == "project_destroy":
            #store.delete(content['name'])
            logging.info('Project {0} destoried.' content['name'])
            return "OK"
        elif content['event_name'] == "project_rename":
            #store.rename(content['old_path_with_namespace'].split('/')[1], content['name'])
            logging.info('Project renamed from {0} to {1}' content['old_path_with_namespace'].split('/')[1], content['name'])
            return "OK"
        elif content['event_name'] == "project_transfer":
            #store.hmset(content['name'], {"group": content['path_with_namespace'].split('/')[0]})
            logging.info('Project {0} transferd' content['name'])
            return "OK"
    else:
        logging.inf("else")
        return "JSON Only"
     
if __name__ == "__main__":
    application.run()
