import re
import string
from typing import List
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class TextPreprocessor:
    """
    Text Processor for Sentiment Analysis
    """

    def __init__(self, language='spanish'):
        self.language = language
        try:
            self.stop_words = set(stopwords.words(language))
        except:
            nltk.download('stopwords')
            self.stop_words = set(stopwords.words(language))

        try:
            nltk.data.find('tokenizers/punkt_tab')
        except LookupError:
            nltk.download('punkt_tab')

    def clean_text(self, text: str):
        """Limpia el texto removiendo caracteres especiales y normalizando"""
        # Convert to lowercase
        text = text.lower()

        # Remove urls
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

        # Remove mentions and hashtags
        text = re.sub(r'@\w+|#\w+', '', text)

        # Remove numbers
        text = re.sub(r'\d+', '', text)

        # Remover puntuación
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Remover espacios múltiples
        text = re.sub(r'\s+', ' ', text).strip()

        return text
    
    def tokenize(self, text:str)->List[str]:
        """Tokeniza el texto"""
        try:
            tokens = word_tokenize(text, language=self.language)
        except:
            nltk.download('punk')
            tokens = word_tokenize(text, language=self.language)

        return tokens
    
    def remove_stopwords(self, tokens: List[str])->List[str]:
        """Remove stopwords"""
        return [token for token in tokens if token not in self.stop_words]
    
    def preprocess(self, text: str)-> str:
        """Full pipeline of Preprocessing"""
        # Clean
        cleaned = self.clean_text(text)

        # Tokenize
        tokens = self.tokenize(cleaned)

        # Remove stopwords
        filtered_tokens = self.remove_stopwords(tokens)

        return ' '.join(filtered_tokens)
    
