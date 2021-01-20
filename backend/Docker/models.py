from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)


class Docker(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128)
    image = models.CharField(max_length=64, null=True, blank=True)
    environment = models.TextField(default=None, null=True, blank=True)
    ports = models.TextField(default=None, null=True, blank=True)   # store data as json

