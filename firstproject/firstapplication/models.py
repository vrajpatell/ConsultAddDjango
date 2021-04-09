from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=150)
