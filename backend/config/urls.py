from django.contrib import admin
from django.urls import path, include
from news.views import api_root
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def api_root(request):
    return JsonResponse({
        "articles": "/api/articles/",
        "auth": {
            "register": "/api/auth/register/",
            "token": "/api/auth/token/",
            "token_refresh": "/api/auth/token/refresh/"
        },
        "process_news": "/api/process_news/"
    })


def health_check(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('api/', api_root, name = "api_root" ),
    path("api/articles/", include("news.urls")),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

] 