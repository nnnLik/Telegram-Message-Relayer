from typing import Dict

from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import SendTelegramMessageSerializer, TelegramTokenSerializer, TokenUpdateSerializer
from .services import MessageServices, TokenServices


class GetGeneratedTokenView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TelegramTokenSerializer

    def post(self, request: Request):
        user: User = self.request.user
        token_generator: TokenServices = TokenServices()
        result: Dict[str, str] = token_generator.generate(user)
        return Response(result, status=status.HTTP_201_CREATED)


class UpdateTokenStatusView(generics.UpdateAPIView):
    serializer_class = TokenUpdateSerializer

    def put(self, request: Request):
        token_generator: TokenServices = TokenServices()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        chat_id: int = serializer.validated_data["chat_id"]
        username: str = serializer.validated_data["username"]
        token: str = serializer.validated_data["token"]

        result, status_code = token_generator.update_token_status(
            chat_id, username, token
        )
        return Response(result, status=status_code)


class SendMessageView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SendTelegramMessageSerializer

    def post(self, request: Request):
        message_service: MessageServices = MessageServices()
        user: User = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        msg: str = serializer.validated_data["message"]

        result, status_code = message_service.create_msg(user, msg)
        return Response(result, status=status_code)
