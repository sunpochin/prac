from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import ProjectFilter
# Create your views here.
# https://stackoverflow.com/questions/41218117/django-css-file-wont-update#


def many_projects_func(request):
    items = Project.objects.all()
    filtered = ProjectFilter(request.GET, queryset=items)
    items = filtered.qs

    context = {
        'projects': items,
        'filtered': filtered,
    }
    return render(request, 'the_projects.html', context)


def project_detail_func(request, project_id):
    item = get_object_or_404(Project, id=project_id)
    context = {
        'project': item
    }
    return render(request, 'project_detail.html', context)
