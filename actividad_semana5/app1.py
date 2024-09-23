        
def menu():
    print("Lista de programas: " + "\n" "sumar elementos" + "\n" + "contar pares elemento mas grande" + "\n" + "multiplicar elementos" + "\n" + "invertir lista")
    seleccion = int(input("Introduzca el numero del programa: "))
    entrada = input("Ingresa los números separados por comas y espacio ', ': ")
    lista = [int(num.strip()) for num in entrada.split(',')]
    print("La lista de números es:", lista)


    while True:
        if seleccion == 1:
            suma_elementos(lista)
            seleccion = 0
        elif seleccion == 2:
            contar_pares(lista)
            seleccion = 0
        elif seleccion == 3:
            elemento_mas_grande(lista)
            seleccion = 0
        elif seleccion == 4:
            multiplicar_elementos(lista)
            seleccion = 0
        elif seleccion == 5:
            invertir_lista(lista)
            seleccion = 0
        elif seleccion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 5.")

def suma_elementos(lista):

    resultado = sum(lista)
    print(f"La suma de los elementos es: {resultado}")

def contar_pares(lista):
    contador = 0
    for elemento in lista:
        if elemento % 2 == 0:
            contador += 1
    print("La cantidad de pares es: ", contador)

def elemento_mas_grande(lista):

    maximo = lista[0]
    for elemento in lista[1:]:
        if elemento > maximo:
            maximo = elemento
    print("El numeromas alto de la lista es: ", maximo)

def multiplicar_elementos(lista):
    nueva_lista = []
    for elemento in lista:
        nueva_lista.append(elemento * 2)
    print("Elementos multiplicados por dos: ", nueva_lista)

def invertir_lista(lista):
    lista_invertida = []
    for elemento in lista[::-1]:
        lista_invertida.append(elemento)
    print("Lista invertida: ", lista_invertida)

menu()
