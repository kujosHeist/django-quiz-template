from django.contrib import admin
from .models import Quiz

# Register your models here.

admin.site.register(Quiz)

class QuestionAdmin(admin.StackedInline):
    model = Quiz
class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuizAdmin(admin.ModelAdmin):
    inlines = [ QuestionAdmin ]