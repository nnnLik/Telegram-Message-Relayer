from typing import Dict

from rest_framework import generics
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import TelegramTokenSerializer
from .services import TokenGenerator


class GetGeneratedToken(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TelegramTokenSerializer

    def post(self, request: Request):
        user = self.request.user
        token_generator: TokenGenerator = TokenGenerator()
        result: Dict[str, str] = token_generator.generate(user)
        return Response(result, status=status.HTTP_201_CREATED)
