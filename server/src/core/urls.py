from django.urls import path

from .views import GetGeneratedToken

urlpatterns = [
    path("generate/", GetGeneratedToken.as_view(), name="generate"),
]
