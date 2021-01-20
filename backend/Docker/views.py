# Django
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Project, Docker
import Lib.api

import yaml
import json


def create_project(request):
    """
    Create A Project
    :param request:
    :return:
    """
    return HttpResponse('fuck')


def create_docker_compose_yml(request, project_id):
    """
    Create docker-compose.yml
    """
    project = Project.objects.get(id=project_id)
    if not project:
        # No such project
        return api.fail('No such project')

    docker_compose = {'version': 3, 'services': {}}
    dockers = Docker.objects.filter(project=project)
    for docker in dockers:
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
        local_docker_compose['ports'] = [f"{port.outer}:{port.inner}" for port in ports]

        docker_compose[docker.name] = local_docker_compose

    docker_compose_yml = yaml.dump(docker_compose)

    # TODO: store docker-compose.yml as real file

    return HttpResponse(docker_compose_yml)


def create_docker_compose_yml(request):
    """
    Make docker-compose.yml

    :param request:
    :return:
    """

