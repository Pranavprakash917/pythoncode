from django.db import models


class courses(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    course = models.CharField(max_length=100)

class fees(models.Model):
    student_name = models.CharField(max_length=50)
    amount = models.IntegerField()