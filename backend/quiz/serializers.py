from .models import Question,Quiz,Progress
from rest_framework import serializers

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('figure','content','explanation')

class ProgressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('user','score')

class QuizSerializers(serializers.ModelSerializer):
    question_set = QuestionSerializers(many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = ('title','course','description','url',
        'random_order','max_questions','answers_at_end',
        'exam_paper','single_attempt','pass_mark','success_text','fail_text','draft','question_set','get_max_score')
