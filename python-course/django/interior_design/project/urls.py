from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.many_projects_func, name='many_projects'),
    path('<int:project_id>', views.project_detail_func, name='project_detail'),
]
