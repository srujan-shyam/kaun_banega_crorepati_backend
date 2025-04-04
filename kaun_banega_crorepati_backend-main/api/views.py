from django.shortcuts import render
from .models import Question,Answer
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view,permission_classes

@api_view(['POST','GET'])
def questions(request):
    questions = Question.objects.prefetch_related('answers').all()
    # serializer = QuestionSerializer(questions, many=True)
    questions_data = [
        {
            "id": question.id,
            "question": question.text,
            "answers": [
                {"text": answer.text, "correct": answer.correct} for answer in question.answers.all()
            ]
        } for question in questions
    ]
    prizes = Prizes.objects.all()
    prizes_data =[
        {
            "id":{prize.question.id for prize in prizes},
            "amount":{prize.text for prize in prizes}
        }
    ]
    data={"questions_data":questions_data,"prizes_data":prizes_data}
    return Response(data)


