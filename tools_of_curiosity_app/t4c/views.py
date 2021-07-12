from django.shortcuts import render

from django.http import HttpResponse

from pprint import pprint

def index(request):
    print("t4c/views.py @ index()")
    pprint(request)
    context = {}
    return render(request, "t4c/index.html", context)

def aframedemo(request):
    print("t4c/views.py @ aframedemo()")
    pprint(request)
    context = {}
    return render(request, "t4c/aframedemo.html", context)

def minigame1(request):
    print("t4c/views.py @ minigame1()")
    pprint(request)
    context = {}
    return render(request, "t4c/minigame1.html", context)

def minigame2(request):
    print("t4c/views.py @ minigame2()")
    pprint(request)
    context = {}
    return render(request, "t4c/minigame2.html", context)

def minigame3(request):
    print("t4c/views.py @ minigame3()")
    pprint(request)
    context = {}
    return render(request, "t4c/minigame3.html", context)

def minigame4(request):
    print("t4c/views.py @ minigame4()")
    pprint(request)
    context = {}
    return render(request, "t4c/minigame4.html", context)
    
def designsprint(request):
    print("t4c/views.py @ designsprint()")
    pprint(request)
    context = {}
    return render(request, "t4c/designsprint.html", context)
    
def designsprint2(request):
    print("t4c/views.py @ designsprint2()")
    pprint(request)
    context = {}
    return render(request, "t4c/designsprint2.html", context)

def OBSOLETEindex(request):
    return HttpResponse("Hello, world. You're at the t4c index.")

def Starter(request):
    print("t4c/views.py @ Starter()")
    pprint(request)
    context = {}
    return render(request, "t4c/Starter.html", context)