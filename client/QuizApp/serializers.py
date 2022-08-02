from rest_framework import serializers
from .models import Quiz, Question, Answer, Category


class CategorySerealizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz_count"     
        )
class QuizSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (            
            "title",
            "question_count"     
        )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "answer_text",
            "is_right",
        )

