from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.getStudents, name="students"),
    path("mentors/", views.getMentors, name="mentors"),
    path("courses/", views.getCourses, name="courses"),
    path("student_course/", views.getStudentCourse, name="student_course"),
]

