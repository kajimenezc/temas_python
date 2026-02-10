
numero_1 = float(input("Ingrese el numero 1: "))
numero_2 = float(input("Ingrese el numero 2: "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2

if numero_2 == 0:
    division = "No es posible hacer la division por 0"
else:
    division = numero_1 / numero_2
 
print()
print(f"La suma de {numero_1} y {numero_2} es: {suma}")
print(f"La resta de {numero_1} y {numero_2} es: {resta}")
print(f"La multiplicacion de {numero_1} y {numero_2} es: {multiplicacion}")
print(f"La division de {numero_1} y {numero_2} es: {division}")











