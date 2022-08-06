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
            "text",
            "is_right"
        )

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    difficulty = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = (
            "title",
            "answer",
            "difficulty"
        )
    def get_difficulty(self, obj):
        return obj.get_difficulty_display()

