from django.contrib import admin
import nested_admin
from .models import Category, Quiz, Answer, Question

class AnswerAdmin(nested_admin.NestedTabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [AnswerAdmin,]    

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionAdmin,]

#************
class QustionInlineAdmin(nested_admin.NestedModelAdmin):
    inlines = [AnswerAdmin,] 

admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Question, QustionInlineAdmin)
admin.site.register(Quiz,QuizAdmin)







