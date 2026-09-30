# Architecture Overview

## Components
- Frontend: React + TypeScript + Vite + Tailwind UI for dashboards and charts
- Backend: FastAPI with REST routers for auth, stocks, predictions, portfolio, watchlist, news, admin
- Data layer: MySQL schema with normalized tables, views, procedures, and indexes
- ML layer: Python-based forecasting pipeline and model comparison logic

## Flow
1. User interacts with the frontend dashboard.
2. Frontend calls FastAPI endpoints.
3. Backend queries MySQL and orchestrates model inference.
4. ML pipeline generates predictions, confidence, and recommendations.
5. Results are returned to the UI and stored in the database.
