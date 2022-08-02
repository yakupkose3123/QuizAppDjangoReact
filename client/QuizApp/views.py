from django.shortcuts import render
from rest_framework import viewsets
from .models import Question, Answer, Quiz, Category
from .serializers import CategorySerealizer , QuizSerealizer, AnswerSerializer
from .permission import IsStafforReadOnly


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerealizer
    permission_classes = (IsStafforReadOnly,)  #! For permission



class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerealizer
    permission_classes = (IsStafforReadOnly,)  #! For permission




