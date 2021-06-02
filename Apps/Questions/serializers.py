from rest_framework import serializers
from django.core import serializers as core_serializers

from .models import Solution, Questions


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['code', 'language', 'questionForSolution']
    
    def save(self):
        solution = Solution(
            code = self.validated_data['code'],
            userSolution = self.context['request'].user,
            language = self.validated_data['language'],
            questionForSolution = Questions.objects.filter(id = self.context['questionID'])
        )

        
        solution.save()
        return solution