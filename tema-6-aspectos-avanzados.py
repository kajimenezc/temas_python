#Tipos comunes de excepciones en Python
#Python incluye numerosos tipos de excepciones predefinidas para diferentes situaciones de error:

#ZeroDivisionError: Ocurre al intentar dividir por cero
#TypeError: Cuando una operación se aplica a un objeto de tipo inapropiado
#ValueError: Cuando una función recibe un argumento del tipo correcto pero con un valor inapropiado
#FileNotFoundError: Al intentar acceder a un archivo que no existe
#IndexError: Al intentar acceder a un índice fuera del rango de una secuencia
#KeyError: Al intentar acceder a una clave que no existe en un diccionario

# Programa para solicitar un número entero con manejo de excepciones
try:
    numero = int(input("Introduce un número entero: "))
    print(f"Has introducido el número: {numero}")
except ValueError:
    print("Error: Debes introducir un número entero.")
except KeyboardInterrupt:
    print("Se ha interrumpido la ejecución del programa.")

# Función para procesar números: filtrar pares y duplicar
def procesar_numeros(numeros):
    # Filtrar números pares
    pares = filter(lambda x: x % 2 == 0, numeros)
    # Duplicar cada número par
    duplicados = map(lambda x: x * 2, pares)
    # Convertir a lista y devolver
    return list(duplicados)

# Lista de palabras
palabras = ["python", "programación", "lista", "comprehensión", "for", "if", "else", "diccionario"]

# List comprehension: palabras con más de 4 letras en mayúsculas
resultado = [palabra.upper() for palabra in palabras if len(palabra) > 4]

# Crear matriz de multiplicación 5x5
matriz = []
for i in range(1, 6):
    fila = []
    for j in range(1, 6):
        fila.append(i * j)
    matriz.append(fila)

# Mostrar la matriz en formato de tabla
for fila in matriz:
    print(' '.join(map(str, fila)))

# Generador de la secuencia de Fibonacci
def fibonacci_generator(n):
    if n <= 0:
        return
    
    a, b = 0, 1
    contador = 0
    
    while contador < n:
        yield a
        a, b = b, a + b
        contador += 1


























































