from django.urls import path
from .views import (
    hello_api,
    course_list,
    course_detail,
    student_list,
    student_detail,
    enrollment_list,
    department_list,
)

urlpatterns = [
    path("hello/", hello_api),

    path("courses/", course_list),
    path("courses/<int:pk>/", course_detail),

    path("students/", student_list),
    path("students/<int:pk>/", student_detail),

    path("enrollments/", enrollment_list),
    path("departments/", department_list),
]