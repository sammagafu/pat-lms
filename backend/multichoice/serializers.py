from rest_framework import serializers
from . models import MCQuestion
from quiz.serializers import QuestionSerializers

class MCQuestionsSerializer(QuestionSerializers):
    class Meta:
        model = MCQuestion
        fields = '__all__'