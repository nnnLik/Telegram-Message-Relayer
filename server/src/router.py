from django.urls import path, include


routes = [
    path("core/", include("src.core.urls"), name="core"),
]
