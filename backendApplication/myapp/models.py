from django.conf import settings
from django.db import models
from django.utils import timezone


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
#
#
# class Customer(models.Model):
#     name = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#
# class OrderDetails(models.Model):
#     customer = models.OneToOneField(Customer, unique=True, on_delete=models.CASCADE)
#     total = models.FloatField(blank=True, null=True)
#
# class Products(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.FloatField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class OrderItems(models.Model):
#     order_details = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     product = models.OneToOneField(Products, unique=True, on_delete=models.CASCADE, default=None)
#     quantity = models.IntegerField()

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    year_experience = models.IntegerField()
    salary = models.FloatField()


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    mentor = models.OneToOneField(Mentor, on_delete=models.SET_NULL, default=None, null=True, blank=True)



class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)


