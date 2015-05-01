from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Список школ")

def classes(request, school_id):
    return HttpResponse("Список классов у школы %s" % school_id)

def school(request, school_id):
    return HttpResponse("Школа %s" % school_id)

