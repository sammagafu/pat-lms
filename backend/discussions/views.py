from django.shortcuts import render
from .models import Topic, Reply
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny,IsAuthenticated
from . serializers import TopicSerializer
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.

class CourseListView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user=self.request.user
        )

class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


# class EnrollCourse(generics.ListCreateAPIView):
#     queryset = E