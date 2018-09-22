from django.shortcuts import render
from django.http import HttpResponse
from .models import Mytable
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json

def index(request):
    if request.method == "GET":
        try :
            tmp = str(request.get_full_path())
            tmp = tmp[1:-1]
            stat = "OFF"
            time = str(datetime.today().strftime("%Y/%m/%d %H:%M:%S  "))

            if int(tmp) > 25:
                stat = "ON"
            else:
                stat = "OFF"
            in_data = Mytable(tmp = tmp, stat = stat)
            in_data.save()
        except :
            in_data = None
    
    return HttpResponse(in_data)

def present(request):
    rows = Mytable.objects.order_by('id').last()
    time = str(rows.time.strftime("%Y/%m/%d %H:%M:%S "))
    return HttpResponse(time + str(rows.tmp) +" " + str(rows.stat))

