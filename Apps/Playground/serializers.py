from django.db.models import fields
from rest_framework import serializers

from .models import Playground

class PlaygroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playground
        fields = []
    
    def save(self):
        playground = Playground(
            player2 = self.context['player2'],
            questionForComp = self.context['questionForComp'],
            player1 = self.context['player1'],
        )

        
        playground.save()
        return Playground