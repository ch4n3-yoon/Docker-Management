
from django.urls import path
from .views import create_project, create_docker_compose_yml

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('project/create', create_project),
    path('project/<int:project_id>/docker-compose.yml', create_docker_compose_yml),
]
