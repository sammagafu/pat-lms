from rest_framework import generics,filters
from . models import Course,Lesson
from .serializers import CourseSerializers,LessonSerializers
from rest_framework.permissions import AllowAny,IsAuthenticated


from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CourseListCreate(generics.ListCreateAPIView):
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




    