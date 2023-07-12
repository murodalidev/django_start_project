from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('Django start project!')
