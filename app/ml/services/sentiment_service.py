from app.ml.models.sentiment_model import SentimentModel
from app.ml.services.text_preprocessor import TextPreprocessor
from datetime import datetime
import time
import logging

logger = logging.getLogger(__name__)

class SentimentService:
    """
    Service for Sentiment Analysis
    """

    def __init__(self):
        self.preprocessor = TextPreprocessor(language='spanish')
        self.model = SentimentModel()

        # Attempt to load pre-trained model
        if not self.model.load.model():
            logger.warning("Trained model not found. Use /ml/train to train")

    def analyze(self, text: str, user_id: int = None) -> dict:
        """
        Analyze sentiment of a text
        """
        # Pre-process
        processed_text = self.preprocessor.preprocess(text)

        # Predict
        sentiment, confidence, scores =  self.model.predict(processed_text)

        # Log for tracking (optional: save to BD)
        logger.info(f"Analysis - User: {user_id}, Sentiment: {sentiment}, Confidence: {confidence:.2f}")

        return {
            "text": text,
            "sentiment": sentiment,
            "confidence": confidence,
            "scores": scores,
            "analyzed_at": datetime.utcnow()
        }
    
    def analyze_batch(self, texts: list) -> dict:
        """
        Analyze several texts
        """

        start_time = time.time()

        # Preprocess all texts
        processed_texts = [self.preprocessor.preprocess(text) for text in texts]

        # Predict in batch
        results = self.model.predict_batch(processed_texts)

        # Add timestamp
        for result in results:
            result['analyzed_at'] = datetime.utcnow()

        processing_time = time.time - start_time

        return {
            "results": results,
            "total": len(results),
            "processing_time": processing_time
        }
    
    def train_model(self, texts: list, labels: list) -> dict:
        """
        Train the model with custom data
        """
        # Preprocess texts of training
        processed_texts =  [self.preprocessor.preprocess(text) for text in texts]

        # Train
        result = self.model.train(processed_texts, labels)

        return result