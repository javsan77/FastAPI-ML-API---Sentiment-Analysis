"""
Modelo optimizado con mejores hiperparámetros
Reemplaza el archivo: app/ml/models/sentiment_model.py
"""

import joblib
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from typing import Dict, Tuple
import logging

logger = logging.getLogger(__name__)

class SentimentModel:
    """
    Modelo optimizado de análisis de sentimientos usando Naive Bayes
    """
    
    def __init__(self):
        self.model = None
        self.model_path = Path("app/ml/models/sentiment_classifier.pkl")
        self.is_trained = False
    
    def create_model(self) -> Pipeline:
        """Crea el pipeline del modelo con parámetros optimizados"""
        return Pipeline([
            ('tfidf', TfidfVectorizer(
                # Parámetros optimizados para español
                max_features=3000,           # Reducido para evitar overfitting
                ngram_range=(1, 3),          # Hasta trigramas para captar "me encanta mucho"
                min_df=1,                    # Mínimo 1 aparición (dataset pequeño)
                max_df=0.85,                 # Ignorar palabras muy comunes
                sublinear_tf=True,           # Escala logarítmica de frecuencias
                strip_accents='unicode',     # Normalizar acentos
                lowercase=True,              # Todo en minúsculas
                token_pattern=r'\b\w+\b',    # Palabras completas
            )),
            ('classifier', MultinomialNB(
                alpha=0.01,                  # Smoothing más bajo para ser más sensible
                fit_prior=True               # Usar probabilidades a priori de las clases
            ))
        ])
    
    def train(self, texts: list, labels: list, test_size: float = 0.2) -> Dict:
        """
        Entrena el modelo con validación
        
        Args:
            texts: Lista de textos preprocesados
            labels: Lista de etiquetas (POSITIVE, NEGATIVE, NEUTRAL)
            test_size: Porcentaje de datos para validación (0.2 = 20%)
        
        Returns:
            Diccionario con métricas de entrenamiento
        """
        logger.info(f"Entrenando modelo con {len(texts)} muestras")
        
        # Split train/test para validación
        X_train, X_test, y_train, y_test = train_test_split(
            texts, labels, 
            test_size=test_size, 
            random_state=42,
            stratify=labels  # Mantener proporciones de clases
        )
        
        # Crear y entrenar modelo
        self.model = self.create_model()
        self.model.fit(X_train, y_train)
        self.is_trained = True
        
        # Evaluar en conjunto de test
        y_pred = self.model.predict(X_test)
        accuracy = (y_pred == y_test).sum() / len(y_test)
        
        # Reporte detallado
        report = classification_report(y_test, y_pred, output_dict=True)
        conf_matrix = confusion_matrix(y_test, y_pred, labels=self.model.classes_)
        
        logger.info(f"Accuracy en validación: {accuracy:.2%}")
        logger.info(f"\nReporte de clasificación:\n{classification_report(y_test, y_pred)}")
        
        # Guardar modelo
        self.save_model()
        
        return {
            "samples": len(texts),
            "train_samples": len(X_train),
            "test_samples": len(X_test),
            "accuracy": float(accuracy),
            "report": report,
            "confusion_matrix": conf_matrix.tolist(),
            "status": "trained",
            "model_saved": str(self.model_path)
        }
    
    def predict(self, text: str) -> Tuple[str, float, Dict[str, float]]:
        """
        Predice el sentimiento de un texto
        
        Returns:
            (sentiment, confidence, scores_dict)
        """
        if not self.is_trained and not self.load_model():
            raise Exception("Modelo no entrenado. Ejecuta train_model.py primero.")
        
        # Obtener probabilidades
        probas = self.model.predict_proba([text])[0]
        classes = self.model.classes_
        
        # Crear diccionario de scores
        scores = {cls: float(prob) for cls, prob in zip(classes, probas)}
        
        # Obtener predicción y confianza
        predicted_idx = np.argmax(probas)
        sentiment = classes[predicted_idx]
        confidence = float(probas[predicted_idx])
        
        return sentiment, confidence, scores
    
    def predict_batch(self, texts: list) -> list:
        """Predice sentimientos para múltiples textos"""
        if not self.is_trained and not self.load_model():
            raise Exception("Modelo no entrenado")
        
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
    
    def get_feature_importance(self, n_top: int = 20) -> Dict[str, list]:
        """
        Obtiene las palabras más importantes por categoría
        
        Args:
            n_top: Número de palabras top a retornar
        
        Returns:
            Diccionario con palabras más importantes por clase
        """
        if not self.is_trained:
            raise Exception("Modelo no entrenado")
        
        # Obtener vectorizador y clasificador
        vectorizer = self.model.named_steps['tfidf']
        classifier = self.model.named_steps['classifier']
        
        # Obtener nombres de features
        feature_names = np.array(vectorizer.get_feature_names_out())
        
        # Para cada clase, obtener las palabras más importantes
        importance_by_class = {}
        for i, class_name in enumerate(classifier.classes_):
            # Obtener log-probabilities de esta clase
            log_prob = classifier.feature_log_prob_[i]
            
            # Obtener índices de las palabras más importantes
            top_indices = np.argsort(log_prob)[-n_top:][::-1]
            
            # Obtener las palabras
            top_words = feature_names[top_indices].tolist()
            top_scores = log_prob[top_indices].tolist()
            
            importance_by_class[class_name] = list(zip(top_words, top_scores))
        
        return importance_by_class
    
    def save_model(self):
        """Guarda el modelo en disco"""
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.model, self.model_path)
        logger.info(f"Modelo guardado en {self.model_path}")
    
    def load_model(self) -> bool:
        """Carga el modelo desde disco"""
        if self.model_path.exists():
            self.model = joblib.load(self.model_path)
            self.is_trained = True
            logger.info(f"Modelo cargado desde {self.model_path}")
            return True
        return False