from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def berita(request):
    template =loader.get_template('latihan1.html')
    return HttpResponse(template.render())
def about(request):
    template =loader.get_template('about.html')
    return HttpResponse(template.render())



