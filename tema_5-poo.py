
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



























































