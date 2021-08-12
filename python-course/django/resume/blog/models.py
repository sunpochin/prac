from django.db import models
from django.urls import reverse

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_number', kwargs={
            'blog_no': self.id
        })
