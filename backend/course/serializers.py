from rest_framework import serializers
from . models import Course,Lesson,CourseDocuments,CourseVideo,CourseEnrollment
from discussions.serializers import TopicSerializer

class LessonDocument(serializers.ModelSerializer):
    class Meta:
        model = CourseDocuments
        fields = ('lesson','title','document')
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
    course_topic = TopicSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ('pk','author','name','points','cover','description','is_published','courseprice','pub_date','slug','lesson','course_topic')

class EnrolledCourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = ("course","student","is_paid")