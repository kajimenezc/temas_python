
# Ejercicio 1
#
#class Persona:
#    def __init__( self, nombre, edad ):
#        self.nombre = nombre
#        self.edad = edad
#    def presentarse( self ):
#        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
#Persona1 = Persona("Juan", 30)
#print(Persona1.presentarse())

# Ejercicio 2

#class Libro:
#    def __init__( self, titulo, autor, paginas ):
#        self.titulo = titulo
#        self.autor = autor
#        self.paginas = paginas
#
#    def describir(self):
#        return  f"'{self.titulo}' escrito por {self.autor} - {self.paginas} páginas."
#
#    def es_largo(self):
#        return self.paginas > 300
#    
#    def resumir(self, longitud=None):
#        if longitud is None:
##            longitud = 50#
#
#        return f"'{self.titulo}' - Resumen de {longitud} caracteres."
    
#Libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
#print(Libro1.describir())
#print(Libro1.es_largo())
#print(Libro1.resumir(100))

#Libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
#print(Libro2.describir())
#print(Libro2.es_largo())
#print(Libro2.resumir())

# Actividad 3

#class Biblioteca:

#    total_libros = 0
#    nombre_biblioteca = "Biblioteca Central"

#    def __init__( self, nombre_seccion):
#        self.nombre_seccion = nombre_seccion
#        self.libros = []
    
#    def agregar_libro(self, libro):
#        self.libros.append(libro)
#        Biblioteca.total_libros += 1

#    def obtener_informe(self):
#        return f"Sección: {self.nombre_seccion} de {self.nombre_biblioteca} : Total libros: {self.libros.__len__()}"  

#Biblioteca1 = Biblioteca("Ficción")
#Biblioteca1.agregar_libro("Cien Años de Soledad")
#Biblioteca1.agregar_libro("El Principito")
#print(Biblioteca1.obtener_informe())

#Biblioteca2 = Biblioteca("Arte")
#Biblioteca2.agregar_libro("Historia del Arte")
#print(Biblioteca2.obtener_informe())

# Actividad 4

class Contador:

    contadores_creados = 0

    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial  # Atributo de instancia para el valor del contador
        Contador.contadores_creados += 1  # Incrementa el contador de instancias creadas

    def incrementar(self):
        self.valor += 1
        return self.valor
    
    def decrementar(self):
        self.valor -= 1
        if self.valor < 0:
            self.valor = 0
        return self.valor
    
    @classmethod
    def reiniciar_contador_global(cls):
        cls.contadores_creados = 0

    @staticmethod
    def es_par(numero):
        return numero % 2 == 0


contador1 = Contador()
contador2 = Contador()

print(contador1.incrementar())  # Incrementa el valor del contador1
print(contador2.decrementar())  # Decrementa el valor del contador2

Contador.reiniciar_contador_global()  # Reinicia el contador global de instancias
print(contador1.incrementar())  # Incrementa el valor del contador1
print(Contador.es_par(contador1.valor))  # Verifica si el valor es par
print(Contador.es_par(contador2.valor))  # Verifica si el valor es par   


#  Actividad 5

class Vehiculo:

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f"{self.marca} - {self.modelo} ({self.año})"

class Automovil(Vehiculo):

    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)    
        self.puertas = puertas

    def mostrar_info(self):
        return f"{super().mostrar_info()} - {self.puertas} puertas"

class Motocicleta(Vehiculo):

    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)    
        self.cilindrada = cilindrada

    def mostrar_info(self):
        return f"{super().mostrar_info()} - cc: {self.cilindrada}"
    

automovil1 = Automovil("Toyota", "Corolla", 2020, 4)
motocicleta1 = Motocicleta("Honda", "CBR500R", 2019, 500)   

print(automovil1.mostrar_info())  # Muestra la información del automóvil
print(motocicleta1.mostrar_info())  # Muestra la información de la motocicleta

# Actividad 6

class Libro:

    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        """Agregar un nuevo libro a la colección"""
        self.libros.append(libro)
    
    def buscar_por_titulo(self, titulo):
        """Buscar libros por título (devolviendo todos los que contengan la cadena de búsqueda)"""
        resultados = []
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                resultados.append(libro)
        return resultados
    
    def contar_por_autor(self, autor):
        """Contar cuántos libros hay de un autor específico"""
        contador = 0
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                contador += 1
        return contador


# Pruebas de Actividad 6
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("El Amor en los Tiempos del Cólera", "Gabriel García Márquez", 1985)
libro3 = Libro("La Casa de los Espíritus", "Isabel Allende", 1982)
libro4 = Libro("El Joven Montaigne", "Walter Pater", 1873)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)

# Buscar por título
print("=== Búsqueda por título: 'Amor' ===")
resultados = biblioteca.buscar_por_titulo("Amor")
for libro in resultados:
    print(f"  - {libro.titulo} ({libro.autor}, {libro.año_publicacion})")

# Contar libros por autor
print("\n=== Contar libros por autor ===")
print(f"Gabriel García Márquez: {biblioteca.contar_por_autor('Gabriel García Márquez')} libros")
print(f"Isabel Allende: {biblioteca.contar_por_autor('Isabel Allende')} libro(s)")
print(f"Walter Pater: {biblioteca.contar_por_autor('Walter Pater')} libro(s)")

   
# Actividad 7

# operaciones_matematicas.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b   

def multiplicar(a, b):
    return a * b        

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

## Definición de la constante PI

_PI = 3.14159  # Definición de la constante PI


# calculadora.py
from operaciones_matematicas import sumar, restar, multiplicar, dividir, _PI

## Calcular y mostrar el resultado de sumar 15 y 7

sumardo = sumar(15, 7)
print(f"Resultado de sumar 15 y 7: {sumardo}") 

## Calcular y mostrar el resultado de multiplicar 3.5 por 2
multiplicardo = multiplicar(3.5, 2)
print(f"Resultado de multiplicar 3.5 por 2: {multiplicardo}")

## Calcular y mostrar el área de un círculo con radio 5
radio = 5
area_circulo = _PI * (radio ** 2) 












































