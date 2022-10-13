from ast import List
from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from urllib import request, response
from django.shortcuts import render
from .models import blog
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
class blogwrite(ListView):
    model= blog
    template_name = 'blog.html'
    context_object_name = 'all'
class readblog(DetailView):
    model= blog
    template_name = 'read.html'
class createblog(CreateView):
    model = blog
    template_name= 'create.html'
    fields = '__all__'
class ediptblog(UpdateView):
    model = blog 
    template_name = 'blog_edit.html'
    fields= ['title','writing']
class deleteblog(DeleteView):
    model = blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog')
def home(request):
    return render(request,'home.html')
    

