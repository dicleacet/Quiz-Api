from django.contrib import admin
from quiz.models import Question, Answer, QuestionMedia
from django.utils.translation import gettext_lazy as _

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficulty', 'date_created', 'is_active')
    list_display_links = ('id', 'title')
    list_filter = ('difficulty', 'is_active')
    search_fields = ('title', 'description')
    
    fieldsets = (
        (_('Question'), {
            'fields': ('title', 'description', 'difficulty', 'is_active')
        }),
    )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer_text', 'is_right')
    list_display_links = ('id', 'question')
    list_filter = ('is_right',)
    search_fields = ('question', 'answer_text')

@admin.register(QuestionMedia)
class QuestionMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'media')
    list_display_links = ('id', 'question')
    search_fields = ('question', 'media')