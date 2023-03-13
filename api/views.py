from rest_framework.response import Response
from rest_framework.decorators import api_view
from .validators import validate_request
from .dispatcher import dispatch


@api_view(['GET', 'POST'])
def anonymize(request):
    response = {}
    match request.method:
        case "GET":
            response = {"Message": "Welcome to anonymizer!"}
        case "POST":
            request_validity = validate_request(request)
            if request_validity == True:
                response = dispatch(request)
            elif request_validity == False:
                response = {
                    "Request Error": "The request media type is not 'application/json'"
                }
            else:
                response = request_validity
    return Response(response)


@api_view(['GET'])
def help(request):
    return Response({"Help": "Anonymizer help tips"})
