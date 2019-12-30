from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.apps import apps
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from restaurants.models import Restaurant

# Create your models here.


def generate_referral_code():
    Customer = apps.get_model('users.Customer')
    while True:
        referral_code = uuid.uuid4().hex[:7].upper()
        if not Customer.objects.filter(referral_code=referral_code).exists():
            break
    return referral_code


class User(AbstractUser):
    # @TODO: expire auth tokens
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __str__(self):
        return self.email


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Customer(models.Model):
    tab = models.ForeignKey('restaurants.Tab', on_delete=models.CASCADE, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    stripe_user_id = models.CharField(max_length=255, blank=True)
    stripe_access_token = models.CharField(max_length=255, blank=True)
    referral_code = models.CharField(default=generate_referral_code, unique=True, editable=False, max_length=7)



