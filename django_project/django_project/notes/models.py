from django.db import models


class User(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)


class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
