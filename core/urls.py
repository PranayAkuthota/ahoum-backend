"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


def home(request):
    return JsonResponse({
        "message": "Ahoum Backend Assignment API",
        "docs": "/api/docs/"
    })


urlpatterns = [
    path("", home),

    path("admin/", admin.site.urls),

    path(
        "auth/",
        include("accounts.urls")
    ),

    path(
        "events/",
        include("events.urls")
    ),

    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
    ),
]
