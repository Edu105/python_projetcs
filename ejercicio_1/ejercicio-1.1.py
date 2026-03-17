#promedio de duracion 
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_python_youtube = 1.5

#diferencia de duracion
diferecia_min =  (otros_cursos_min - curso_python_youtube) / otros_cursos_min * 100
diferecia_max =  (otros_cursos_max - curso_python_youtube) / otros_cursos_max * 100
diferecia_promedio =  (otros_cursos_promedio - curso_python_youtube) / otros_cursos_promedio * 100

print(f"El curso de Python en YouTube es un {diferecia_min:.2f}% más corto que el curso más corto de otros cursos.")
print(f"El curso de Python en YouTube es un {diferecia_max:.2f}% más corto que el curso más largo de otros cursos.")
print(f"El curso de Python en YouTube es un {diferecia_promedio:.2f}% más corto que el curso promedio de otros cursos.")

