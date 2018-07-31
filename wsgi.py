from flask import Flask
from flask import request
 
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/', methods = ['POST'])
def JsonHandler():
    if request.is_json:
        logger.info("if")
        content = request.get_json()
        logger.info(content)
        # Handle project changes
        if content['event_name'] == "project_create":
            #pipe = store.pipeline()
            #pipe.hmset(content['name'], {"group": content['owner_name']})
            #pipe.hmset(content['name'], {"branches": map_branches })
            #pipe.execute()
            logger.info('Project {0} Created.'.format(content['name']))
            return "OK"
        elif content['event_name'] == "push":
            #update_consul_last_push(content)
            logger.info('Project {0} push.')
            return "OK"
        elif content['event_name'] == "project_destroy":
            #store.delete(content['name'])
            logger.info('Project {0} destoried.'.format(content['name']))
            return "OK"
        elif content['event_name'] == "project_rename":
            #store.rename(content['old_path_with_namespace'].split('/')[1], content['name'])
            logger.info('Project renamed from {0} to {1}'.format(content['old_path_with_namespace'].split('/')[1], content['name']))
            return "OK"
        elif content['event_name'] == "project_transfer":
            #store.hmset(content['name'], {"group": content['path_with_namespace'].split('/')[0]})
            logger.info('Project {0} transferd'.format(content['name']))
            return "OK"
    else:
        return "JSON Only"
     
if __name__ == "__main__":
    application.run()
