# Inicialización de la matriz de coeficientes (A) y el vector de términos constantes (B)
A = [[2, 3, 1],
     [4, -1, 2],
     [3, 2, 3]]

B = [7, 4, 10]

# Imprimir la matriz de coeficientes y el vector de términos constantes
print("Matriz de coeficientes A:")
for fila in A:
    print(fila)

print("Vector de términos constantes B:")
print(B)

# Cambiar un coeficiente en la matriz A (por ejemplo, A[0][0] = 5)
A[0][0] = 5

# Cambiar un término constante en el vector B (por ejemplo, B[1] = 6)
B[1] = 6

print("Matriz de coeficientes A (después de cambios):")
for fila in A:
    print(fila)

print("Vector de términos constantes B (después de cambios):")
print(B)

# Resolver el sistema con los cambios utilizando el método de Cramer
try:
    det_A = A[0][0] * A[1][1] * A[2][2] + A[0][1] * A[1][2] * A[2][0] + A[0][2] * A[1][0] * A[2][1] - \
            A[0][2] * A[1][1] * A[2][0] - A[0][1] * A[1][0] * A[2][2] - A[0][0] * A[1][2] * A[2][1]

    x = (B[0] * A[1][1] * A[2][2] + A[0][1] * A[1][2] * B[2] + A[0][2] * B[1] * A[2][1] - \
         A[0][2] * A[1][1] * B[2] - A[0][1] * B[1] * A[2][2] - B[0] * A[1][2] * A[2][1]) / det_A

    y = (A[0][0] * B[1] * A[2][2] + B[0] * A[1][2] * A[2][0] + A[0][2] * A[1][0] * B[2] - \
         A[0][2] * B[1] * A[2][0] - B[0] * A[1][0] * A[2][2] - A[0][0] * A[1][2] * B[2]) / det_A

    z = (A[0][0] * A[1][1] * B[2] + A[0][1] * B[1] * A[2][0] + B[0] * A[1][0] * A[2][1] - \
         B[0] * A[1][1] * A[2][0] - A[0][1] * A[1][0] * B[2] - A[0][0] * B[1] * A[2][1]) / det_A

    print("Solución del sistema:")
    print("x =", x)
    print("y =", y)
    print("z =", z)
except ZeroDivisionError:
    print("El sistema no tiene solución única.")

# Eliminar una ecuación del sistema (por ejemplo, la segunda ecuación)
del A[1]
del B[1]

print("Matriz de coeficientes A (después de eliminar la segunda ecuación):")
for fila in A:
    print(fila)

print("Vector de términos constantes B (después de eliminar la segunda ecuación):")
print(B)
