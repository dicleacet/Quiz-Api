from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.Serializer):
    answer_text = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False)
    is_right = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return AnswerSerializer(**validated_data)

    def update(self,validated_data):
        return AnswerSerializer(**validated_data)


class WriteQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, required=True, allow_null=False, write_only=True)

    class Meta:
        model = Question
        fields = [
            'id', 'title', 'description', 'difficulty', 'date_created', 'is_active', 'question_type', 'answer'
        ]

    def create(self, validated_data):
        answers = validated_data.pop('answer')
        self.instance = Question.objects.create(**validated_data)
        
        answers_list = []
        for answer in answers:
            answers_list.append(Answer(
                question=self.instance,
                answer_text=answer['answer_text'],
                is_right=answer['is_right']
            ))
        Answer.objects.bulk_create(answers_list)
        return self.instance


class ReadQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id', 'title', 'description', 'difficulty', 'date_created', 'is_active', 'question_type', 'answer'
        ]