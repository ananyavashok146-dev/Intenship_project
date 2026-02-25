from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('company', 'Company'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    education = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.user.username


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.company_name


class Internship(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    description = models.TextField()
    required_skills = models.CharField(max_length=200)
    deadline = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='pending')
    applied_on = models.DateTimeField(auto_now_add=True)