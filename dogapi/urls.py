from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import controllers

router = DefaultRouter()
router.register(r"dogs", controllers.DogViewSet)
router.register(r"breeds", controllers.BreedViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
