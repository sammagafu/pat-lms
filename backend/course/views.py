from rest_framework import generics,filters
from . models import Course,Lesson,CourseEnrollment
from .serializers import CourseSerializers,LessonSerializers,EnrolledCourseSerializers
from rest_framework import permissions 
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CourseListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CourseRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    lookup_field = "slug"


class LeasonListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class LessonRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers

class EnrolledCourse(generics.ListCreateAPIView):
    queryset = CourseEnrollment.objects.all()
    serializer_class = EnrolledCourseSerializers
    permission_classes = [permissions.IsAuthenticated,]


    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            student=self.request.user
        )

    