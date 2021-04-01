from django.db import models
from datetime import datetime

class Person(models.Model):
    username = models.IntegerField(default=0)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_encoded = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name

class Savings(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    date_created = models.DateTimeField(auto_now_add=False, auto_now=True)
    amount = models.IntegerField(default=200)

    def __str__(self):
        return str(self.person)+ ' ' + str(self.amount) + ' ' + str(self.date)