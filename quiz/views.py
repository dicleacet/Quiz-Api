from rest_framework.response import Response
from quiz.serializers import WriteQuestionSerializer, ReadQuestionSerializer
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import extend_schema

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
        serializer = self.serializer_class()
        return Response(serializer.data, status=status.HTTP_200_OK)
