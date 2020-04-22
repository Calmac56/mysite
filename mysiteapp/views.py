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

def getprojects(request):
    projnames = request.GET.getlist('name[]', None)
    projcreations = request.GET.getlist('creation[]', None)
    projmodified = request.GET.getlist('modified[]', None)
    projlanguages = request.GET.getlist('language[]', None)
    projurls = request.GET.getlist('url[]', None)
    print(request.GET)
    if len(projnames) > 0:
        for x in range(len(projnames)):
            project = Projects()
            project.name = projnames[x]
            
            project.datecreated = projcreations[x][:10]
            project.lastmodified = projmodified[x][:10]
            project.url = projurls[x]
            if Projects.objects.filter(name=project.name).exists() == False:
                project.save()
    return render(request, 'mysiteapp/projects.html')

    