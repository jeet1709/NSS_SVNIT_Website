from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('team',views.team,name='team'),
    path('gallery',views.gallery,name='gallery'),
]
