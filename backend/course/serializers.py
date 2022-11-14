from rest_framework import serializers
from . models import Course,Lesson

class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title','order','course','content')

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('author','name','cover','description','is_published','courseprice','pub_date','slug')
