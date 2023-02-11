from django.contrib import admin
from quiz.models import Question, Answer
from django.utils.translation import gettext_lazy as _

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'is_active', 'question_type']
    list_filter = ['difficulty', 'is_active', 'question_type']
    search_fields = ['title', 'description']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer_text']
    list_filter = ['question']
    search_fields = ['question', 'answer_text']