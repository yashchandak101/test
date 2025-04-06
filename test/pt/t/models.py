
from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)

class SignalCreatedModel(models.Model):
    message = models.CharField(max_length=100)
