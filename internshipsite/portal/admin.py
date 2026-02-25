from django.contrib import admin
from .models import User, StudentProfile, CompanyProfile, Internship, Application

admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(CompanyProfile)
admin.site.register(Internship)
admin.site.register(Application)