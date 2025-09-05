from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CustomerProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username