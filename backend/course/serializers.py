from rest_framework import serializers
from . models import Course

class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('title','order','course','content')

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name','cover','description','is_published','courseprice','pub_date')