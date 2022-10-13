from django.urls import path
from .views import blogwrite
from .views import readblog
from .views import createblog
from .views import ediptblog
from .views import deleteblog
from .views import home
urlpatterns = [
    path('',blogwrite.as_view(),name='blog'),
    path('<int:pk>/',readblog.as_view(),name='read'),
    path('create/',createblog.as_view(),name='create'),
    path('<int:pk>/edit',ediptblog.as_view(),name='edit'),
    path('<int:pk>/delete',deleteblog.as_view(),name='delete'),
    path('home/', home , name='home'),
    

]