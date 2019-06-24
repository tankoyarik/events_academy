"""events_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_swagger.views import get_swagger_view

from events.serializers import CustomJWTSerializer
from events.views import UserCreateView, UserListView

schema_view = get_swagger_view(title="Events API")

urlpatterns = [
    path("", schema_view),
    path("admin/", admin.site.urls),
    path("", include("events.urls")),
    path(
        "api-token-auth/",
        ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer),
    ),
    path("users/create", UserCreateView.as_view()),
    path("users", UserListView.as_view()),
]
