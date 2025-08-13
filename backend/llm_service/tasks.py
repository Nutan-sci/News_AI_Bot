from celery import shared_task
from .services import GeminiClient


@shared_task
def summarize_article(article_text):
    client = GeminiClient()
    return client.summarize(article_text)


@shared_task
def sentiment_analysis(article_text):
    client = GeminiClient()
    return client.analyze_sentiment(article_text)
