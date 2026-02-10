
print("----------PRIMER EJERCICIO -----------")
print()
age = 28
height = 1.80
is_student = False
name = "Kevin Jimenez"

print(f"La persona es {name}")
print(f"Tiene: {age} años")
print(f"Su altura es: {height}")
print(f"Es estudiante: {is_student}")
print()
print("----------SEGUNDO EJERCICIO -----------")
print()
numeros = [10, 20, 30, 40, 50]

numeros.append(60)
numeros.insert(1,15)
del numeros[3]

suma = sum(numeros)
promedio = suma / len(numeros)

print(f"Lista: {numeros}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")

print()
print("----------TERCER EJERCICIO -----------")
print()

contacto = ("Ana Garcia", "ana@ejemplo.com", "555-1234")

nombre, email, telefono = contacto


print(f"Nombre: {nombre}")
print(f"Email: {email}")
print(f"Telefono: {telefono}")

contacto_completo = (nombre, email, telefono, "Madrid")
print()
print(f"Tupla final: {contacto_completo}")

print()
print("----------CUARTO EJERCICIO -----------")
print()

contactos = { 
    "persona1": {"nombre": "Edwin", "telefono": "11111111111", "correo_electronico": "edwin@gmail.com"},
    "persona2": {"nombre": "Kevin", "telefono": "22222222222", "correo_electronico": "kevin@gmail.com"},
    "persona3": {"nombre": "Anyely", "telefono": "3333333333", "correo_electronico": "anyely@gmail.com"}
}

correo_persona2 = contactos.get("persona2").get("correo_electronico")

print(f"Correo de la 2 persona es: {correo_persona2}")

contactos["persona4"] = {"nombre": "Esteffany", "telefono": "4444444444", "correo_electronico": "esteffany@gmail.com"}

contactos["persona1"]["telefono"] = "5555555555"

for contacto in contactos:
    nombre = contactos[contacto]["nombre"]
    print(f"Nombre de la persona: {nombre}")


print()
print("----------QUINTO EJERCICIO -----------")
print()

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

# 1. Intersección (en ambas listas)
interseccion = conjunto1 & conjunto2
print("Elementos en ambas listas:", interseccion)

# 2. Solo en la primera lista
solo_lista1 = conjunto1 - conjunto2
print("Solo en la primera lista:", solo_lista1)

# 3. Solo en la segunda lista
solo_lista2 = conjunto2 - conjunto1
print("Solo en la segunda lista:", solo_lista2)

# 4. Unión (todos los únicos)
union = conjunto1 | conjunto2
print("Todos los elementos únicos:", union)


print()
print("----------SEXTO EJERCICIO -----------")
print()
from collections import Counter

def analizar_texto(texto):
    # Total de caracteres (con espacios)
    total_caracteres = len(texto)

    # Quitar espacios para el conteo
    texto_sin_espacios = texto.replace(" ", "")
    total_sin_espacios = len(texto_sin_espacios)

    # Contar frecuencias
    contador = Counter(texto_sin_espacios)

    # 3 caracteres más comunes
    caracteres_mas_comunes = contador.most_common(3)

    return {
        "caracteres_mas_comunes": caracteres_mas_comunes,
        "total_caracteres": total_caracteres,
        "total_sin_espacios": total_sin_espacios
    }

resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)











