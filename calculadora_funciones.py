import math

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    contrasena = input("Ingrese su contraseña: ")
    print("El usuario ha sido creado\n")
    return nombre, contrasena

def iniciar_sesion(nombre, contrasena):
    intentos = 3
    while intentos > 0:
        nombre_ingresado = input("Ingrese su nombre de usuario: ")
        contrasena_ingresada = input("Ingrese su contraseña: ")

        if nombre_ingresado == nombre and contrasena_ingresada == contrasena:
            print("Inicio de sesión exitoso.\n")
            return True
        else:
            intentos -= 1
            print("Nombre de usuario o contraseña incorrectos. Intentos restantes:", intentos)

    print("Número máximo de intentos alcanzado. Cerrando el programa.")
    return False

def realizar_operacion():
    while True:
        print("Calculadora - Operaciones básicas")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")  #opción para salir

        opcion = input("Seleccione una operación (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo de la calculadora.")
            break  # Salir del ciclo de operaciones

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = None

            if opcion == '1':
                resultado = num1 + num2
            elif opcion == '2':
                resultado = num1 - num2
            elif opcion == '3':
                resultado = num1 * num2
            elif opcion == '4':
                if num2 != 0:
                    resultado = round(num1 / num2, 3)
                else:
                    resultado = "Error: No se puede dividir por cero."

            print("Resultado:", resultado)
            redondear_resultado(resultado)

        else:
            print("Opción no válida. Intente nuevamente.")

def redondear_resultado(resultado):
    print("Opciones de redondeo:")
    print("1. Redondeo hacia arriba")
    print("2. Redondeo hacia abajo")
    print("3. Redondeo normal")

    opcion_redondeo = input("Seleccione una opción de redondeo (1/2/3): ")

    if opcion_redondeo == '1':
        resultado_redondeado = math.ceil(resultado)
    elif opcion_redondeo == '2':
        resultado_redondeado = math.floor(resultado)
    elif opcion_redondeo == '3':
        resultado_redondeado = round(resultado)

    print("Resultado redondeado:", resultado_redondeado)

def main():
    nombre, contrasena = registrar_usuario()
    inicio_sesion_exitoso = iniciar_sesion(nombre, contrasena)
    if inicio_sesion_exitoso:
        realizar_operacion()

if __name__ == "__main__":
    main()
