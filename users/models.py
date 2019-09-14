from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # firstname = models.CharField(max_length=50)
    # surname = models.CharField(max_length=50)
    # email = models.EmailField()

  def __str__(self):
    return self.email