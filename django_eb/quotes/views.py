from django.shortcuts import render
from django.http import HttpResponse
from.models import Data
import random

def index(request):
    message = "This page shows quotes randomly."
    q = Data.objects.filter(pk=random.randint(1, 10))
    return HttpResponse("{0} '\n '\n {1}".format(message, q[0]))

def detail(request, quote_id):
    c = Data.objects.filter(pk=quote_id)
    return HttpResponse("{0}".format(c[0]))
