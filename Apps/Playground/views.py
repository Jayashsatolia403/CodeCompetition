from django.db.models.query import QuerySet
from Apps.Questions.models import Questions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Apps.Users.models import User

from subprocess import check_output

from .serializers import PlaygroundSerializer
import random
from .models import Playground


@api_view(['POST', ])
def createPlayground(request):
    player1 = request.user
    player1.isPlaying = True
    player1.save()
    
    player2s = User.objects.all()
    player2List = []

    for player2 in player2s:
        if player2.isPlaying:
            player2List.append(player2)
    
    player2 = player2List[1]

    questions = Questions.objects.all()
    questionList = []

    for question in questions:
        questionList.append(question)
    
    questionForComp = questionList[0]

    playgroundSerializer = PlaygroundSerializer(data = request.data, context = {'player1': player1, 'player2': player2, 'questionForComp': questionForComp})

    if playgroundSerializer.is_valid():
        playgroundSerializer = playgroundSerializer.save()
    
    return Response({"Yo":"Yo"})




@api_view(['POST', ])
def playerSolution(request, playgroundId):
    playground = Playground.objects.get(id=playgroundId)

    

    if playground.winner != None:
        return Response("Winner is {}".format(playground.winner))

    if playground.player1 == request.user:
        playground.player1Solution = request.data['playerSolution']
    
        path = r"C:/Users/Jayash Satolia/OneDrive/Desktop/APIs/CodeCompetitionHelper/Apps/Playground/Answers/Questions"
        
        filename = path + str(playground.questionForComp) + "_" + str(request.user.username) + ".py"
        with open(filename, "w") as file:
            file.write(playground.player1Solution)
        
        answer = "./" + str(playground.questionForComp.originalSolution)
        data = {}
        try:
            x = check_output("python {} {}".format(answer, filename), shell=True)
            data["Output"] = str(x)
            playground.winner = request.user
        except Exception as error:
            data["Output"] = str(error)
        

        return Response(data)
    
    elif playground.player2 == request.user:
        playground.player2Solution = request.data['playerSolution']
    
        path = r"C:/Users/Jayash Satolia/OneDrive/Desktop/APIs/CodeCompetitionHelper/Apps/Playground/Answers/Questions/"
        
        filename = path + str(playground.questionForComp) + "_" + str(request.user.username) + ".py"
        with open(filename, "w") as file:
            file.write(playground.player2Solution)
        
        answer = "./" + str(playground.questionForComp.originalSolution)
        data = {}
        try:
            x = check_output("python {} {}".format(answer, filename), shell=True)
            data["Output"] = str(x)
            playground.winner = request.user
        except Exception as error:
            data["Output"] = str(error)
        

        return Response(data)



    playground.save()
    
    return Response("Wrong!")
