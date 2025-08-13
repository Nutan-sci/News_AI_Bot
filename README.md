# Real-time News Web App — Repository Skeleton

This repository is a runnable skeleton for a **Real-time News Web Application**:
- Next.js frontend (React) — `frontend/`
- Django backend with DRF — `backend/`
- Celery worker (for fetching & LLM tasks)
- Dockerfiles for frontend & backend
- docker-compose for local development
- Kubernetes manifests for production deployment (`k8s/`)
- GitHub Actions workflow example (`.github/workflows/ci.yml`)

**How to use (local dev)**

1. Backend:
   - `cd backend`
   - Create a virtualenv: `python -m venv .venv && source .venv/bin/activate`
   - Install: `pip install -r requirements.txt`
   - Run migrations: `python manage.py migrate`
   - Start Django: `python manage.py runserver`

2. Frontend:
   - `cd frontend`
   - Install: `npm install`
   - Start dev server: `npm run dev`

3. Or use docker-compose:
   - `docker-compose up --build`

This skeleton is intentionally minimal and focuses on project structure and integration points. You should replace placeholders (e.g. secret keys, provider API keys) before production.


