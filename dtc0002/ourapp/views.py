from os import getenv
from django.shortcuts import render

def say_hello(request):
    return render(request, "ourapp/hello.html", { "whos_talking": getenv("WHO_IS_TALKING", "Django") })
