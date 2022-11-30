from rest_framework import serializers
from . models import Course,Lesson,CourseDocuments,CourseVideo

class LessonDocument(serializers.ModelSerializer):
    class Meta:
        model = CourseDocuments
        fields = ('lesson','document')
class CourseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = ('title','video')
class LessonSerializers(serializers.ModelSerializer):
    courseDocument = LessonDocument(read_only=True)
    courseVideo = CourseVideoSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = ('title','order','content','courseDocument','courseVideo','course')

class CourseSerializers(serializers.ModelSerializer):
    lesson = LessonSerializers(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ('pk','author','name','cover','description','is_published','courseprice','pub_date','slug','lesson')
