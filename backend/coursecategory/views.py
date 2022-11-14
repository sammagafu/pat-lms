from .serializer import CategorSerializer
from rest_framework import generics
from .models import ProuctCategory

class CategoryListView(generics.ListCreateAPIView):
    queryset = ProuctCategory.objects.all()
    serializer_class = CategorSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = ProuctCategory.objects.all()
    serializer_class = CategorSerializer
    lookup_field = 'slug'
