from django.contrib import admin
from .models import Student, Course, StudentCourse, Mentor

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(Mentor)



