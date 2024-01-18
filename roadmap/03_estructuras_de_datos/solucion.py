"""
Explicacion teórica:

1. Listas: 
    Secuencia mutable de elementos. Se define con corchetes. Ejemplo: `mi_lista = [1, 2, 3]`.
2. Tuplas: 
    Secuencia inmutable de elementos. Se define con paréntesis. Ejemplo: `mi_tupla = (1, 2, 3)`.
3. Conjuntos: 
    Colección no ordenada de elementos únicos. Se define con llaves. Ejemplo: `mi_conjunto = {1, 2, 3}`.
4. Diccionarios: 
    Colección de pares clave-valor. Se define con llaves y dos puntos. Ejemplo: `mi_diccionario = {'clave': 'valor'}`.
5. Colas (Queue): 
    Estructura de datos FIFO (First In, First Out) para almacenar elementos.
6. Pilas (Stack): 
    Estructura de datos LIFO (Last In, First Out) para almacenar elementos.
7. Arreglos (mediante NumPy): 
    Estructuras eficientes para trabajar con datos numéricos multidimensionales en arrays.

"""
# Ejercicios
# Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# Utiliza operaciones de inserción, borrado, actualización y ordenación.

# Lista
mi_lista = [1, 2, 3, 4, 5]

# Inserción en lista
mi_lista.append(6)
print("Lista después de inserción:", mi_lista)

# Borrado en lista
mi_lista.remove(3)
print("Lista después de borrado:", mi_lista)

# Actualización en lista
mi_lista[0] = 10
print("Lista después de actualización:", mi_lista)

# Ordenación en lista
mi_lista.sort()
print("Lista ordenada:", mi_lista)

# Tupla
# No se pueden realizar operaciones de inserción, borrado, o actualización en tuplas
mi_tupla = (1, 2, 3, 4, 5)

# Conjunto
mi_conjunto = {1, 2, 3, 4, 5}

# Inserción en conjunto
mi_conjunto.add(6)
print("Conjunto después de inserción:", mi_conjunto)

# Borrado en conjunto
mi_conjunto.remove(3)
print("Conjunto después de borrado:", mi_conjunto)

# Diccionario
mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}

# Inserción y actualización en diccionario
mi_diccionario['clave4'] = 'valor4'
mi_diccionario['clave1'] = 'nuevo_valor1'
print("Diccionario después de inserción y actualización:", mi_diccionario)

# Borrado en diccionario
del mi_diccionario['clave2']
print("Diccionario después de borrado:", mi_diccionario)

# Cola (Queue) y Pila (Stack)
# No hay operaciones directas de actualización o ordenación.
# Cola (Queue)
from queue import Queue

mi_cola = Queue()
mi_cola.put(1)
mi_cola.put(2)
mi_cola.put(3)

print("Cola:", mi_cola)

# Arreglo (NumPy)
import numpy as np

mi_arreglo = np.array([1, 2, 3, 4, 5])

# Actualización en arreglo
mi_arreglo[0] = 10
print("Arreglo después de actualización:", mi_arreglo)

# Ordenación en arreglo
mi_arreglo.sort()
print("Arreglo ordenado:", mi_arreglo)


# Ejercicio extra: Agenda de contactos por terminal

CONTACT_BOOK = {}

