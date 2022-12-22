from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project


def index(request):
    latest_project_list = Project.objects.order_by('-pub_date')[:5]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'projects/index.html', context)


def search(request):
    latest_project_list = Project.objects.order_by('-pub_date')[:9]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'projects/search.html', context)
    

def project(request, project_id):
    return render(request, 'projects/project_view.html')
