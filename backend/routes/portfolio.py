from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_portfolio():
    return {
        'value': 248430,
        'daily_pnl': 18200,
        'allocation': {'AAPL': 0.4, 'MSFT': 0.35, 'NVDA': 0.25}
    }
