from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from mysiteapp.models import Language, Projects

# Create your views here.

def index(request):
    return render(request, 'mysiteapp/index.html')

def project(request):
    context_dict = {}
    context_dict['project'] = Projects.objects.all()
    return render(request, 'mysiteapp/projects.html', context=context_dict)

def portfolio(request):
    return render(request, 'mysiteapp/portfolio.html')

def error404(request,exception):
    return render(request, 'mysiteapp/404.html')

def error500(request):
    return render(request, 'mysiteapp/404.html')

def updateviews(request,projid):

    currentviews = Projects.objects.get(projid=projid).views
    newviews = currentviews + 1
    Projects.objects.filter(projid=projid).update(views=newviews)
    url = currentviews = Projects.objects.get(projid=projid).url
    return redirect(url)
