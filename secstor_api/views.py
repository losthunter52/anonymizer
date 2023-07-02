from rest_framework.response import Response
from rest_framework.decorators import api_view
from .dispatcher import process_data
from django.shortcuts import render
from .doc import doc as d
from .serializer import serialize_request
from .tasks import assync_process_data
from celery.result import AsyncResult
from .dispatcher import process_data
from .validators.validate import validade_result_request
import json

@api_view(['GET', 'POST'])
def anonymize(request):
    if request.method == "POST":
        request = serialize_request(request)
        result = assync_process_data.delay(request)
        return Response({"task_id": result.id})
    return Response({"Message": "Welcome to anonymizer!"})
            
@api_view(['GET', 'POST'])
def result(request):
    if request.method == "POST":
        valid = validade_result_request(request)
        if valid == True:
            task_id = request.data['task_id']
            result = AsyncResult(task_id)
            return Response({"Status": result.status, "Result": result.result})
        return Response(valid)
    return Response({"Message": "Welcome to anonymizer!"})

def doc(request):
    context = {
        'doc': d,
    }
    return render(
        request,
        'index.html',
        context
    )
