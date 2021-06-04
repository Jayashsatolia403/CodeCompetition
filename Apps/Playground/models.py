from django.db.models.fields import BLANK_CHOICE_DASH
from Apps.Questions.models import Questions
from django.db import models

from Apps.Users.models import User

class Playground(models.Model):
    questionForComp = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='questionForComp')
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1', null=True, blank=True)
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2', null=True, blank=True)
    player1Solution = models.TextField(null=True, blank=True)
    player2Solution = models.TextField(null=True, blank=True)
    player1SolvedTime = models.DateTimeField(null=True, blank=True)
    player2SolvedTime = models.DateTimeField(null=True, blank=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner', null=True, blank=True)