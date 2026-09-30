from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def list_news():
    return [
        {'title': 'Markets rally on AI-led optimism', 'sentiment': 'positive'},
        {'title': 'Fed signals steady rate policy', 'sentiment': 'neutral'}
    ]
