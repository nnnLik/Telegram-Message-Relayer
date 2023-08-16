from django.urls import path

from .views import GetGeneratedTokenView, UpdateTokenStatusView, SendMessageView

urlpatterns = [
    path("generate/", GetGeneratedTokenView.as_view(), name="generate-token"),
    path("update-status/", UpdateTokenStatusView.as_view(), name="update-token-status"),
    path("send/", SendMessageView.as_view(), name="send-message"),
]
