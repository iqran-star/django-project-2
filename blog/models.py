from django.db import models

# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    text=models.TextField()
    date=models.DateTimeField(auto_now=True)
    