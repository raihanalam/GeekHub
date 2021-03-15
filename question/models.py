from django.db import models

# Create your models here.
class Question(models.Model):

    id = models.AutoField(primary_key=True)
    by = models.CharField(max_length=100,blank=False)
    problem = models.CharField(max_length=300,blank=False)
    description = models.TextField(max_length=1000,blank=True)
    tag = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.problem
