from django.contrib import admin
from django.urls import path
from . import views
import funccrud.urls
import funccrud.views


urlpatterns = [

    path('', views.read, name="home"),
    path('newblog/', views.create, name="newblog"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('add_comment/<int:pk>', views.add_comment, name='add_comment'),
    

]