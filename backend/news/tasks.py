from celery import shared_task
from .models import Article
import requests, logging

logger = logging.getLogger(__name__)

@shared_task
def fetch_from_provider_dummy():
    # This is a placeholder task. Replace with real provider calls.
    dummy = {
        'title': 'Provider: Demo article',
        'content': 'This is a demo article inserted by the fetcher.',
        'url': 'https://example.com/demo-article',
        'source': 'demo',
    }
    Article.objects.update_or_create(url=dummy['url'], defaults=dummy)
    logger.info('Inserted demo article')

from .fetcher import provider_fetch_newsapi, store_articles, ProviderError
from .models import Article
from llm_service.tasks import summarize_article, sentiment_analysis
import logging
logger = logging.getLogger(__name__)

@shared_task
def scheduled_fetch_newsapi(query='technology'):
    try:
        arts = provider_fetch_newsapi(query=query)
        store_articles(arts)
        # Launch summarization + sentiment for newest articles
        for a in arts:
            if a.get('url'):
                summarize_article.delay(a.get('content') or a.get('title'))
                sentiment_analysis.delay(a.get('content') or a.get('title'))
    except ProviderError as e:
        logger.error('ProviderError: %s', e)
    except Exception as e:
        logger.exception('fetch failed: %s', e)
