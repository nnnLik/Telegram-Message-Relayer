from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Telegram-Message-Relayer API",
        default_version="v3.1.3",
        description="Telegram-Message-Relayer Api implementation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    urlconf="config.urls",
)
