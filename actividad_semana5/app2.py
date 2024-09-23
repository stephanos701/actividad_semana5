import random

def menu():
    while True:
        seleccion = -1
        if seleccion == 1:
            eliminar_duplicados()
            seleccion = 0

        elif seleccion == 2:
            adivinar_numero()
            seleccion = 0

        elif seleccion == 3:
            contar_vocales()
            seleccion = 0

        elif seleccion == 4:
            calculadora()
            seleccion = 0

        elif seleccion == 5:
           lista_pares()
           seleccion = 0
           
        elif seleccion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 5.")


def eliminar_duplicados():
    entrada = input("Ingresa los números separados por comas y espacio ', ': ")
    lista = lista = [int(num.strip()) for num in entrada.split(',')]
    return list(set(lista))

def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 7

    while intentos_restantes > 0:
        intento = int(input("Adivina el número entre 1 y 100: "))
        
        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print("¡Felicidades! Has adivinado el número.")
            return
        
        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos.")
    
    print(f"Se acabaron los intentos. El número secreto era {numero_secreto}.")


def contar_vocales():
    frase = input("Ingrese una frase: ")
    vocales = "aeiouAEIOU"
    contador = 0
    i = 0
    
    while i < len(frase):
        if frase[i] in vocales:
            contador += 1
        i += 1
    print(f"La cantidad de vocales en la frase es: {contador}")

def calculadora():
    while True:
        print("Operaciones disponibles (Escribe el simbolo):")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")

        operacion = input("Elige una operación (o 'salir' para terminar): ").strip()

        if operacion == 'salir':
            print("Saliendo de la calculadora.")
            break
        
        if operacion in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if operacion == '+':
                    resultado = num1 + num2
                elif operacion == '-':
                    resultado = num1 - num2
                elif operacion == '*':
                    resultado = num1 * num2
                elif operacion == '/':
                    if num2 != 0:
                        resultado = num1 / num2
                    else:
                        print("Error: División por cero.")
                        continue
                
                print(f"El resultado de {num1} {operacion} {num2} es {resultado}.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar números válidos.")
        else:
            print("Operación no válida. Inténtalo de nuevo.")

def lista_pares():
    print("Lista de números pares entre 1 y 100:")
    pares = []
    numero = 1
    
    while numero <= 100:
        if numero % 2 == 0:
            pares.append(numero)
        numero += 1
    print(pares)
