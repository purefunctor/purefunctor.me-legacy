from django.shortcuts import render


def soon(request):
    return render(request, "pfhome/soon.html")


def home(request):
    return render(request, "pfhome/home.html")
