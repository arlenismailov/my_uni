from django.shortcuts import render
from rest_framework import viewsets

from .models import Focultet, Professor, Student, Course, Office, Schedule, Registrationcourse, Homework, Passingexam
from .serializers import FocultetSerializer, ProfessorSerializer, StudentSerializer, CourseSerializer, OfficeSerializer, \
    ScheduleSerializer, RegistrationcourseSerializer, HomeworkSerializer, PassingexamSerializer


class FocultetViewSets(viewsets.ModelViewSet):
    queryset = Focultet.objects.all()
    serializer_class = FocultetSerializer


class ProfessorViewSets(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSets(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class OfficeViewSets(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class ScheduleViewSets(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class RegistrationcourseViewSets(viewsets.ModelViewSet):
    queryset = Registrationcourse.objects.all()
    serializer_class = RegistrationcourseSerializer


class HomeworkViewSets(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class PassingexamViewSets(viewsets.ModelViewSet):
    queryset = Passingexam.objects.all()
    serializer_class = PassingexamSerializer
