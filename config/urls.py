from django.contrib import admin
from django.urls import path, include

from src.router import routes

from .yasg import schema_view


urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("admin/", admin.site.urls),
    path("api/", include(routes)),
    path(
        "swagger/",
        schema_view.with_ui("swagger"),
        name="schema-swagger-ui",
    ),
]
