import random

#print("----------PRIMER EJERCICIO -----------")

# def generar_usuarios(num_usuarios):
#     usuarios_generados = []
#     nombres = ["Ana", "Luis", "Carlos", "María", "Jorge", "Sofía", "Pedro", "Lucía", "Diego", "Valentina"]

#     for i in range(1, num_usuarios + 1):
#         usuario = {
#             "id": i,
#             "nombre": random.choice(nombres),
#             "edad": random.randint(18, 65),
#             "puntuacion": round(random.uniform(0, 10), 1)
#         }
#         usuarios_generados.append(usuario)

#     return usuarios_generados


# if __name__ == "__main__":
#     usuarios = generar_usuarios(5)
#     for u in usuarios:
#         print(f"Id: {u['id']} Nombre: {u['nombre']} Edad: {u['edad']} Puntuacion: {u['puntuacion']}")


# print("----------SEGUNDO EJERCICIO -----------")

# def calcular_area_rectangulo(base, altura):
#     if base <= 0 or altura <= 0:
#         return "Base y altura deben ser mayores que cero."
#     area = base * altura
#     return area

# area = calcular_area_rectangulo(5, 3)
# print(f"El área del rectángulo es: {area}")


# print("----------TERCER EJERCICIO -----------")

# # *args = lista de argumentos posicionales, se pueden pasar varios valores sin necesidad de nombrarlos
# # **kwargs = diccionario de argumentos nombrados, permite pasar pares clave-valor adicionales a la función

# def procesar_estudiantes(escuela, *estudiantes, **datos_adicionales):
#     lista_estudiantes = list(estudiantes)
#     return {
#         "escuela": escuela,
#         "estudiantes": lista_estudiantes,
#         "datos_adicionales": datos_adicionales
#         }

# resultado = procesar_estudiantes("IES Tecnológico", "Ana", "Carlos", "Elena", curso="1º DAW", turno="mañana")
# print(resultado)

print("----------CUARTO EJERCICIO -----------")

cuadrado = lambda x: x ** 2
es_par = lambda x: x % 2 == 0
suma = lambda a, b: a + b

numeros = [1, 2, 3, 4, 5]

# Usar map() con la lambda cuadrado para crear la lista cuadrados
cuadrados = list(map(cuadrado, numeros))
print(f"Números originales: {numeros}")
print(f"Números al cuadrado: {cuadrados}")

# Usar filter() con la lambda es_par para crear la lista pares
pares = list(filter(es_par, numeros))
print(f"Números pares: {pares}")


import os

def listar_archivos_por_tamaño():
    # 1. Obtener todos los elementos en el directorio actual ('.')
    try:
        elementos = os.listdir('.')
        archivos_con_datos = []

        for nombre in elementos:
            # 2. Filtrar solo los archivos (ignorar carpetas)
            if os.path.isfile(nombre):
                # 3. Obtener el tamaño en bytes
                tamaño = os.path.getsize(nombre)
                archivos_con_datos.append((nombre, tamaño))

        # 4. Ordenar la lista por el segundo elemento de la tupla (tamaño)
        # reverse=True para que sea de mayor a menor
        archivos_con_datos.sort(key=lambda x: x[1], reverse=True)

        # 5. Mostrar resultados
        print(f"{'Archivo':<40} | {'Tamaño (Bytes)':>15}")
        print("-" * 60)
        
        for nombre, tamaño in archivos_con_datos:
            print(f"{nombre:<40} | {tamaño:>15,}")

    except OSError as e:
        print(f"Ocurrió un error al acceder al directorio: {e}")

if __name__ == "__main__":
    listar_archivos_por_tamaño()



















