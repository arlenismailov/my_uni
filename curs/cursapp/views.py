from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Department,
    Professor,
    Student,
    Course,
    Office,
    Schedule,
    RegistrationCourse,
    Homework,
    PassingExam,
)
from .serializers import (
    DepartmentSerializer,
    ProfessorSerializer,
    StudentSerializer,
    CourseSerializer,
    OfficeSerializer,
    ScheduleSerializer,
    RegistrationCourseSerializer,
    HomeworkSerializer,
    PassingExamSerializer,
)


class DepartmentViewSets(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


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


class RegistrationCourseViewSets(viewsets.ModelViewSet):
    queryset = RegistrationCourse.objects.all()
    serializer_class = RegistrationCourseSerializer


class HomeworkViewSets(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class PassingExamViewSets(viewsets.ModelViewSet):
    queryset = PassingExam.objects.all()
    serializer_class = PassingExamSerializer
