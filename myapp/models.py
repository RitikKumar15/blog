from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
  author = models.CharField(max_length=50)
  title = models.CharField(max_length=100)
  desc = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)