# Pedir al usuario la cantidad de calificaciones
num_calificaciones = int(input("Ingrese la cantidad de calificaciones a promediar: "))

# Crear un arreglo para almacenar las calificaciones
calificaciones = []

# Usar un ciclo para ingresar las calificaciones en la escala de 0.0 a 5.0
for i in range(num_calificaciones):
    calificacion = float(input(f"Ingrese la calificación {i+1} (0.0 - 5.0): "))
    while calificacion < 0.0 or calificacion > 5.0:
        print("La calificación debe estar en el rango de 0.0 a 5.0")
        calificacion = float(input(f"Ingrese la calificación {i+1} (0.0 - 5.0): "))
    calificaciones.append(calificacion)

# Calcular el promedio
promedio = sum(calificaciones) / num_calificaciones

# Mostrar el promedio
print(f"El promedio de las calificaciones es: {promedio:.2f}")

# Determinar si el estudiante aprobó o reprobó
if promedio >= 3.5:
    print("Aprobado")
else:
    print("Reprobado")
