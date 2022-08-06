from django.urls import path, include
from rest_framework import routers 
from .views import CategoryView, QuizView, QuestionView
from .models import Question

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('quizzes', QuizView)
router.register('question', QuestionView)


urlpatterns = [
    path('_nested_admin/', include('nested_admin.urls')),
]

urlpatterns += router.urls