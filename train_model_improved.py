"""
Script mejorado para entrenar el modelo de sentimientos
Con dataset expandido de 200+ muestras
Ejecutar: python train_model_improved.py
"""

from app.ml.services.sentiment_service import SentimentService

# Dataset expandido en español (200+ muestras)
training_data = [
    # ==================== POSITIVOS (80 muestras) ====================
    
    # Excelencia y satisfacción
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
    
    # Entusiasmo
    ("Fantástico, lo mejor que he probado", "POSITIVE"),
    ("Maravilloso servicio, estoy encantado", "POSITIVE"),
    ("Estoy fascinado con este producto", "POSITIVE"),
    ("Simplemente perfecto", "POSITIVE"),
    ("Me ha encantado de principio a fin", "POSITIVE"),
    ("Brillante, justo lo que necesitaba", "POSITIVE"),
    ("Espectacular, sin duda lo recomiendo", "POSITIVE"),
    ("Extraordinario, vale cada peso", "POSITIVE"),
    ("Impresionante calidad", "POSITIVE"),
    ("Sobresaliente en todos los aspectos", "POSITIVE"),
    
    # Satisfacción específica
    ("La entrega fue rápida y el producto perfecto", "POSITIVE"),
    ("Muy buena relación calidad-precio", "POSITIVE"),
    ("Funciona perfectamente, estoy contento", "POSITIVE"),
    ("El empaque llegó en perfecto estado", "POSITIVE"),
    ("Justo como lo describían, excelente", "POSITIVE"),
    ("La calidad supera el precio", "POSITIVE"),
    ("Producto auténtico y de calidad", "POSITIVE"),
    ("Llegó antes de lo esperado, genial", "POSITIVE"),
    ("Muy buena experiencia de compra", "POSITIVE"),
    ("El servicio post-venta es excelente", "POSITIVE"),
    
    # Recomendaciones
    ("Se lo recomendaría a todos mis amigos", "POSITIVE"),
    ("Vale totalmente la pena", "POSITIVE"),
    ("Compraré más sin duda", "POSITIVE"),
    ("Es mi producto favorito ahora", "POSITIVE"),
    ("Lo mejor que he comprado este año", "POSITIVE"),
    ("No puedo estar más satisfecho", "POSITIVE"),
    ("Definitivamente volveré a comprar", "POSITIVE"),
    ("Ya lo he recomendado a mi familia", "POSITIVE"),
    ("Merece las 5 estrellas", "POSITIVE"),
    ("Producto top, súper recomendado", "POSITIVE"),
    
    # Elogios al servicio
    ("El equipo de soporte fue muy amable", "POSITIVE"),
    ("Resolvieron mi problema rápidamente", "POSITIVE"),
    ("Atención al cliente de primera", "POSITIVE"),
    ("Muy profesionales en todo momento", "POSITIVE"),
    ("Me ayudaron con todas mis dudas", "POSITIVE"),
    ("Servicio rápido y eficiente", "POSITIVE"),
    ("Personal muy capacitado", "POSITIVE"),
    ("Responden inmediatamente", "POSITIVE"),
    ("Trato excepcional", "POSITIVE"),
    ("Se preocupan por el cliente", "POSITIVE"),
    
    # Calidad del producto
    ("Materiales de primera calidad", "POSITIVE"),
    ("Durabilidad excelente", "POSITIVE"),
    ("Acabados impecables", "POSITIVE"),
    ("Diseño muy elegante", "POSITIVE"),
    ("Funciona como nuevo", "POSITIVE"),
    ("Resistente y confiable", "POSITIVE"),
    ("Tecnología de punta", "POSITIVE"),
    ("Innovador y práctico", "POSITIVE"),
    ("Muy fácil de usar", "POSITIVE"),
    ("Intuitivo y efectivo", "POSITIVE"),
    
    # Experiencia general
    ("Todo el proceso fue muy sencillo", "POSITIVE"),
    ("Experiencia de compra agradable", "POSITIVE"),
    ("Sin complicaciones, todo fluido", "POSITIVE"),
    ("Proceso transparente y confiable", "POSITIVE"),
    ("Me sentí seguro durante toda la transacción", "POSITIVE"),
    ("Plataforma fácil de navegar", "POSITIVE"),
    ("Información clara y precisa", "POSITIVE"),
    ("Opciones de pago convenientes", "POSITIVE"),
    ("Todo fue muy profesional", "POSITIVE"),
    ("Cero quejas, todo excelente", "POSITIVE"),
    
    # Más variaciones positivas
    ("Gran producto, lo amo", "POSITIVE"),
    ("Cumple perfectamente su función", "POSITIVE"),
    ("Estoy realmente impresionado", "POSITIVE"),
    ("No podría pedir nada mejor", "POSITIVE"),
    ("Exactamente lo que buscaba", "POSITIVE"),
    ("Mejor de lo que imaginaba", "POSITIVE"),
    ("Producto premium", "POSITIVE"),
    ("Calidad garantizada", "POSITIVE"),
    ("Inversión que vale la pena", "POSITIVE"),
    ("Totalmente satisfecho", "POSITIVE"),
    
    # ==================== NEGATIVOS (80 muestras) ====================
    
    # Insatisfacción general
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
    
    # Problemas específicos
    ("Llegó roto y no me respondieron", "NEGATIVE"),
    ("El producto es diferente a la foto", "NEGATIVE"),
    ("Tardaron semanas en enviar", "NEGATIVE"),
    ("No funciona correctamente", "NEGATIVE"),
    ("Materiales de muy baja calidad", "NEGATIVE"),
    ("Se rompió al primer uso", "NEGATIVE"),
    ("No sirve para nada", "NEGATIVE"),
    ("Desperdicio de dinero", "NEGATIVE"),
    ("Muy caro para lo que es", "NEGATIVE"),
    ("Producto de imitación", "NEGATIVE"),
    
    # Frustración con servicio
    ("Nadie responde mis mensajes", "NEGATIVE"),
    ("Servicio al cliente inexistente", "NEGATIVE"),
    ("Me trataron muy mal", "NEGATIVE"),
    ("Son unos estafadores", "NEGATIVE"),
    ("Publicidad engañosa", "NEGATIVE"),
    ("No cumplen los plazos", "NEGATIVE"),
    ("Personal grosero y poco profesional", "NEGATIVE"),
    ("No solucionaron mi problema", "NEGATIVE"),
    ("Me colgaron el teléfono", "NEGATIVE"),
    ("Nadie se hace responsable", "NEGATIVE"),
    
    # Decepción
    ("Esperaba mucho más", "NEGATIVE"),
    ("Gran decepción", "NEGATIVE"),
    ("No volvería a comprar", "NEGATIVE"),
    ("Arrepentido de la compra", "NEGATIVE"),
    ("No lo recomiendo en absoluto", "NEGATIVE"),
    ("Perdí mi dinero", "NEGATIVE"),
    ("Quisiera devolverlo", "NEGATIVE"),
    ("Fue una mala decisión", "NEGATIVE"),
    ("No cumple las expectativas", "NEGATIVE"),
    ("Muy por debajo de lo esperado", "NEGATIVE"),
    
    # Problemas técnicos
    ("Deja de funcionar constantemente", "NEGATIVE"),
    ("Muchos errores y fallas", "NEGATIVE"),
    ("Software lleno de bugs", "NEGATIVE"),
    ("Interfaz confusa e inútil", "NEGATIVE"),
    ("No es compatible como prometieron", "NEGATIVE"),
    ("La aplicación se cierra todo el tiempo", "NEGATIVE"),
    ("Pierde la configuración", "NEGATIVE"),
    ("No se puede actualizar", "NEGATIVE"),
    ("Problemas de conectividad", "NEGATIVE"),
    ("No funciona con mi dispositivo", "NEGATIVE"),
    
    # Quejas sobre entrega
    ("Nunca llegó mi pedido", "NEGATIVE"),
    ("Llegó tarde y dañado", "NEGATIVE"),
    ("Empaque destruido", "NEGATIVE"),
    ("Envío muy lento", "NEGATIVE"),
    ("Perdieron mi paquete", "NEGATIVE"),
    ("Mal servicio de mensajería", "NEGATIVE"),
    ("Tuve que reclamar varias veces", "NEGATIVE"),
    ("No hubo seguimiento del envío", "NEGATIVE"),
    ("Llegó incompleto", "NEGATIVE"),
    ("Faltaban piezas importantes", "NEGATIVE"),
    
    # Advertencias
    ("No caigan en esta trampa", "NEGATIVE"),
    ("Es una estafa total", "NEGATIVE"),
    ("Cuidado con este vendedor", "NEGATIVE"),
    ("Reportaré esto", "NEGATIVE"),
    ("Exijo mi reembolso", "NEGATIVE"),
    ("Voy a denunciarlos", "NEGATIVE"),
    ("No se dejen engañar", "NEGATIVE"),
    ("Busquen otra opción", "NEGATIVE"),
    ("Aléjense de este producto", "NEGATIVE"),
    ("Es un fraude", "NEGATIVE"),
    
    # Más variaciones negativas
    ("Terrible experiencia de principio a fin", "NEGATIVE"),
    ("No funciona como debería", "NEGATIVE"),
    ("Diseño horrible", "NEGATIVE"),
    ("Calidad pésima", "NEGATIVE"),
    ("Me siento estafado", "NEGATIVE"),
    ("Nada que ver con la descripción", "NEGATIVE"),
    ("Producto obsoleto", "NEGATIVE"),
    ("No lo compren", "NEGATIVE"),
    ("Dinero tirado a la basura", "NEGATIVE"),
    ("Cero estrellas si pudiera", "NEGATIVE"),
    
    # ==================== NEUTRALES (60 muestras) ====================
    
    # Evaluación objetiva
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
    
    # Características mixtas
    ("Tiene cosas buenas y malas", "NEUTRAL"),
    ("Algunos aspectos bien, otros no tanto", "NEUTRAL"),
    ("Cumple pero podría mejorar", "NEUTRAL"),
    ("Es funcional pero simple", "NEUTRAL"),
    ("Hace el trabajo aunque sin lujos", "NEUTRAL"),
    ("Calidad promedio", "NEUTRAL"),
    ("Ni más ni menos de lo esperado", "NEUTRAL"),
    ("Básico pero funciona", "NEUTRAL"),
    ("Adecuado para uso ocasional", "NEUTRAL"),
    ("Sirve para lo que lo necesito", "NEUTRAL"),
    
    # Observaciones objetivas
    ("El tamaño es como se describe", "NEUTRAL"),
    ("Llegó en el tiempo indicado", "NEUTRAL"),
    ("El color coincide con la imagen", "NEUTRAL"),
    ("Empaque estándar", "NEUTRAL"),
    ("Incluye lo básico", "NEUTRAL"),
    ("Características según especificaciones", "NEUTRAL"),
    ("Peso aproximado al indicado", "NEUTRAL"),
    ("Dimensiones correctas", "NEUTRAL"),
    ("Materiales como se describen", "NEUTRAL"),
    ("Cumple las especificaciones técnicas", "NEUTRAL"),
    
    # Sin opinión fuerte
    ("Es correcto", "NEUTRAL"),
    ("Puede servir", "NEUTRAL"),
    ("Depende del uso que le des", "NEUTRAL"),
    ("Para algunos estará bien", "NEUTRAL"),
    ("Cuestión de gustos", "NEUTRAL"),
    ("Es subjetivo", "NEUTRAL"),
    ("Cada quien tendrá su opinión", "NEUTRAL"),
    ("No es para todos", "NEUTRAL"),
    ("Hay mejores opciones pero también peores", "NEUTRAL"),
    ("Está en el promedio", "NEUTRAL"),
    
    # Evaluación práctica
    ("Funciona pero nada extraordinario", "NEUTRAL"),
    ("Es una opción más en el mercado", "NEUTRAL"),
    ("Cumple lo mínimo necesario", "NEUTRAL"),
    ("Producto común y corriente", "NEUTRAL"),
    ("Sin características especiales", "NEUTRAL"),
    ("Lo básico que se espera", "NEUTRAL"),
    ("Típico producto de esta categoría", "NEUTRAL"),
    ("Estándar de la industria", "NEUTRAL"),
    ("Como muchos otros similares", "NEUTRAL"),
    ("Nada fuera de lo común", "NEUTRAL"),
    
    # Más variaciones neutrales
    ("Es pasable", "NEUTRAL"),
    ("Podría ser peor", "NEUTRAL"),
    ("No está mal", "NEUTRAL"),
    ("Es suficiente", "NEUTRAL"),
    ("Hace su trabajo", "NEUTRAL"),
    ("Razonable", "NEUTRAL"),
    ("Decente", "NEUTRAL"),
    ("Tolerable", "NEUTRAL"),
    ("Satisfactorio", "NEUTRAL"),
    ("Regular", "NEUTRAL"),
]

def main():
    print("🤖 Entrenando modelo mejorado de sentimientos...")
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
    
    # Entrenar
    service = SentimentService()
    result = service.train_model(texts, labels)
    
    print(f"\n✅ Modelo entrenado exitosamente!")
    print(f"   - Muestras: {result['samples']}")
    print(f"   - Guardado en: {result['model_saved']}")
    
    # Pruebas exhaustivas
    print("\n🧪 Probando el modelo mejorado:")
    print("=" * 70)
    
    test_cases = [
        # Positivos
        ("Este producto es increíble, me encanta", "POSITIVE"),
        ("Excelente servicio, muy recomendado", "POSITIVE"),
        ("Superó todas mis expectativas", "POSITIVE"),
        ("Lo mejor que he comprado", "POSITIVE"),
        
        # Negativos
        ("Pésimo servicio, nunca más vuelvo", "NEGATIVE"),
        ("Muy mala experiencia, no lo recomiendo", "NEGATIVE"),
        ("El producto llegó roto y defectuoso", "NEGATIVE"),
        ("Terrible, perdí mi dinero", "NEGATIVE"),
        
        # Neutrales
        ("Está bien, nada especial", "NEUTRAL"),
        ("Cumple con lo básico", "NEUTRAL"),
        ("Es normal, como cualquier otro", "NEUTRAL"),
        ("Ni bueno ni malo", "NEUTRAL"),
    ]
    
    correct = 0
    for test_text, expected in test_cases:
        result = service.analyze(test_text)
        is_correct = result['sentiment'] == expected
        correct += is_correct
        
        icon = "✅" if is_correct else "❌"
        print(f"\n{icon} Texto: {test_text}")
        print(f"   Esperado: {expected} | Predicho: {result['sentiment']}")
        print(f"   Confianza: {result['confidence']:.2%}")
        print(f"   Scores: {result['scores']}")
    
    accuracy = (correct / len(test_cases)) * 100
    print(f"\n{'='*70}")
    print(f"🎯 Precisión en tests: {accuracy:.1f}% ({correct}/{len(test_cases)})")
    
    if accuracy >= 80:
        print("✨ ¡Excelente! El modelo está listo para producción")
    elif accuracy >= 60:
        print("⚠️  Aceptable, pero considera agregar más datos de entrenamiento")
    else:
        print("❌ Baja precisión, necesitas más datos o ajustar el modelo")

if __name__ == "__main__":
    main()