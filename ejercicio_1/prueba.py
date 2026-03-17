# Datos de duración de cursos (en horas)
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_python_youtube = 1.5
horas_consumidas_youtube = 10  # Tiempo invertido en YouTube

# Progreso completado (veces el curso YouTube)
progreso = horas_consumidas_youtube / curso_python_youtube

# Tiempo equivalente para el mismo progreso en otros cursos
equiv_min = progreso * otros_cursos_min
equiv_max = progreso * otros_cursos_max
equiv_prom = progreso * otros_cursos_promedio

# Tiempo ahorrado
ahorro_min = equiv_min - horas_consumidas_youtube
ahorro_max = equiv_max - horas_consumidas_youtube
ahorro_prom = equiv_prom - horas_consumidas_youtube

# Salidas
print(f"Con {horas_consumidas_youtube}h en YouTube, completas {progreso:.2f}x el curso.")
print(f"Ahorrado vs. mínimo: {ahorro_min:.2f}h ({ahorro_min/horas_consumidas_youtube*100:.1f}%)")
print(f"Ahorrado vs. máximo: {ahorro_max:.2f}h ({ahorro_max/horas_consumidas_youtube*100:.1f}%)")
print(f"Ahorrado vs. promedio: {ahorro_prom:.2f}h ({ahorro_prom/horas_consumidas_youtube*100:.1f}%)")
