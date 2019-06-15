from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.apps import apps

# Create your models here.


def generate_referral_code():
    Customer = apps.get_model('users.Customer')
    while True:
        referral_code = uuid.uuid4().hex[:7].upper()
        if not Customer.objects.filter(referral_code=referral_code).exists():
            break
    return referral_code


class User(AbstractUser):
    def __str__(self):
        return self.email


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Customer(models.Model):
    tab = models.ForeignKey('restaurants.Tab', on_delete=models.CASCADE, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    referral_code = models.CharField(default=generate_referral_code, unique=True, editable=False, max_length=7)



