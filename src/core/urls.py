from django.urls import path

from .views import GetGeneratedTokenView, SendMessageView, GetMessageHistory

urlpatterns = [
    path("generate/", GetGeneratedTokenView.as_view(), name="generate-token"),
    path("send/", SendMessageView.as_view(), name="send-message"),
    path("history/", GetMessageHistory.as_view(), name="history"),
]
