import django_filters
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from .models import *
from rest_framework.parsers import JSONParser

from .permissions import IsOwnerOrReadOnly
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import action


def index(request):
    student_list = Students.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'students_list': student_list,
        'title': 'Портфолио',
        'num_visits': num_visits
    }
    return render(request, 'students/index.html', context=context)


def show_student(request, student_id):
    if int(student_id) > len(Students.objects.all()):
        return redirect('home', permanent=False)
    student = Students.objects.get(pk=student_id)
    try:
        workexperience = Workexperiences.objects.get(student_id=student_id)
    except:
        workexperience = 0
    try:
        education = Education.objects.get(student_id=student_id)
    except:
        education = 0
    try:
        certificates = Certificates.objects.filter(student_id=student_id)
        if len(certificates) == 0:
            certificates = 0
    except:
        certificates = 0
    context = {
        'student': student,
        'title': 'Информация о студенте',
        'workexperience': workexperience,
        'education': education,
        'certificates': certificates,
    }
    return render(request, 'students/student_page.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False)
    def second_course_of_studying(self, request):
        students = Students.objects.all().filter(Q(birth_date__startswith="2004") | Q(birth_date__startswith="2003"))

        page = self.paginate_queryset(students)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'students': reverse('students-list', request=request, format=format),
        'projects': reverse('projects-list', request=request, format=format),
        'skills': reverse('skills-list', request=request, format=format),
    })
