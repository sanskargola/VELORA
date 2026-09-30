from fastapi import APIRouter

router = APIRouter()

@router.get('/{symbol}')
def get_stock(symbol: str):
    return {'symbol': symbol, 'price': 182.4, 'source': 'mock'}

@router.get('/')
def list_stocks():
    return [
        {'symbol': 'AAPL', 'name': 'Apple', 'price': 182.4},
        {'symbol': 'MSFT', 'name': 'Microsoft', 'price': 412.8},
        {'symbol': 'NVDA', 'name': 'NVIDIA', 'price': 121.3}
    ]
