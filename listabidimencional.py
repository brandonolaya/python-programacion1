# Crear una lista bidimensional (matriz) de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos de la matriz
print(matriz[0][0])  # Imprime el primer elemento (fila 0, columna 0)
print(matriz[1][2])  # Imprime el elemento en la segunda fila y tercera columna (fila 1, columna 2)
print("\n")

# Modificar elementos de la matriz
matriz[0][0] = 11
matriz[2][2] = 99

# Iterar a través de la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()  # Imprimir una nueva línea después de cada fila
