from django.urls import path

from .views import GetGeneratedTokenView, SendMessageView

urlpatterns = [
    path("generate/", GetGeneratedTokenView.as_view(), name="generate-token"),
    path("send/", SendMessageView.as_view(), name="send-message"),
]
