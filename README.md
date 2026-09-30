# StockVision AI

StockVision AI is a premium fintech-style platform for stock analysis, forecasting, portfolio tracking, and AI-powered recommendations.

## Features
- React + TypeScript + Vite frontend
- FastAPI backend with modular routes
- ML pipeline for forecasting and model comparison
- MySQL schema for users, predictions, portfolios, watchlists, news, and analytics
- Production-oriented documentation and deployment scaffolding

## Quick start

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Database
Import [database/schema.sql](database/schema.sql) into MySQL.

## Project structure
- frontend/
- backend/
- database/
- docs/
- deployment/
