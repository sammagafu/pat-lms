from django.urls import path
from . import views

urlpatterns = [
    path("",views.CategoryListView.as_view()),
    path("<str:slug>/",views.CategoryDetailView.as_view())
]