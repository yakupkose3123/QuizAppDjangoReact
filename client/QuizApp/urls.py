from django.urls import path, include
from rest_framework import routers 
from .views import CategoryView, QuizView


router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('quizzes', QuizView)


urlpatterns = [
    # ...
    path('_nested_admin/', include('nested_admin.urls')),
]

urlpatterns += router.urls