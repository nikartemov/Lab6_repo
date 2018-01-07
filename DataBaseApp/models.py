from django.db import models


class User(models.Model):
    def __str__(self):
        return self.first_name
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()


class Team(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    description = models.TextField()
