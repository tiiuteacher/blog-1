
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]

