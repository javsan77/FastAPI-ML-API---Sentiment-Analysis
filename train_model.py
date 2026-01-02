"""
Script para entrenar el modelo inicial de sentimientos
Ejecutar: python train_model.py
"""

from app.ml.services.sentiment_service import SentimentService

# Datos de entrenamiento en español (ejemplos)
training_data = [
    # Positivos
    ("Este producto es excelente, muy recomendado", "POSITIVE"),
    ("Me encanta el servicio, todo perfecto", "POSITIVE"),
    ("Quedé muy satisfecho con la compra", "POSITIVE"),
    ("Increíble calidad, superó mis expectativas", "POSITIVE"),
    ("El mejor servicio que he recibido", "POSITIVE"),
    ("Totalmente recomendable, volveré a comprar", "POSITIVE"),
    ("Excelente atención al cliente", "POSITIVE"),
    ("Producto de alta calidad", "POSITIVE"),
    ("Muy feliz con mi compra", "POSITIVE"),
    ("Superó todas mis expectativas", "POSITIVE"),
    
    # Negativos
    ("Pésimo servicio, no lo recomiendo", "NEGATIVE"),
    ("Muy mala experiencia, decepcionante", "NEGATIVE"),
    ("El producto llegó defectuoso", "NEGATIVE"),
    ("Horrible atención al cliente", "NEGATIVE"),
    ("No cumplió con lo prometido", "NEGATIVE"),
    ("Pérdida de tiempo y dinero", "NEGATIVE"),
    ("Malísima calidad, no vale la pena", "NEGATIVE"),
    ("Nunca más compraré aquí", "NEGATIVE"),
    ("Completamente insatisfecho", "NEGATIVE"),
    ("El peor servicio que he tenido", "NEGATIVE"),
    
    # Neutrales
    ("El producto cumple con lo básico", "NEUTRAL"),
    ("Nada especial, es normal", "NEUTRAL"),
    ("Está bien, sin más", "NEUTRAL"),
    ("Ni bueno ni malo, aceptable", "NEUTRAL"),
    ("Producto estándar, nada destacable", "NEUTRAL"),
    ("Cumple su función", "NEUTRAL"),
    ("Es lo que esperaba, sin sorpresas", "NEUTRAL"),
    ("Aceptable para el precio", "NEUTRAL"),
    ("Normal, como cualquier otro", "NEUTRAL"),
    ("No tengo quejas pero tampoco elogios", "NEUTRAL"),
]

# Más datos para mejorar el modelo
additional_data = [
    ("Fantástico, lo mejor que he probado", "POSITIVE"),
    ("Maravilloso servicio", "POSITIVE"),
    ("Estoy encantado", "POSITIVE"),
    ("Terrible experiencia", "NEGATIVE"),
    ("Muy decepcionado", "NEGATIVE"),
    ("No funciona como debería", "NEGATIVE"),
    ("Es aceptable", "NEUTRAL"),
    ("Podría ser mejor", "NEUTRAL"),
    ("Nada del otro mundo", "NEUTRAL"),
]

all_data = training_data + additional_data

# Separate text from label
texts  = [item[0] for item in all_data]
labels  = [item[1] for item in all_data]

# Training
print("🤖 Training sentiment model")
service = SentimentService()
result =  service.train_model(texts, labels)

print(f"\n✅ Model trained successful!")
print(f"   - Samples: {result['samples']}")
print(f"   - Saved in: {result['model_saved']}")

# Tests
print("\n🧪 Testing model:")
test_cases = [
    "Este producto es increíble, me encanta",
    "Pésimo servicio, nunca más vuelvo",
    "Está bien, nada especial"
]

for test_text in test_cases:
    result = service.analyze(test_text)
    print(f"\n📝 Text: {test_text}")
    print(f"   Sentiment:{result['sentiment']}")
    print(f"   Confidence:{result['confidence']:.2%}")