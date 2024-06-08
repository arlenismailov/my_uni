from .views import (
    DepartmentViewSets,
    ProfessorViewSets,
    StudentViewSets,
    CourseViewSets,
    OfficeViewSets,
    ScheduleViewSets,
    RegistrationCourseViewSets,
    HomeworkViewSets,
    PassingExamViewSets,
)
from django.urls import path

urlpatterns = [
    path(
        "department/",
        DepartmentViewSets.as_view({"get": "list", "post": "create"}),
        name="department_list",
    ),
    path(
        "department/<int:pk>/",
        DepartmentViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="department_detail",
    ),
    path(
        "professor/",
        ProfessorViewSets.as_view({"get": "list", "post": "create"}),
        name="professor_list",
    ),
    path(
        "professor/<int:pk>/",
        ProfessorViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="professor_detail",
    ),
    path(
        "student/",
        StudentViewSets.as_view({"get": "list", "post": "create"}),
        name="student_list",
    ),
    path(
        "student/<int:pk>/",
        StudentViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="student_detail",
    ),
    path(
        "course/",
        CourseViewSets.as_view({"get": "list", "post": "create"}),
        name="course_list",
    ),
    path(
        "course/<int:pk>/",
        CourseViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="course_detail",
    ),
    path(
        "office/",
        OfficeViewSets.as_view({"get": "list", "post": "create"}),
        name="office_list",
    ),
    path(
        "office/<int:pk>/",
        OfficeViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="office_detail",
    ),
    path(
        "schedule/",
        ScheduleViewSets.as_view({"get": "list", "post": "create"}),
        name="schedule_list",
    ),
    path(
        "schedule/<int:pk>/",
        ScheduleViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="schedule_detail",
    ),
    path(
        "registration_course/",
        RegistrationCourseViewSets.as_view({"get": "list", "post": "create"}),
        name="registration_course_list",
    ),
    path(
        "registration_course/<int:pk>/",
        RegistrationCourseViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="registration_course_detail",
    ),
    path(
        "homework/",
        HomeworkViewSets.as_view({"get": "list", "post": "create"}),
        name="homework_list",
    ),
    path(
        "homework/<int:pk>/",
        HomeworkViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="homework_detail",
    ),
    path(
        "passing_exam/",
        PassingExamViewSets.as_view({"get": "list", "post": "create"}),
        name="passing_exam_list",
    ),
    path(
        "passing_exam/<int:pk>/",
        PassingExamViewSets.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="passing_exam_detail",
    ),
]
