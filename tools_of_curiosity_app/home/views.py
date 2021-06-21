from django.shortcuts import render

from django.http import HttpResponse


def index(request):
   context = {}
   return render(request, "home/index.html", context)

def OBSOLETEindex(request):
    return HttpResponse("Hello, world. You're at the /home index.")

