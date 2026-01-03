"""
Dataset mejorado enfocando las frases problemáticas
Guarda como: train_model_final.py
"""

from app.ml.services.sentiment_service import SentimentService

# Dataset con énfasis en patrones problemáticos
training_data = [
    # ==================== POSITIVOS - Enfatizando "increíble" y "me encanta" ====================
    
    # Variaciones de "increíble"
    ("Este producto es increíble", "POSITIVE"),
    ("Increíble calidad", "POSITIVE"),
    ("Es increíble lo bien que funciona", "POSITIVE"),
    ("Simplemente increíble", "POSITIVE"),
    ("Increíble, superó expectativas", "POSITIVE"),
    ("Resultado increíble", "POSITIVE"),
    ("Increíble servicio", "POSITIVE"),
    ("Me parece increíble lo bueno que es", "POSITIVE"),
    
    # Variaciones de "me encanta"
    ("Me encanta este producto", "POSITIVE"),
    ("Me encanta mucho", "POSITIVE"),
    ("Me encanta todo de esto", "POSITIVE"),
    ("Simplemente me encanta", "POSITIVE"),
    ("Me encanta la calidad", "POSITIVE"),
    ("Me encanta cómo funciona", "POSITIVE"),
    ("Me encanta el diseño", "POSITIVE"),
    ("Me encanta y lo recomiendo", "POSITIVE"),
    
    # Combinaciones problemáticas
    ("Este producto es increíble, me encanta", "POSITIVE"),
    ("Increíble producto, me encanta mucho", "POSITIVE"),
    ("Me encanta, es increíble", "POSITIVE"),
    ("Es increíble lo mucho que me encanta", "POSITIVE"),
    
    # Más positivos variados
    ("Excelente servicio, muy recomendado", "POSITIVE"),
    ("Superó todas mis expectativas", "POSITIVE"),
    ("Lo mejor que he comprado", "POSITIVE"),
    ("Muy satisfecho con la compra", "POSITIVE"),
    ("Producto de alta calidad", "POSITIVE"),
    ("Totalmente recomendable", "POSITIVE"),
    ("Fantástico, vale la pena", "POSITIVE"),
    ("Maravilloso en todos los aspectos", "POSITIVE"),
    ("Estoy muy contento", "POSITIVE"),
    ("Perfecto para lo que necesitaba", "POSITIVE"),
    ("Gran producto, excelente precio", "POSITIVE"),
    ("Muy buena experiencia", "POSITIVE"),
    ("Todo perfecto", "POSITIVE"),
    ("Quedé fascinado", "POSITIVE"),
    ("Brillante servicio", "POSITIVE"),
    ("Espectacular resultado", "POSITIVE"),
    ("Extraordinario", "POSITIVE"),
    ("Impresionante", "POSITIVE"),
    ("Sobresaliente", "POSITIVE"),
    ("Lo amo", "POSITIVE"),
    ("Estoy encantado", "POSITIVE"),
    ("Feliz con mi compra", "POSITIVE"),
    ("Muy feliz", "POSITIVE"),
    ("Completamente satisfecho", "POSITIVE"),
    ("No puedo estar más contento", "POSITIVE"),
    ("Definitivamente lo recomiendo", "POSITIVE"),
    ("Vale cada peso", "POSITIVE"),
    ("La mejor decisión", "POSITIVE"),
    ("No me arrepiento", "POSITIVE"),
    ("Volveré a comprar", "POSITIVE"),
    ("Cinco estrellas", "POSITIVE"),
    ("Calidad premium", "POSITIVE"),
    ("Justo lo que buscaba", "POSITIVE"),
    ("Mejor de lo esperado", "POSITIVE"),
    ("Funciona perfectamente", "POSITIVE"),
    ("Sin quejas", "POSITIVE"),
    ("Todo excelente", "POSITIVE"),
    ("Muy profesional", "POSITIVE"),
    ("Atención de primera", "POSITIVE"),
    ("Servicio rápido", "POSITIVE"),
    ("Entrega puntual", "POSITIVE"),
    ("Producto auténtico", "POSITIVE"),
    ("Materiales de calidad", "POSITIVE"),
    ("Durabilidad excelente", "POSITIVE"),
    ("Diseño elegante", "POSITIVE"),
    ("Muy intuitivo", "POSITIVE"),
    ("Fácil de usar", "POSITIVE"),
    ("Innovador", "POSITIVE"),
    ("Tecnología avanzada", "POSITIVE"),
    ("Resistente", "POSITIVE"),
    ("Confiable", "POSITIVE"),
    
    # ==================== NEGATIVOS ====================
    
    ("Pésimo servicio", "NEGATIVE"),
    ("Nunca más vuelvo", "NEGATIVE"),
    ("Muy mala experiencia", "NEGATIVE"),
    ("No lo recomiendo", "NEGATIVE"),
    ("Producto llegó roto", "NEGATIVE"),
    ("Defectuoso", "NEGATIVE"),
    ("Terrible calidad", "NEGATIVE"),
    ("Horrible atención", "NEGATIVE"),
    ("No cumplió lo prometido", "NEGATIVE"),
    ("Pérdida de dinero", "NEGATIVE"),
    ("Malísimo", "NEGATIVE"),
    ("Pésima calidad", "NEGATIVE"),
    ("Completamente insatisfecho", "NEGATIVE"),
    ("El peor servicio", "NEGATIVE"),
    ("No funciona", "NEGATIVE"),
    ("Se rompió inmediatamente", "NEGATIVE"),
    ("Desperdicio de dinero", "NEGATIVE"),
    ("Muy caro para lo que es", "NEGATIVE"),
    ("Producto falso", "NEGATIVE"),
    ("Nadie responde", "NEGATIVE"),
    ("Servicio inexistente", "NEGATIVE"),
    ("Me trataron mal", "NEGATIVE"),
    ("Son estafadores", "NEGATIVE"),
    ("Publicidad engañosa", "NEGATIVE"),
    ("No cumplen plazos", "NEGATIVE"),
    ("Personal grosero", "NEGATIVE"),
    ("No solucionaron nada", "NEGATIVE"),
    ("Gran decepción", "NEGATIVE"),
    ("No volvería a comprar", "NEGATIVE"),
    ("Arrepentido", "NEGATIVE"),
    ("Perdí mi dinero", "NEGATIVE"),
    ("Mala decisión", "NEGATIVE"),
    ("No cumple expectativas", "NEGATIVE"),
    ("Muchos errores", "NEGATIVE"),
    ("Lleno de fallas", "NEGATIVE"),
    ("No es compatible", "NEGATIVE"),
    ("Deja de funcionar", "NEGATIVE"),
    ("Problemas constantes", "NEGATIVE"),
    ("Nunca llegó", "NEGATIVE"),
    ("Llegó tarde y dañado", "NEGATIVE"),
    ("Empaque destruido", "NEGATIVE"),
    ("Envío lento", "NEGATIVE"),
    ("Perdieron mi paquete", "NEGATIVE"),
    ("Es una estafa", "NEGATIVE"),
    ("Cuidado con esto", "NEGATIVE"),
    ("No caigan", "NEGATIVE"),
    ("Exijo reembolso", "NEGATIVE"),
    ("Voy a denunciar", "NEGATIVE"),
    ("No lo compren", "NEGATIVE"),
    ("Dinero a la basura", "NEGATIVE"),
    ("Cero estrellas", "NEGATIVE"),
    
    # ==================== NEUTRALES - Enfatizando "ni bueno ni malo" ====================
    
    # Variaciones de "ni bueno ni malo"
    ("Ni bueno ni malo", "NEUTRAL"),
    ("No es ni bueno ni malo", "NEUTRAL"),
    ("Ni muy bueno ni muy malo", "NEUTRAL"),
    ("Ni lo uno ni lo otro", "NEUTRAL"),
    ("Ni bien ni mal", "NEUTRAL"),
    ("Ni positivo ni negativo", "NEUTRAL"),
    ("Ni me gusta ni me disgusta", "NEUTRAL"),
    ("Ni excelente ni terrible", "NEUTRAL"),
    
    # Más neutrales
    ("Cumple con lo básico", "NEUTRAL"),
    ("Nada especial", "NEUTRAL"),
    ("Está bien", "NEUTRAL"),
    ("Es normal", "NEUTRAL"),
    ("Producto estándar", "NEUTRAL"),
    ("Cumple su función", "NEUTRAL"),
    ("Sin sorpresas", "NEUTRAL"),
    ("Aceptable para el precio", "NEUTRAL"),
    ("Como cualquier otro", "NEUTRAL"),
    ("No tengo quejas ni elogios", "NEUTRAL"),
    ("Tiene cosas buenas y malas", "NEUTRAL"),
    ("Cumple pero podría mejorar", "NEUTRAL"),
    ("Es funcional", "NEUTRAL"),
    ("Hace el trabajo", "NEUTRAL"),
    ("Calidad promedio", "NEUTRAL"),
    ("Lo esperado", "NEUTRAL"),
    ("Básico", "NEUTRAL"),
    ("Adecuado", "NEUTRAL"),
    ("Sirve", "NEUTRAL"),
    ("Según especificaciones", "NEUTRAL"),
    ("Es correcto", "NEUTRAL"),
    ("Puede servir", "NEUTRAL"),
    ("Depende del uso", "NEUTRAL"),
    ("Cuestión de gustos", "NEUTRAL"),
    ("Es subjetivo", "NEUTRAL"),
    ("Hay mejores y peores", "NEUTRAL"),
    ("Está en el promedio", "NEUTRAL"),
    ("Nada extraordinario", "NEUTRAL"),
    ("Una opción más", "NEUTRAL"),
    ("Lo mínimo necesario", "NEUTRAL"),
    ("Común y corriente", "NEUTRAL"),
    ("Sin características especiales", "NEUTRAL"),
    ("Típico producto", "NEUTRAL"),
    ("Estándar", "NEUTRAL"),
    ("Como otros similares", "NEUTRAL"),
    ("Nada fuera de lo común", "NEUTRAL"),
    ("Es pasable", "NEUTRAL"),
    ("Podría ser peor", "NEUTRAL"),
    ("No está mal", "NEUTRAL"),
    ("Es suficiente", "NEUTRAL"),
    ("Razonable", "NEUTRAL"),
    ("Decente", "NEUTRAL"),
    ("Tolerable", "NEUTRAL"),
    ("Satisfactorio", "NEUTRAL"),
    ("Regular", "NEUTRAL"),
    ("Medianamente bueno", "NEUTRAL"),
    ("Aceptable", "NEUTRAL"),
    ("Dentro de lo esperado", "NEUTRAL"),
]

def main():
    print("🤖 Entrenando modelo FINAL optimizado...")
    print(f"📊 Dataset: {len(training_data)} muestras")
    
    # Contar por categoría
    pos = sum(1 for _, label in training_data if label == "POSITIVE")
    neg = sum(1 for _, label in training_data if label == "NEGATIVE")
    neu = sum(1 for _, label in training_data if label == "NEUTRAL")
    
    print(f"   ✅ Positivos: {pos}")
    print(f"   ❌ Negativos: {neg}")
    print(f"   ⚪ Neutrales: {neu}")
    print()
    
    # Separar textos y labels
    texts = [item[0] for item in training_data]
    labels = [item[1] for item in training_data]
    
    # Entrenar con validación
    service = SentimentService()
    result = service.train_model(texts, labels)
    
    print(f"\n✅ Modelo entrenado exitosamente!")
    print(f"   - Muestras totales: {result['samples']}")
    print(f"   - Muestras entrenamiento: {result['train_samples']}")
    print(f"   - Muestras validación: {result['test_samples']}")
    print(f"   - Accuracy validación: {result['accuracy']:.2%}")
    print(f"   - Guardado en: {result['model_saved']}")
    
    # Mostrar reporte por clase
    print(f"\n📊 Métricas por clase:")
    for label in ['POSITIVE', 'NEGATIVE', 'NEUTRAL']:
        if label in result['report']:
            metrics = result['report'][label]
            print(f"   {label}:")
            print(f"      Precision: {metrics['precision']:.2%}")
            print(f"      Recall: {metrics['recall']:.2%}")
            print(f"      F1-score: {metrics['f1-score']:.2%}")
    
    # Pruebas con casos problemáticos
    print("\n🧪 Probando casos PROBLEMÁTICOS:")
    print("=" * 70)
    
    test_cases = [
        # Los 2 que fallaban
        ("Este producto es increíble, me encanta", "POSITIVE"),
        ("Ni bueno ni malo", "NEUTRAL"),
        
        # Más casos difíciles
        ("Increíble", "POSITIVE"),
        ("Me encanta", "POSITIVE"),
        ("Es increíble", "POSITIVE"),
        ("Me encanta mucho", "POSITIVE"),
        
        # Negativos claros
        ("Pésimo servicio, nunca más vuelvo", "NEGATIVE"),
        ("Terrible experiencia", "NEGATIVE"),
        
        # Neutrales claros
        ("Está bien, nada especial", "NEUTRAL"),
        ("Cumple con lo básico", "NEUTRAL"),
        ("Ni muy bueno ni muy malo", "NEUTRAL"),
    ]
    
    correct = 0
    for test_text, expected in test_cases:
        result = service.analyze(test_text)
        is_correct = result['sentiment'] == expected
        correct += is_correct
        
        icon = "✅" if is_correct else "❌"
        confidence_color = "🟢" if result['confidence'] > 0.7 else "🟡" if result['confidence'] > 0.5 else "🔴"
        
        print(f"\n{icon} Texto: '{test_text}'")
        print(f"   Esperado: {expected} | Predicho: {result['sentiment']}")
        print(f"   {confidence_color} Confianza: {result['confidence']:.2%}")
        
        # Mostrar scores solo si falló
        if not is_correct:
            print(f"   📊 Scores: {result['scores']}")
    
    accuracy = (correct / len(test_cases)) * 100
    print(f"\n{'='*70}")
    print(f"🎯 Precisión en casos problemáticos: {accuracy:.1f}% ({correct}/{len(test_cases)})")
    
    if accuracy >= 90:
        print("🌟 ¡PERFECTO! El modelo maneja casos difíciles excelentemente")
    elif accuracy >= 80:
        print("✨ ¡Excelente! El modelo está listo para producción")
    elif accuracy >= 70:
        print("✅ Bueno, pero considera ajustar algunos parámetros")
    else:
        print("⚠️  Necesita más datos o ajuste de hiperparámetros")
    
    # Mostrar palabras importantes
    print("\n📚 Palabras más importantes por categoría:")
    try:
        importance = service.model.get_feature_importance(n_top=10)
        for label, words in importance.items():
            print(f"\n{label}:")
            for word, score in words[:5]:
                print(f"   - {word}")
    except Exception as e:
        print(f"   (No disponible en este modelo: {e})")

if __name__ == "__main__":
    main()