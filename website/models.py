from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records')
    created_at = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length= 15)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
