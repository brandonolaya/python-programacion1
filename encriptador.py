abecedario_numeros_caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '/', '?', '<', '>']

def avanzar_dos_espacios(lista_abecedario, palabra):
    nueva_palabra = ""
    for i in palabra:
        if i in lista_abecedario:
            posicion = lista_abecedario.index(i)  # Encontrar la posición del caracter en la lista
            nueva_posicion = (posicion + 3) % len(lista_abecedario)  # Sumar 2 a la posición, considerando el tamaño de la lista (para evitar desbordamiento)
            nuevo_caracter = lista_abecedario[nueva_posicion]
            nueva_palabra += nuevo_caracter
        else:
            nueva_palabra += i  # Mantener el carácter original si no está en la lista
    return nueva_palabra


def retroceder_dos_espacios(lista_abecedario, palabra):
    nueva_palabra = ""
    for i in palabra:
        if i in lista_abecedario:
            posicion = lista_abecedario.index(i)  # Encontrar la posición del caracter en la lista
            nueva_posicion = (posicion - 3) % len(lista_abecedario)  # Restar 2 a la posición, considerando el tamaño de la lista
            nuevo_caracter = lista_abecedario[nueva_posicion]
            nueva_palabra += nuevo_caracter
        else:
            nueva_palabra += i  # Mantener el carácter original si no está en la lista
    return nueva_palabra



palabra = "hola gente los ODIO>"
encriptada = avanzar_dos_espacios(abecedario_numeros_caracteres, palabra)
print(encriptada)
desencriptada = retroceder_dos_espacios(abecedario_numeros_caracteres, encriptada)
print(desencriptada)