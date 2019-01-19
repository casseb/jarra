from flask import make_response
import talk

def rest(message):
    return make_response("{message} listened correctly".format(message=message), 201)

def getContent(message):
    talk.audit("Ouvi que você falou " + message.get("content"))
    return message.get("content")
