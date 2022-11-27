from rest_framework import serializers
from . models import Course,Lesson

class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title','order','content')
        write_only_fields = ('course')

class CourseSerializers(serializers.ModelSerializer):
    lesson = LessonSerializers(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ('pk','author','name','cover','description','is_published','courseprice','pub_date','slug','lesson')
