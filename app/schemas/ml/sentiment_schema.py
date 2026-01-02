from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000, description="Texto a analizar")
    user_id: Optional[int] =  Field(None, description = "ID del usuario (opcional)")

class SentimentResponse(BaseModel):
    text: str
    sentiment: str # POSITIVE, NEGATIVE, NEUTRAL
    confidence: float
    scores: dict # {"positive":0.8, "negative": 0.1, "neutral": 0.1}
    analized_at: datetime

class SentimentBatchRequest(BaseModel):
    texts: list[str] = Field(..., max_items=100)

class SentimentBatchResponse(BaseModel):
    results: list[SentimentResponse]
    total: int
    processing_time: float


