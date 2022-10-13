from audioop import reverse
from turtle import mode
from django.db import models
from django.urls import reverse
class blog(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    title = models.CharField(max_length=20)
    writing = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog')

    
    
