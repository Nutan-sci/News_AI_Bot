FROM python:3.11-slim

# Install tini for PID 1 signal handling and curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends tini curl && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /srv/app

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install django-filter psycopg2-binary celery redis
# Create non-root user
RUN useradd --create-home appuser
WORKDIR /srv/app
COPY . .
# Copy wait-for-postgres script
COPY wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /wait-for-postgres.sh

RUN chown -R appuser:appuser /srv/app

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
USER appuser

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD curl --fail http://localhost:8000/health/ || exit 1

ENTRYPOINT ["/usr/bin/tini", "--", "/entrypoint.sh"]
