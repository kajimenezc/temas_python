# print("----------PRIMER EJERCICIO -----------")

# numero_1 = float(input("Ingrese el numero 1: "))
# numero_2 = float(input("Ingrese el numero 2: "))

# suma = numero_1 + numero_2
# resta = numero_1 - numero_2
# multiplicacion = numero_1 * numero_2

# if numero_2 == 0:
#     division = "No es posible hacer la division por 0"
# else:
#     division = numero_1 / numero_2
 
# print()
# print(f"La suma de {numero_1} y {numero_2} es: {suma}")
# print(f"La resta de {numero_1} y {numero_2} es: {resta}")
# print(f"La multiplicacion de {numero_1} y {numero_2} es: {multiplicacion}")
# print(f"La division de {numero_1} y {numero_2} es: {division}")

# print("----------SEGUNDO EJERCICIO -----------")

# # edad = int(input("Ingrese su edad: "))

# if edad < 0:
#     print("Edad no valida")
# elif edad >= 0 and edad <= 12:
#     print("Infante")
# elif edad >= 13 and edad <= 17:
#     print("Adolescente")
# elif edad >= 18 and edad <= 64:
#     print("Adulto")
# elif edad >= 65:
#     print("Adulto mayor")

# print("----------TERCER EJERCICIO -----------")

# # range() genera una secuencia de números, útil para iterar en bucles
# # range(inicio, fin+1) crea números desde inicio hasta fin (ambos inclusive)
# def suma_pares(inicio, fin):
#     suma = 0
#     # Itera cada número en el rango (inicio hasta fin + 1 para incluir el fin)
#     for numero in range(inicio, fin + 1):
#         if numero % 2 == 0:
#             suma += numero
#     return suma

# resultado = suma_pares(1, 10)
# print(f"La suma de los números pares entre 1 y 10 es: {resultado}")

# # Otro ejemplo
# resultado2 = suma_pares(5, 15)
# print(f"La suma de los números pares entre 5 y 15 es: {resultado2}")

# print("----------CUARTO EJERCICIO -----------")

# Inicializar suma en 0 para llevar el registro de la suma acumulada
# suma = 0
# contador = 0

# # Bucle while que se ejecuta mientras suma sea menor que 100
# while suma < 100:
#     try:
#         # Solicitar al usuario que ingrese un número entero positivo
#         numero = int(input("Ingrese un número entero positivo: "))
        
#         # Si el número es negativo, mostrar error y continuar sin añadirlo
#         if numero < 0:
#             print("Error: Por favor, ingrese un número entero positivo.")
#             continue
        
#         # Si el número es válido, añadirlo a la suma e incrementar contador
#         suma += numero
#         contador += 1
#         print(f"Número válido añadido. Suma actual: {suma}")
        
#     except ValueError:
#         # Si la entrada no es numérica, mostrar error y continuar
#         print("Error: Entrada no válida. Por favor, ingrese un número entero.")

# # Cuando la suma alcance o supere 100, mostrar mensaje final
# print(f"\n¡Suma completada! Valor final: {suma}")
# print(f"Total de números válidos ingresados: {contador}")

print("----------QUINTO EJERCICIO -----------")

def extraer_info(email):
    # Validar que contenga @ y un punto después del @
    if "@" not in email or "." not in email.split("@")[1]:
        return {}
    
    # Extraer nombre_usuario (parte antes del @)
    nombre_usuario = email.split("@")[0]
    
    # Extraer dominio y extensión (parte después del @)
    parte_dominio = email.split("@")[1]
    dominio = parte_dominio.split(".")[0]
    extension = parte_dominio.split(".")[-1]
    
    # Devolver diccionario con las tres claves
    return {
        "nombre_usuario": nombre_usuario,
        "dominio": dominio,
        "extension": extension
    }

# Ejemplo de uso
resultado = extraer_info("usuario@ejemplo.com")
print(resultado)

# Ejemplo incorrecto (sin @)
resultado2 = extraer_info("usuario@ejemplocom")
print(resultado2)



# En Python, la indentación es crucial en las estructuras condicionales para definir los bloques de código.
# El operador lógico or devuelve True si al menos una de las condiciones es verdadera.
# El operador lógico not invierte el valor de verdad de una expresión.











