from django.shortcuts import render
from django.http import HttpResponse
from .models import Mytable
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

def index(request):
    if request.method == "GET":
        try:
            t = str(request.get_full_path())
            tmp = t[1:]
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
            in_data = None
        return HttpResponse(in_data)


def present(request):
    row = Mytable.objects.order_by('id').last()
    context = {'row': row}
    time = str(datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
    tmp = str(row.tmp)
    strength = row.strength
    stat = str(row.stat)
    return render(request, 'project/present.html', context)
#    return HttpResponse(time +" "+tmp+" "+strength+" "+stat)
