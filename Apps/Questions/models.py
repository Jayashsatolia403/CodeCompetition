from django.db import models

from Apps.Users.models import User

class Questions(models.Model):
    title = models.CharField(max_length=50)
    statement = models.TextField()
    example1 = models.CharField(max_length=250, blank=True, null=True)
    example2 = models.CharField(max_length=250, blank=True, null=True)
    example3 = models.CharField(max_length=250, blank=True, null=True)
    constraints = models.CharField(max_length=250, blank=True, null=True)
    picture = models.ImageField(upload_to='upload/questions/', blank=True, null=True)
    dificulty = models.CharField(max_length=250, blank=True, null=True)
    relatedTopics = models.CharField(max_length=250, blank=True, null=True)
    relatedQuestions = models.CharField(max_length=250, blank=True, null=True)
    originalSolution = models.FileField(upload_to="Apps/Questions/Answers/Questions/", blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)


class Solution(models.Model):
    code = models.TextField()
    userSolution = models.ForeignKey(User, related_name='userSolution', on_delete=models.CASCADE, null=True)
    language = models.CharField(max_length=10)
    questionForSolution = models.ForeignKey(Questions, related_name='questionForSolution', on_delete=models.CASCADE, null=True)