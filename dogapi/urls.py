from django.urls import path
from . import controllers

urlpatterns = [
    path("dogs/", controllers.DogList.as_view()),
    path("dogs/<int:pk>/", controllers.DogDetail.as_view()),
    path("breeds/", controllers.BreedList.as_view()),
    path("breeds/<int:pk>/", controllers.BreedDetail.as_view()),
]
