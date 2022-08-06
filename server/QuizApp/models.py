from unicodedata import category
from django.db import models
from pkg_resources import require


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category Name") #verbose name: admin panel de feild adını custimeze etmeye yarar

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name_plural = "Categories"
    @property    # name gibi attribute olarak kullanabliriz örn: AAA.quiz_count ---  normalde AAA.quiz_count()
    def quiz_count(self):
        return self.quiz_set.count() #hangi modelin sayısı ise küçükharf_set


class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural="Quizzes"
    
    @property   
    def question_count(self):
        return self.question_set.count()

#! ortak kullanacağımız fieldları burada yazıp bu fieldları kullanacağımız modelleri buradan inherite edebiliriz.
class Update(models.Model):
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Question(Update):
    difficulty_options = [
        ("B","BEGINNER"),
        ("I","INTERMADIATE"),
        ("A", "ADVANCED")
    ]
    title = models.CharField(max_length=300, verbose_name="question title")
    difficulty = models.CharField(max_length=1, choices=difficulty_options)
    created_date = models.DateTimeField(auto_now_add=True)
    # updated_date = models.DateTimeField(auto_now=True)  #! Bunu yukarıdaki absract metodu ile hallettik
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE )

    def __str__(self):
        return f'{self.title}'


class Answer(Update):

    text = models.CharField(max_length=300, verbose_name="Answer Text")    
    # updated_date = models.DateTimeField(auto_now=True)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'