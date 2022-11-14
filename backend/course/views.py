from rest_framework import generics,filters
from . models import Course
from .serializers import CourseSerializers

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    # filterset_fields = ['is_published', 'courseprice','pub_date']
    # ordering_fields = ['pub_date','courseprice']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)