from django.urls import path
from . import views

app_name = "course"
urlpatterns = [
    path('',views.CourseListCreate.as_view(),name="list"),
    path('<str:slug>',views.CourseRetrieve.as_view(),name="detail"),
    path('lesson/create/',views.LeasonListCreate.as_view(),name="create-course"),
    path('lesson/<int:pk>',views.LessonRetrieve.as_view(),name="create-course"),
]
