
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('project/create', views.create_project),
    path('project/<int:project_id>/docker-compose.yml', views.create_docker_compose_yml),
]
