from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.add_comment, name='add_comment'),
    path('show_comments', views.show_comments, name='show_comments')
]