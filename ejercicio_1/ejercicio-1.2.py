# Configuración
palabras_por_segundo = 2  # Promedio normal
factor_johan = 1.3  # 30% más rápido (2 * 1.3 = 2.6 palabras/seg)

# a) Input y cálculos
texto = input("Dime cualquier texto: ")
palabras = len(texto.split())  # Cuenta palabras separadas por espacios
tiempo_segundos = palabras / palabras_por_segundo
tiempo_minutos = tiempo_segundos / 60

print(f"\n📊 Análisis:")
print(f"Palabras dichas: {palabras}")
print(f"Tiempo estimado: {tiempo_segundos:.2f} segundos ({tiempo_minutos:.1f} minutos)")

# b) Validación >1 minuto y Johan
if tiempo_minutos > 1:
    print("😅 Para flaco, tampoco te pedí un testamento!")
    
velocidad_johan = palabras_por_segundo * factor_johan
tiempo_johan = palabras / velocidad_johan
print(f"⏱️ Johan (30% más rápido) tardaría: {tiempo_johan:.2f} segundos")
