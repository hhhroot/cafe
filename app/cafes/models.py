from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = settings.AUTH_USER_MODEL


class AddressLevelOne(models.Model):
    name = models.CharField(max_length=20)


class AddressLevelTwo(models.Model):
    name = models.CharField(max_length=20)
    super_name = models.ForeignKey(AddressLevelOne, on_delete=models.CASCADE)


class AddressLevelThree(models.Model):
    name = models.CharField(max_length=20)
    super_name = models.ForeignKey(AddressLevelTwo, on_delete=models.CASCADE)


class Cafe(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey(AddressLevelThree, on_delete=models.CASCADE)

    detail_address = models.CharField(max_length=50)
    detail_address_load = models.CharField(max_length=50)
    number = PhoneNumberField()


class CafePost(models.Model):
    cafe = models.OneToOneField(Cafe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
