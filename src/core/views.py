from typing import Dict

from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from src.base.services.token import TokenServices
from src.base.services.msg import MessageServices

from .serializers import SendTelegramMessageSerializer, TelegramTokenSerializer


class GetGeneratedTokenView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TelegramTokenSerializer

    def post(self, request: Request):
        user: User = self.request.user
        token_generator: TokenServices = TokenServices()
        result: Dict[str, str] = token_generator.generate(user)
        return Response(result, status=status.HTTP_201_CREATED)


class SendMessageView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SendTelegramMessageSerializer

    def post(self, request: Request):
        message_service: MessageServices = MessageServices()
        user: User = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        msg: str = serializer.validated_data["message"]

        success: bool = message_service.send_message(user, msg)
        if success:
            return Response(
                {"message": "Your message has been delivered successfully."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Your message was not delivered."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
