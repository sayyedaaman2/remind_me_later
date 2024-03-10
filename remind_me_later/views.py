from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return render(request,"index.html")


def authPage(request):
    return render(request, 'auth.html')


def remiderList(request):
    return render(request,"remiderlist.html")
