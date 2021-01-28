# Django
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Project, Docker, Dockerfile
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from Lib import api

# import yaml
import oyaml as yaml
import json
import pprint


def create_project(request):
    """
    Create A Project
    :param request:
    :return:
    """
    return HttpResponse('fuck')


def create_docker_compose_yml(request, project_id=1):
    """
    Create docker-compose.yml
    """
    project = Project.objects.get(id=project_id)
    if not project:
        # No such project
        return api.fail('No such project')

    # Do not combine the two lines of code below
    docker_compose = {'version': '3'}
    docker_compose['services'] = {}

    dockers = Docker.objects.filter(project=project)
    for docker in dockers:
        dockerfile = Dockerfile.objects.get(docker=docker)
        file = open('/tmp/')

        local_docker_compose = {}
        local_docker_compose['image'] = docker.image

        # Parse environment stored in JSON
        environments = json.loads(docker.environment)
        local_docker_compose['environment'] = \
            [f"{key}={value}" for key, value in environments.items()]

        # Parse ports stored in JSON
        """
        # ports will be ...
        [
            {outer: 80, inner: 8080},
            {outer: 3306, inner: 1234},
        ]
        """
        ports = json.loads(docker.ports)
        local_docker_compose['ports'] = [f"{port.get('outer')}:{port.get('inner')}" for port in ports]

        docker_compose['services'][docker.name] = local_docker_compose

    pprint.pprint(docker_compose)
    docker_compose_yml = yaml.dump(docker_compose)

    # TODO: store docker-compose.yml as real file

    return HttpResponse(docker_compose_yml)


