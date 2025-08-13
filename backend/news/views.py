from rest_framework import generics, filters
from .models import Article
from .serializers import ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.order_by('-published_at').all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['category', 'source']

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from llm_service.tasks import summarize_article, sentiment_analysis
from django.urls import reverse

@api_view(["GET"])
def api_root(request):
    return Response({
        "articles": request.build_absolute_uri(reverse("article-list")),
        "register": request.build_absolute_uri(reverse("auth-register")),
        "token": request.build_absolute_uri(reverse("token-obtain-pair")),
        "process_news": request.build_absolute_uri(reverse("process-news")),
    })

@api_view(["POST"])
def process_news(request):
    text = request.data.get("text")
    if not text:
        return Response({"error": "No text provided"}, status=400)
    
    summary_task = summarize_article.delay(text)
    sentiment_task = sentiment_analysis.delay(text)

    return Response({
        "summary_task_id": summary_task.id,
        "sentiment_task_id": sentiment_task.id
    })


