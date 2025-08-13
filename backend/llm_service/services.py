import os
import logging
import requests

logger = logging.getLogger(__name__)

class GeminiClient:
    def __init__(self, api_key=None, model=None, mock=False):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model or os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        self.mock = mock or os.getenv("LLM_MOCK_MODE", "false").lower() == "true"
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"

    def summarize(self, text: str) -> str:
        if self.mock:
            return f"[MOCK SUMMARY] {text[:60]}..."
        
        payload = {
            "contents": [{"parts": [{"text": f"Summarize: {text}"}]}]
        }
        url = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"
        
        try:
            res = requests.post(url, json=payload)
            res.raise_for_status()
            data = res.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            logger.error(f"Gemini API Error: {e}")
            return None

    def analyze_sentiment(self, text: str) -> str:
        if self.mock:
            return "[MOCK SENTIMENT] Neutral"
        
        prompt = f"Analyze sentiment (Positive, Negative, Neutral) for this text: {text}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        url = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"

        try:
            res = requests.post(url, json=payload)
            res.raise_for_status()
            data = res.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            logger.error(f"Gemini API Error: {e}")
            return None
