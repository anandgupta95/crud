from django.db import models

# Create your models here.

class Student(models.Model):
  roll_no = models.CharField(max_length=255,primary_key=True)
  name = models.CharField(max_length=255)
  branch=models.CharField(max_length=255)
  email=models.CharField(max_length=255)

