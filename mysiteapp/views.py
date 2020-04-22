from django.shortcuts import render
from django.shortcuts import HttpResponse
from mysiteapp.models import Language, Projects

# Create your views here.

def index(request):
    return render(request, 'mysiteapp/index.html')

def project(request):
    context_dict = {}
    context_dict['project'] = Projects.objects.all()
    return render(request, 'mysiteapp/projects.html', context=context_dict)
