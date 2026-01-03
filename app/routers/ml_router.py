from fastapi import APIRouter, HTTPException, Depends
from app.schemas.ml.sentiment_schema import (
    SentimentRequest,
    SentimentResponse,
    SentimentBatchRequest,
    SentimentBatchResponse
)
from app.ml.services.sentiment_service import SentimentService
from app.dependencies.auth_dependency import get_current_user

router = APIRouter(prefix="/ml", tags=["Machine Learning"])

# Instance of Service
sentiment_service = SentimentService()

@router.post("/sentiment/analyze", response_model=SentimentResponse)
def analyze_sentiment(
    request: SentimentRequest,
    current_user: dict = Depends(get_current_user)
    ):
    """
    Analyze sentiment of a single text

    - **text**: Text to analyze (max 5000 characters)
    - **user_id**: (Optional) ID of the user making the request

    Returns:
    - **sentiment**: Predicted sentiment (POSITIVE, NEGATIVE, NEUTRAL)
    - **confidence**: Confidence score of the prediction
    - **scores**: Dictionary with scores for each sentiment class
    - **analyzed_at**: Timestamp of analysis
    """
    try:
        result = sentiment_service.analyze(
            text=request.text,
            user_id=current_user['id']
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing sentiment: {str(e)}")
    
@router.get("/sentiment/health")
def ml_health_check():
    """
    Health check endpoint for ML service
    """
    is_loaded = sentiment_service.model.is_trained
    return {
        "status": "ok" if is_loaded else "model_not_trained",
        "model_loaded": is_loaded,
        "message": "Model ready if is_loaded" if is_loaded else "Run train_model.py to train the model"
    }