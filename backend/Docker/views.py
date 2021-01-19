# Django
from django.http import HttpResponse
from django.views import View
from .models import Docker


def create_project(request):
    """
    Create A Project
    :param request:
    :return:
    """
    return HttpResponse('fuck')


def create_docker_compose_yml(request):
    """
    Make docker-compose.yml

    :param request:
    :return:
    """

