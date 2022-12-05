from django.urls import path,include
from . import views
urlpatterns =[
    path('',views.CourseListView.as_view(),name="topic"),
    path('<str:slug>', views.CourseDetailView.as_view(),name="detail")

]
