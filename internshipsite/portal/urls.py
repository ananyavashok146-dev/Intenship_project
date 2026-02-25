from django.urls import path
from . import views

urlpatterns = [
    path('', views.internship_list, name='internship_list'),
]