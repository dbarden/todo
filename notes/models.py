from django.db import models


class List(models.Model):
    name = models.CharField(max_length=128)


class Note(models.Model):
    name = models.CharField(max_length=128)
    test = models.TextField()
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True)
    list = models.ForeignKey('List', related_name='notes')
