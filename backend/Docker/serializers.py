from rest_framework import serializers
from .models import Project, Docker, Dockerfile
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project

