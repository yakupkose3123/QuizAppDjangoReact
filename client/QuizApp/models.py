from unicodedata import category
from django.db import models
from pkg_resources import require

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category Name")

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name_plural = "Categories"
    @property    # name gibi attribute olarak kullanabliriz örn: AAA.quiz_count ---  normalde AAA.quiz_count()
    def quiz_count(self):
        return self.quiz_set.count()


class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name="Quiz Title")
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural="Quizzes"
    
    @property   
    def question_count(self):
        return self.question_set.count()


class Question(models.Model):
    difficulty_options = [
        ("B","BASIC"),
        ("I","INTERMADIATE"),
        ("A", "ADVANCED")
    ]
    title = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=1, choices=difficulty_options)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE )

    def __str__(self):
        return f'{self.title}'


class Answer(models.Model):

    text = models.CharField(max_length=100, verbose_name="Answer Text")    
    updated_date = models.DateTimeField(auto_now=True)
    is_right = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'