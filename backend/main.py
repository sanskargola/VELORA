from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, stocks, predictions, portfolio, watchlist, news, admin

app = FastAPI(title='StockVision AI API', version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router, prefix='/api/auth', tags=['auth'])
app.include_router(stocks.router, prefix='/api/stocks', tags=['stocks'])
app.include_router(predictions.router, prefix='/api/predictions', tags=['predictions'])
app.include_router(portfolio.router, prefix='/api/portfolio', tags=['portfolio'])
app.include_router(watchlist.router, prefix='/api/watchlist', tags=['watchlist'])
app.include_router(news.router, prefix='/api/news', tags=['news'])
app.include_router(admin.router, prefix='/api/admin', tags=['admin'])

@app.get('/api/health')
def health():
    return {'status': 'ok', 'service': 'StockVision AI'}
