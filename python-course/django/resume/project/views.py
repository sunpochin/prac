from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.


def index(request):
    myprojects = Project.objects.all()
    context = {
        'projects': myprojects
    }
    return render(request, 'project/index.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'item': project
    }
    return render(request, 'project/detail.html', context)
