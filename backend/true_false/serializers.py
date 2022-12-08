from rest_framework import serializers
from quiz.serializers import QuestionSerializers
from . models import TF_Question

class TFQuestionsSerializer(QuestionSerializers):
    class Meta:
        model = TF_Question
        fields = '__all__'