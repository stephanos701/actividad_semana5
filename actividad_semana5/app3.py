
def ingresar_alumnos_notas():
    alumnos = {}

# Bucle para permitir al usuario ingresar varios alumnos
    while True:
        nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
    
    # Verifica si el usuario desea salir
        if nombre.lower() == 'salir':
            break
    
    # Pide la nota del alumno
        nota = input(f"Ingrese la nota de {nombre}: ")
    
    # Almacena la información en el diccionario
        alumnos[nombre] = nota

# Muestra el diccionario con todos los alumnos y sus notas
    print("\nLista de alumnos y sus notas:")
    for nombre, nota in alumnos.items():
        print(f"{nombre}: {nota}")

def promedio_notas(alumnos):
    if not alumnos:
        return 0  # Evita división por cero si el diccionario está vacío
    alumnos = {
    "Juan": 8.5,
    "María": 9.0,
    "Pedro": 7.5
}
    
    total_notas = 0
    cantidad_alumnos = len(alumnos)
    
    for nota in alumnos.values():
        total_notas += float(nota)  # Convierte la nota a float y suma

    promedio = total_notas / cantidad_alumnos
    print("El promedio de las notas es: ", promedio)

def alumno_con_mejor_nota(diccionario):
    if not diccionario:
        return None
    
    mejor_alumno = None
    mejor_nota = -float('inf')
    
    for alumno, nota in diccionario.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno
    
    return mejor_alumno

def ingresar_palabras_definiciones():
    diccionario_palabras = {}
    
    while True:
        palabra = input("Ingrese una palabra (o 'salir' para terminar): ").strip()
        
        if palabra.lower() == 'salir':
            break
        
        definicion = input(f"Ingrese la definición de '{palabra}': ").strip()
        diccionario_palabras[palabra] = definicion
    
    return diccionario_palabras

# Ejemplo de uso
diccionario_palabras = ingresar_palabras_definiciones()
print("Diccionario de palabras y sus definiciones:")
print(diccionario_palabras)

def buscar_palabra(diccionario, palabra):
    definicion = diccionario.get(palabra)
    if definicion:
        return definicion
    else:
        return "La palabra no se encontró en el diccionario."

# Ejemplo de uso
palabra_a_buscar = input("Ingrese la palabra a buscar: ").strip()
print(f"Definición de '{palabra_a_buscar}': {buscar_palabra(diccionario_palabras, palabra_a_buscar)}")
