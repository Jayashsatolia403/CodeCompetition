from rest_framework import status
from rest_framework.response import Response
from .models import Questions, Solution
from .serializers import QuestionsSerializer, SolutionSerializer

from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view

from subprocess import check_output

class QuestionsListView(ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

@api_view(['GET',])
def questionsDetailView(request, pk):
    try:
        questions = Questions.objects.get(pk=pk)
    except Questions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = QuestionsSerializer(questions)
        return Response(serializer.data)

@api_view(['POST',])
def solutionView(request, questionID):
    if request.method == 'POST':
        print(request.data['code'])
        path = "Apps/Questions/Answers/Questions/"
        serializer = SolutionSerializer(data=request.data, context={'request': request, 'questionID': questionID})
        data = {}
        if serializer.is_valid():
            submittedSolution = serializer.save()
            data['response'] = "Waiting For Validataion"
            data['code'] = submittedSolution.code
            data['language'] = submittedSolution.language
            filename = path + str(submittedSolution.questionForSolution) + "_" + str(submittedSolution.userSolution.username) + ".py"
            with open(filename, "w") as file:
                file.write(submittedSolution.code)
            
            answer = "./" + str(submittedSolution.questionForSolution.originalSolution)

            try:
                x = check_output("python {}".format(answer), shell=True)
                data["Output"] = str(x)
            except Exception as error:
                data["Output"] = str(error)
            
        else:
            data = serializer.errors

        return Response(data)


@api_view(['GET',])
def userSolutionView(request, id):
    id = int(id)
    print(" >>> ", id)
    data = {}
    x = Solution.objects.filter(userSolution = request.user, questionForSolution=id)
    x = [i.code for i in x]
    data['Your Answer'] = x

    print(data)
    return Response(data)
