from rest_framework import serializers
from . models import MCQuestion,Answer
from quiz.serializers import QuestionSerializers

class MCAnswer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        
class MCQuestionsSerializer(QuestionSerializers):
    qustion_set = MCAnswer(many=True, read_only=True)
    class Meta:
        model = MCQuestion
        fields = '__all__'

