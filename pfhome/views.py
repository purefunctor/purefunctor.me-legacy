from django.shortcuts import render


def soon(request):
    return render(request, "pfhome/soon.html")
