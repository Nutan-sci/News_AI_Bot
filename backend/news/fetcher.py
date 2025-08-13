import os, logging, requests
from datetime import datetime, timezone
from .models import Article

logger = logging.getLogger(__name__)
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')

class ProviderError(Exception):
    pass

def provider_fetch_newsapi(query='technology', page=1, page_size=20):
    """Fetch top headlines using NewsAPI.org (demo)."""
    if not NEWSAPI_KEY:
        raise ProviderError('NEWSAPI_KEY not configured')

    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'q': query,
        'pageSize': page_size,
        'page': page,
        'language': 'en',
        # country can be adjusted
    }
    headers = {'Authorization': NEWSAPI_KEY}
    resp = requests.get(url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    articles = []
    for a in data.get('articles', []):
        normalized = normalize_provider_payload(a)
        articles.append(normalized)
    return articles

def normalize_provider_payload(payload):
    """Map provider fields to canonical Article fields."""
    title = payload.get('title')
    content = payload.get('content') or payload.get('description') or ''
    url = payload.get('url')
    source = payload.get('source', {}).get('name')
    published_at = payload.get('publishedAt')
    try:
        published_at = datetime.fromisoformat(published_at.replace('Z', '+00:00')) if published_at else None
    except Exception:
        published_at = datetime.now(timezone.utc)

    normalized = {
        'title': title,
        'content': content,
        'url': url,
        'source': source,
        'published_at': published_at,
        'category': None,
        'raw_payload': payload
    }
    return normalized

def store_articles(normalized_articles):
    """Insert or update normalized articles into DB."""
    for a in normalized_articles:
        try:
            Article.objects.update_or_create(url=a['url'], defaults={
                'title': a['title'],
                'content': a['content'],
                'source': a['source'],
                'published_at': a['published_at'],
                'category': a.get('category'),
                'raw_payload': a.get('raw_payload')
            })
        except Exception as e:
            logger.exception('Failed to store article %s: %s', a.get('url'), e)
