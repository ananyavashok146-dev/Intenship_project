from django.shortcuts import render
from .models import Internship

def internship_list(request):
    internships = Internship.objects.all()
    return render(request, 'internships.html', {'internships': internships})