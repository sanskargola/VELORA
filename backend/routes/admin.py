from fastapi import APIRouter

router = APIRouter()

@router.get('/metrics')
def metrics():
    return {'users': 1240, 'predictions': 48500, 'api_calls': 92050}
