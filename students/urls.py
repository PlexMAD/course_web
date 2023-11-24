from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from . import views
from .views import *



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', views.StudentsViewSet, basename='students')
router.register(r'projects', views.ProjectsViewSet, basename='projects')
router.register(r'skills', views.SkillsViewSet, basename='skills')

urlpatterns = [
    path('', index, name='home'),
    path('student/<int:student_id>/', show_student, name='student'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api', views.api_root, name='api'),
]
urlpatterns += [
    path('', include(router.urls)),
]
