from rest_framework import serializers
from .models import Question, Answer, QuestionMedia

class ReadMediaSerializer(serializers.Serializer):
    media = serializers.FileField(required=False, allow_null=True, allow_empty_file=True, read_only=True)

    def create(self, validated_data):
        return ReadMediaSerializer(**validated_data)

    def update(self,validated_data):
        return ReadMediaSerializer(**validated_data)

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
            'id', 'title', 'description', 'difficulty', 'date_created', 'is_active', 'answer'
        ]

    def create(self, validated_data):
        answers = validated_data.pop('answer')
        self.instance = Question.objects.create(**validated_data)
        QuestionMedia.objects.create(question=self.instance)
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
    question_media = ReadMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id', 'title', 'description', 'difficulty', 'date_created', 'is_active', 'answer', 'question_media'
        ]


class QuestionMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionMedia
        fields = ['id', 'question', 'media']

    def validate(self, attrs):
        if attrs['media'].size > 10485760:
            raise serializers.ValidationError("File size is too large")
        if attrs['media'].content_type not in ['image/jpeg', 'image/png', 'image/gif', 'video/mp4']:
            raise serializers.ValidationError("File type is not supported")
        return attrs




# class SolveQuestionSerializer(serializers.Serializer):
#     answer = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False)

#     def create(self, validated_data):
#         return SolveQuestionSerializer(**validated_data)

#     def update(self,validated_data):
#         return SolveQuestionSerializer(**validated_data)


