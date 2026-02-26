from django.urls import path
from . import views

urlpatterns = [
    path('', views.internship_list, name='internship_list'),
    path('internship/<int:pk>/', views.internship_detail, name='internship_detail'),
    path('internship/<int:pk>/apply/', views.apply_internship, name='apply_internship'),
]