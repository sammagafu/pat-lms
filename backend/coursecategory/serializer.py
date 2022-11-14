from rest_framework import serializers
from .models import ProuctCategory, ProductSubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = ['subcategoryname', 'slug']

class CategorSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = ProuctCategory
        fields = ['id','categoryname', 'slug','subcategory']