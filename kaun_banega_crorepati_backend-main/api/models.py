from django.db import models
from django.core.exceptions import ValidationError
class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.correct else 'Incorrect'})"
    def clean(self):
        # Ensure that there is only one correct answer for each question
        if self.correct:
            # Count how many answers for this question are marked as correct
            if self.question.answers.filter(correct=True).exclude(id=self.id).exists():
                raise ValidationError("Only one answer can be correct.")
            

class Prizes(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.PositiveIntegerField()
