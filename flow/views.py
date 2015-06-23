from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This right here is the index.")

def detail(request, type, id):
    return HttpResponse("You're looking at %s %s." % (type, id))
