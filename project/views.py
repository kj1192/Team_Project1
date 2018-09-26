from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from .models import Mytable
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlparse

def index(request):
    if request.method == "GET":
        try:
            row = Mytable.objects.order_by('id').last()
            context = {'row': row}
            tmp = str(row.tmp)
            strength = row.strength
            stat = str(row.stat)

        except:
            return HttpResponse("Get Error")
        return render(request, 'project/present.html', context)

@csrf_exempt
def present(request):
    if request.method == 'PUT':
        try:
            data = (request.body.decode('utf-8'))
            tmp = data[4:]
            stat = "activated"
            time = str(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
            if int(tmp) > 28 and int(tmp) < 31:
                stat = "activated"
                strength = "(Weak wind mode)"
            elif int(tmp) >= 31: 
                stat = "activated"
                strength = "(Strong wind mode)"
            else:
                stat = "deactivated"
                strength = ""
            in_data = Mytable(tmp = tmp, stat = stat, strength = strength)
            in_data.save()
        except:
            print("Put Error")
        return HttpResponse(data)

