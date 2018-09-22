from django.shortcuts import render
from django.http import HttpResponse
from .models import Mytable
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    

    try :
        context = {'time' : time, 'temperature' : temp, 'status' : stat}
        context.save()
    except :
        context = None
    return render(request, "project/", context)
