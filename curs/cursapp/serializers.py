from .models import Focultet, Professor, Student, Course, Office, Schedule, Registrationcourse, Homework, Passingexam
from rest_framework import serializers


class FocultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Focultet
        fields = 'all'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = 'all'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'all'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = 'all'


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = 'all'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = 'all'


class RegistrationcourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrationcourse
        fields = 'all'


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = 'all'


class PassingexamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passingexam
        fields = 'all'
