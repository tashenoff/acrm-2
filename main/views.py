from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'main/index.html')
