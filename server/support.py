import json
from flask import Response

# Error handling


def resource_not_found():
    error_message = {"Message": "Resource not found."}
    msg_json = json.dumps(error_message)
    return Response(msg_json, mimetype='application/json', status=404)


def bad_request(details="No details"):
    error_message = {"Message": "Bad request.", "Details": details}
    msg_json = json.dumps(error_message)
    return Response(msg_json, mimetype='application/json', status=400)


def server_error(details="No details"):
    error_message = {"Message": "Server error.", "Details": details}
    msg_json = json.dumps(error_message)
    return Response(msg_json, mimetype='application/json', status=500)

# Resource getters and setters


def get_resource_response(resource):
    # print(resource)
    if resource:
        return Response(json.dumps(resource), mimetype='application/json')
    return resource_not_found()


def delete_resource_response(response, resourceType):
    if response:
        msg_json = json.dumps({"Message": resourceType + " successfully deleted.", "Data": response})
        return Response(msg_json, mimetype='application/json', status=200)
    else:
        return resource_not_found()


def set_resource_response(response, resourceType, create=True):
    if create:
        status_code = 201
        action = "created"
    else:
        status_code = 200
        action = "updated"
    if response:
        msg_json = json.dumps({"Message": resourceType + " successfully " + action + "."})
        resp = Response(msg_json, mimetype='application/json', status=status_code)
    else:
        msg_json = json.dumps({"Message": resourceType + " not " + action + "."})
        resp = Response(msg_json, mimetype='application/json', status=500)
    return resp


def convert_resource_from_json(resource):
    '''
    Converts resource from JSON into a usable python object.
    If resource is already converted, it will simply return the resource
    @params resource: resource to be converted
    @returns: converted JSON resource in usable form.
    '''
    if type(resource) is str:
        resource = json.loads(resource)
    return resource