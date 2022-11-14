from django.urls import path
from . import views

app_name = "course"
urlpatterns = [
    path('',views.CourseListCreate.as_view(),name="list"),
]
