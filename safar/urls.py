from django.urls import path
from . import views

urlpatterns = [
    path('newSafar/', views.newSafar, name='newSafar'),
    path('addDetail/', views.addDetail, name='addDetail'),
]