from rest_framework.response import Response
from rest_framework.decorators import api_view
from .dispatcher import process_data
from django.shortcuts import render


@api_view(['GET', 'POST'])
def anonymize(request):
    match request.method:
        case "GET":
            return Response({"Message": "Welcome to anonymizer!"})
        case "POST":
            return Response(process_data(request))


def doc(request):
    return render(
        request,
        'index.html'
    )
