
from django.urls import path
from .views import create_project

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('project/create', create_project),
]
