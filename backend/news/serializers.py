from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','content','url','source','published_at','category','summary','sentiment_score','sentiment_label']
