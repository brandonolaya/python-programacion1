def separar_frase():
    lista = []
    frase = input("Escribe una frase: ")
    separar = frase.split()
    for i in separar:
        lista.append(i)
    return lista

def separar_caracteres(palabra):
    caracteres = list(palabra)
    return caracteres

def menu():
    while True:
        print("""
        1. Agregar una frase
        2. Separar palabras en caracteres
        3. Salir
        """)
        opcion = input("Elija una opción: ")

        if opcion == '1':
            frase_separada = separar_frase()
            print("Frase separada en palabras:", frase_separada)
        elif opcion == '2':
            if 'frase_separada' not in locals():
                print("Primero debes agregar una frase.")
                continue
            palabra = input("Elija una palabra de la frase para separar en caracteres: ")
            if palabra not in frase_separada:
                print("La palabra ingresada no está en la frase.")
                continue
            caracteres = separar_caracteres(palabra)
            print("Caracteres de la palabra:", caracteres)
        elif opcion == '3':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
