from rest_framework import serializers
from . models import Reply,Topic

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ("reply","answered")
        write_only_fields = ("user","topic")


class TopicSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True,read_only=True)

    class Meta:
        model = Topic
        fields = ('topic','content','replies')
        write_only_fields = ('course',"user","slug")

