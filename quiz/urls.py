from django.urls import path
from quiz.views import WriteQuestionApi, ReadQuestionApi

app_name='quiz'

urlpatterns = [
    path('write/', WriteQuestionApi.as_view(), name='quiz'),
    path('read/', ReadQuestionApi.as_view(), name='quiz'),
]