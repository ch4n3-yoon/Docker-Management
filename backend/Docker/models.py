from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)


class Docker(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128)
    image = models.CharField(max_length=64, null=True, blank=True)
    environment = models.TextField(default=None, null=True, blank=True)
    ports = models.TextField(default=None, null=True, blank=True)


class Dockerfile(models.Model):
    docker = models.OneToOneField(
        Docker,
        on_delete=models.CASCADE,
    )
    dockerfile = models.TextField(default=None, blank=True)
