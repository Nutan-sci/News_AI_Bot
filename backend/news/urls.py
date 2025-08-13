from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='article-list'),
    path('articles/<uuid:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]

# Auth and LLM process endpoints
from django.urls import path
from . import views as news_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .auth_views import RegisterView

urlpatterns += [
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('process_news/', news_views.process_news, name='process-news'),
]
