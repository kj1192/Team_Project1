from django.shortcuts import render
from django.http import HttpResponse
from .models import Mytable
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json


def index(request):
    if request.method == "GET"
    try :
        tmp = str(request.read())
        time = datetime.now()
        stat = 0
        if int(tmp) > 25:
            stat = 1
        else:
            stat = 0
        in_data = Mytable(time = time, tmp = tmp, stat = stat)
        in_data.save()
    except :
        in_data = None
    return HttpResponse(in_data)
