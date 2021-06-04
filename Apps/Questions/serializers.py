from rest_framework import serializers

from .models import Solution, Questions


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['title', 'statement', 'example1', 'example2', 'example3', 'constraints', 'picture', 'dificulty', 'relatedTopics', 'relatedQuestions']

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['code', 'language']
    
    def save(self):
        solution = Solution(
            code = self.validated_data['code'],
            userSolution = self.context['request'].user,
            language = self.validated_data['language'],
            questionForSolution = Questions.objects.filter(id = self.context['questionID'])[0]
        )

        
        solution.save()
        return solution