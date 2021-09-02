from django.db import models

# Create your models here.


class StudentsList(models.Model):
    studentId = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30, null=True)
    markOne = models.IntegerField()
    markTwo = models.IntegerField()
    markThree = models.IntegerField()
    markFour = models.IntegerField()
    markFive = models.IntegerField()
