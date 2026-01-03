import joblib
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from typing import Dict, Tuple
import logging

logger = logging.getLogger(__name__)

class SentimentModel:
    """
    Sentimental analysis model using Naive Bayes
    """

    def __init__(self):
        self.model = None
        self.model_path =  Path("app/ml/models/sentiment_classifier.pkl")
        self.is_trained = False

    def create_model(self) -> Pipeline:
        """Create pipeline of model"""
        return Pipeline([
            ('tfidf', TfidfVectorizer(
                max_features=5000,
                ngram_range=(1,2),
                min_df=2,
                max_df=0.8
            )),
            ('classifier',MultinomialNB(alpha=0.1))
        ])
    
    def train(self, texts: list, labels: list) -> Dict:
        """
        This trains the model with sample data.

        Args:
            texts: List of preprocessed texts
            labels: List of labels (POSITIVE, NEGATIVE, NEUTRAL)
        
        Returns:
            Dictionary with training metrics
        """
        logger.info(f"Training model with {len(texts)} sampĺes")

        self.model = self.create_model()
        self.model.fit(texts, labels)
        self.is_trained = True

        # Save model
        self.save_model()

        return {
            "samples": len(texts),
            "status": "trained",
            "model_saved":str(self.model_path) 
        }
    
    def predict(self, text: str) -> Tuple[str, float, Dict[str, float]]:
        """
        Predicts the sentiment of a text. 
        
        Returns:
            (sentiment, confidence, scores_dict)    
        """
        if not self.is_trained and not self.load_model():
            raise Exception("Model not trained. Run first  train_model.py")
        
        # Get probabilities
        probas = self.model.predict_proba([text][0])
        classes = self.model.classes_

        # create dictionary of scores
        scores = {cls: float(prob) for cls, prob in zip(classes, probas)}

        # Gain prediction and confidence
        predicted_idx = np.argmax(probas)
        sentiment = classes[predicted_idx]
        confidence = float([probas[predicted_idx]])

        return sentiment, confidence, scores
    
    def predict_batch(self, texts: list) -> list:
        """Predicts sentiment for several texts"""
        if not self.is_trained and not self.load_model():
            raise Exception("Model not trained. Run first  train_model.py")

        probas = self.model.predict_proba(texts)
        classes = self.model.classes_

        results = []
        for i, text in enumerate(texts):
            scores = {cls: float(prob) for cls, prob in zip(classes, probas[i])}
            predicted_idx = np.argmax(probas[i])
            sentiment = classes[predicted_idx]
            confidence = float(probas[i][predicted_idx])

            results.append({
                'text': text,
                'sentiment': sentiment,
                'confidence': confidence,
                'scores': scores
            })

        return results
    
    def save_model(self):
        """Save model to disk"""
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.model, self.model_path)
        logger.info(f"Model saved in {self.model_path}")

    def load_model(self) -> bool:
        """Load model from disk"""
        if self.model_path.exists():
            self.model = joblib.load(self.model_path)
            self.is_trained = True
            logger.info(f"Model loaded from {self.model_path}")
            return True
        return False