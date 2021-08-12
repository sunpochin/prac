import django_filters
#from django import forms
from .models import Project


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['type']
