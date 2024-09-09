from django.urls import path, include
from rest_framework import routers, serializers, viewsets, permissions

from . import views
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"students", views.StudentsViewSet, basename="students")
router.register(r"projects", views.ProjectsViewSet, basename="projects")
router.register(r"skills", views.SkillsViewSet, basename="skills")

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", index, name="home"),
    path("student/<int:student_id>/", show_student, name="student"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api", views.api_root, name="api"),
    path("cache", view_logs, name="cache"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('auth/', include('social_django.urls', namespace='social')),
]
urlpatterns += [
    path("", include(router.urls)),
]
