from django.db import models
from django.forms import Textarea


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    block = models.CharField(max_length=1)
    number = models.CharField(max_length=3)
    u_type = models.CharField(max_length=10)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.block} {self.number}"


class Maintenance(models.Model):
    id = models.IntegerField(primary_key=True)
    block = models.CharField(max_length=10)
    installment = models.CharField(max_length=2)
    penalty = models.CharField(max_length=5)
    dop = models.DateField(auto_now=False, auto_now_add=False)
    p_status = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.block} {self.dop}"


class Notice(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} : {self.title}"


class Gallery(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return f"Id : {self.id}"
