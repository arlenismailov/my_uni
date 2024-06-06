from django.shortcuts import render
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
class passingexamViewSets(viewsets.ModelViewSet):
	queryset = passingexam.objects.all()
	serializer_class = passingexamSerializer