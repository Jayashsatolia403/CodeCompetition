from django.urls import path, include

from .views import createPlayground, playerSolution

urlpatterns = [
    path('create/', createPlayground, name='createPlayground'),
    path('<playgroundId>/solution/', playerSolution, name='playerSolution')
]