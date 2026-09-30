from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def list_watchlist():
    return ['AAPL', 'MSFT', 'NVDA', 'TSLA']
