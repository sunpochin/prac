from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name="my_posts"),
    path('<int:blog_no>', views.blog_detail, name="blog_number")
]
