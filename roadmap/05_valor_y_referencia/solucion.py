
# Asignación por valor: 
# Se copia el valor directamente. 
# Esto ocurre con tipos de datos inmutables como números, cadenas y tuplas. 
# Cambiar el valor de una variable no afecta a las demás.

# Ejemplo
a = 10
b = a  # a y b son independientes
b = 20
print(a)  # a sigue siendo 10


# Asignación por referencia: 
# Se comparte la referencia al objeto en la memoria. 
# Esto sucede con tipos de datos mutables como listas y diccionarios. 
# Modificar un objeto afecta a todas las variables que hacen referencia a él.

#Ejemplo
lista1 = [1, 2, 3]
lista2 = lista1  # lista2 apunta al mismo objeto que lista1
lista2.append(4)
print(lista1)  # lista1 se ve afectada, [1, 2, 3, 4]

# En resumen: 
# Con asignación por valor, cada variable tiene su propio valor independiente. 
# Con asignación por referencia, varias variables pueden apuntar al mismo objeto mutable en la memoria.


# * DIFICULTAD EXTRA (opcional):
# * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
# *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
# *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
# *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
# *   Comprueba también que se ha conservado el valor original en las primeras.

def intercambiar_valores(valor1, valor2):
    temp = valor1
    valor1 = valor2
    valor2 = temp
    return valor1, valor2

# Ejemplo de uso
original1 = 5
original2 = 10

nuevo1, nuevo2 = intercambiar_valores(original1, original2)

print("Originales:", original1, original2) # ---> Originales: 5 10
print("Nuevos:", nuevo1, nuevo2) # ---> Nuevos: 10 5


def intercambiar_referencias(lista1, lista2):
    lista1[0], lista2[0] = lista2[0], lista1[0]
    return lista1, lista2

# Ejemplo de uso
original_lista1 = [5]
original_lista2 = [10]

nueva_lista1, nueva_lista2 = intercambiar_referencias(original_lista1, original_lista2)

print("Originales:", original_lista1[0], original_lista2[0]) # ---> Originales: 10 5
print("Nuevos:", nueva_lista1[0], nueva_lista2[0])  # ---> Nuevos: 5 10
