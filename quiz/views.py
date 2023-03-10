from rest_framework.response import Response
from quiz.serializers import WriteQuestionSerializer, ReadQuestionSerializer, QuestionMediaSerializer, SolveQuestionSerializer
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema
from quiz.models import Question, Answer
from django.utils.translation import gettext_lazy as _

class WriteQuestionApi(APIView):
    serializer_class = WriteQuestionSerializer
    permission_classes = []

    @extend_schema(tags=['Question'],request=WriteQuestionSerializer, responses=WriteQuestionSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReadQuestionApi(APIView):
    serializer_class = ReadQuestionSerializer
    permission_classes = []

    @extend_schema(tags=['Question'], responses=ReadQuestionSerializer)
    def get(self, request, *args, **kwargs):
        question = Question.objects.all()
        serializer = self.serializer_class(question, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SendMediaApi(APIView):
    serializer_class = QuestionMediaSerializer
    permission_classes = []

    @extend_schema(tags=['Question'], request=QuestionMediaSerializer, responses=QuestionMediaSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SolveQuestionApi(APIView):
    serializer_class = SolveQuestionSerializer
    permission_classes = []

    @extend_schema(tags=['Question'], request=SolveQuestionSerializer, responses=SolveQuestionSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = Question.objects.get(id=serializer.validated_data['question'])
        answer = Answer.objects.get(question=question, id=serializer.validated_data['answer'])
        if answer.is_right:
            return Response(
                {'is_right': True, 'message': _('Congratulations! You have solved the question correctly.')},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'is_right': False, 'message': _('Unfortunately, you have solved the question incorrectly.')},
                status=status.HTTP_200_OK
            )