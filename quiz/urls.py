from django.urls import path
from quiz.views import WriteQuestionApi, ReadQuestionApi, SendMediaApi, SolveQuestionApi

app_name='quiz'

urlpatterns = [
    path('write/', WriteQuestionApi.as_view(), name='send_question'),
    path('read/', ReadQuestionApi.as_view(), name='read_question'),
    path('media/', SendMediaApi.as_view(), name='send_media'),
    path('solve/', SolveQuestionApi.as_view(), name='solve_question'),
]