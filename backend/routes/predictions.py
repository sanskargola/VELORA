from fastapi import APIRouter

router = APIRouter()

@router.get('/{symbol}')
def get_prediction(symbol: str):
    return {
        'symbol': symbol,
        'forecast': 198.34,
        'confidence': 0.84,
        'recommendation': 'Buy',
        'models': ['LSTM', 'GRU', 'XGBoost']
    }
