from django.shortcuts import render

# Create your views here.
#request -> response
# request handler
# action

from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x=1
    y=1
    return x

def say_hello(request):
    x=calculate()
    #pull data from db
    # transform
    #send email
    return render(request,'hello.html', {'name': 'Faisal'})