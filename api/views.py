from rest_framework.response import Response
from rest_framework.decorators import api_view
from anonymizer import masking

@api_view(['POST'])
def postData(request):
    payload = request.data
    database = payload['database']
    fields = payload['fields']
    payload['database'] = masking.mask_data(database, fields, method="cpf", masked=True, length=5, mask_result_lenght=True)
    payload['message'] = "success"
    return Response(payload)