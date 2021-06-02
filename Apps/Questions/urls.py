from django.urls import path

from . import views

urlpatterns = [
    path('', views.QuestionsListView.as_view()), 
    path('<pk>', views.questionsDetailView, name='questionsDetailView'),
    path('<questionID>/solution/', views.solutionView, name='solutionView'),
    path('<id>/mysolution/', views.userSolutionView, name='userSolutionView')
]