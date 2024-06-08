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
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "all"


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "all"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "all"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "all"


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "all"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "all"


class RegistrationCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationCourse
        fields = "all"


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "all"


class PassingExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassingExam
        fields = "all"
