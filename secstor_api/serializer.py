import json

def serialize_request(request):
    serialized = {
        'data': request.data
    }
    return json.dumps(serialized)
