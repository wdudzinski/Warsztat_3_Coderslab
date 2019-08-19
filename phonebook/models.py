from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    description = models.TextField


class Phone(models.Model):
    number = models.IntegerField
    type = models.CharField(max_length=64)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    n_house = models.IntegerField
    n_flat = models.IntegerField


class Email(models.Model):
    email = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
# Create your models here.
#miasto, ulicę, numer domu, numer mieszkania