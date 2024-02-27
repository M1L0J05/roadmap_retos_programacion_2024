# Teoría

#La herencia en programación orientada a objetos es un concepto que permite que una clase 
#(llamada subclase) herede atributos y métodos de otra clase (llamada superclase). La 
#subclase puede agregar nuevos atributos y métodos, o modificar los existentes, pero 
#también hereda todas las características de la superclase. Esto ayuda a reutilizar 
#código y a organizar las clases de manera jerárquica.
#
#Una superclase es la clase de la que otra clase (subclase) hereda atributos y métodos. 
#La subclase es la clase que hereda de la superclase. La subclase puede tener sus ropios 
#atributos y métodos además de los que hereda de la superclase.


# Definición de la superclase Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

# Definición de la subclase Perro
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

# Definición de la subclase Gato
class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Función para imprimir el sonido de un animal
def imprimir_sonido(animal):
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

# Creación de objetos y llamada a la función para imprimir su sonido
mi_perro = Perro("Buddy")
mi_gato = Gato("Luna")

#imprimir_sonido(mi_perro)  # Output: Buddy dice: ¡Guau!
#imprimir_sonido(mi_gato)   # Output: Luna dice: ¡Miau!


# Extra
class Empleado:
    def __init__(self, id_empleado, nombre):
        self.id_empleado = id_empleado
        self.nombre = nombre

    def mostrar_info(self):
        print(f"ID Empleado: {self.id_empleado}")
        print(f"Nombre: {self.nombre}")


class Gerente(Empleado):
    def __init__(self, id_empleado, nombre, departamento):
        super().__init__(id_empleado, nombre)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")

class GerenteProyecto(Gerente):
    def __init__(self, id_empleado, nombre, departamento, proyectos):
        super().__init__(id_empleado, nombre, departamento)
        self.proyectos = proyectos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Proyectos a cargo: {', '.join(self.proyectos)}")

class Programador(Empleado):
    def __init__(self, id_empleado, nombre, lenguaje):
        super().__init__(id_empleado, nombre)
        self.lenguaje = lenguaje

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Lenguaje de programación: {self.lenguaje}")


# Ejemplo de uso
empleado1 = GerenteProyecto(1, "Juan", "Desarrollo", ["Proyecto1", "Proyecto2"])
empleado2 = Programador(2, "Ana", "Python")

empleado1.mostrar_info()
print()
empleado2.mostrar_info()
