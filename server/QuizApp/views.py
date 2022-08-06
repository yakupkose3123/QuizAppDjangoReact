from rest_framework import generics
from .models import Category, Quiz, Question
from .serializers import CategorySerealizer, QuizSerealizer, QuestionSerializer
from .permission import IsStafforReadOnly



class CategoryList(generics.ListAPIView):
    serializer_class= CategorySerealizer
    queryset = Category.objects.all()
    permission_classes = (IsStafforReadOnly,)  #! For permission
    
    
class CategoryDetail(generics.ListAPIView):
    serializer_class = QuizSerealizer
    permission_classes = (IsStafforReadOnly,)  #! For permission
    
    def get_queryset(self): #url den gelen category e göre listelemesi için bu methodu override alıyoruz
        queryset = Quiz.objects.all()
        category = self.kwargs["category"]  #backend, frontend
        queryset = queryset.filter(category__name=category) # 2 underscore ile parent modelin fieldlarına ulaşabiliyoruz(quiz tablosunda category id ler ile kayıtlı olduğu için - foreignkey)
        return queryset


class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsStafforReadOnly,)  #! For permission
    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title=title) 
        return queryset
