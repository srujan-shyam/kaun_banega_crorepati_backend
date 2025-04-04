from .models import *
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'correct']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']


class PrizeSerializer(serializers.ModelSerializer):
    prizes = Prizes()
    class Meta:
        model = Prizes
        fields = "__all__"