from celery import shared_task
from .dispatcher import process_data
import json
import time

@shared_task
def assync_process_data(request):
    request = json.loads(request)
    return process_data(request)