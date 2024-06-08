from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

class GradeMixin:
    OPTION_VERY_GOOD = "very good"
    OPTION_GOOD = "good"
    OPTION_NORMALLY = "normally"
    OPTION_BAD = "bad"
    GRADE_CHOICES = (
        (OPTION_VERY_GOOD, _("Very good")),
        (OPTION_GOOD, _("Good")),
        (OPTION_NORMALLY, _("Normally")),
        (OPTION_BAD, _("Bad")),
    )

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Department name"))
    description = models.TextField(_("Description"))


class Professor(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    department = models.models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    bio = models.TextField(_("Bio"))


class Student(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE)
    enrollment_date = models.DateField(verbose_name=_("Enrollment date"),)
    graduation_date = models.DateField(verbose_name=_("Graduation_date"),)

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))
    code = models.SlugField(max_length=50, verbose_name=_("Code"))
    description = models.TextField(_("Description"))
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, verbose_name=_("Professor"), on_delete=models.CASCADE)


class Office(models.Model):
    OPTION_ONE = "1"
    OPTION_TWO = "2"
    OPTION_THREE = "3"
    BUILDING_CHOICES = (
        (OPTION_ONE, "1"),
        (OPTION_TWO, "2"),
        (OPTION_THREE, "3"),
    )
    
    room_number = models.CharField(max_length=50, verbose_name=_("Room number"))
    building = models.CharField(max_length=50, choices=BUILDING_CHOICES, verbose_name=_("Room number"))
    capacity = models.IntegerField(verbose_name=_("Capacity"))


class Schedule(models.Model):
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    classroom = models.ForeignKey(Office, verbose_name=_("Classroom"), on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name=_("Start_time"))
    end_time = models.TimeField(verbose_name=_("Start_time"))
    day_of_week = ArrayField(models.IntegerField(), size=10, verbose_name=_("Day of Week"))


class RegistrationCourse(GradeMixin, models.Model):
    student = models.ForeignKey(Student, verbose_name=_("Student"), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    enrollment_date = models.DateField(verbose_name=_("Enrollment date")) 
    grade = models.CharField(choices=GradeMixin.GRADE_CHOICES, verbose_name=_("Grade"))


class Homework(models.Model):
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True, verbose_name=_("Title"))
    description = models.TextField(_("Description"))
    due_date = models.DateField(verbose_name=_("Deadline"))


class PassingExam(GradeMixin, models.Model):
    assignment = models.ForeignKey(Homework, verbose_name=_("Homework"), on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name=_("Student"), on_delete=models.CASCADE)
    submission_date = models.DateField(verbose_name=_("Submission date"))
    grade = models.CharField(choices=GradeMixin.GRADE_CHOICES, verbose_name=_("Grade"))
    feedback = models.TextField(_("Feedback"))


