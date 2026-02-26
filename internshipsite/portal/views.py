from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Internship, Application, StudentProfile


def internship_list(request):
    internships = Internship.objects.all()
    return render(request, 'portal/internships.html', {'internships': internships})


def internship_detail(request, pk):
    internship = get_object_or_404(Internship, pk=pk)
    return render(request, 'portal/internship_detail.html', {'internship': internship})


@login_required
def apply_internship(request, pk):
    internship = get_object_or_404(Internship, pk=pk)
    try:
        student_profile = request.user.studentprofile
    except StudentProfile.DoesNotExist:
        return redirect('internship_list')

    existing = Application.objects.filter(student=student_profile, internship=internship).first()
    if existing:
        return render(request, 'portal/application_result.html', {'message': 'You have already applied for this internship.'})

    Application.objects.create(student=student_profile, internship=internship, status='pending')
    return render(request, 'portal/application_result.html', {'message': 'Application submitted successfully.'})