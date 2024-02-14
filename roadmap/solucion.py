# Teoria

# Pilas (Stacks - LIFO):
# 1. Una pila es una estructura de datos en la que los elementos
# se añaden y se eliminan siguiendo una política conocida como LIFO, 
# que significa "Last In, First Out" (último en entrar, primero en salir).
# 
# 2. Imagina una pila de platos: 
# El último plato que colocas sobre la pila será el primero en ser retirado.
# 
# 3. En Python, puedes implementar una pila utilizando una lista. 
# Puedes añadir elementos a la pila usando el método `append()` 
# y eliminar elementos usando el método `pop()`.

# Colas (Queue - FIFO):
# 1. Una cola es otra estructura de datos en la que los elementos se añaden y 
# se eliminan siguiendo una política conocida como FIFO, 
# que significa "First In, First Out" (primero en entrar, primero en salir).
#
# 2. Imagina una cola en una tienda: 
# La persona que llega primero es la primera en ser atendida.
# 
# 3. En Python, puedes implementar una cola utilizando la clase `deque` 
# del módulo `collections`. Puedes añadir elementos a la cola usando 
# el método `append()` y eliminar elementos usando el método `popleft()`.

import time
from collections import  deque

stack_lifo = []

print(f'\n[+] Modificando elementos de la pila:')
print(f'\n[+] Contenido de la pila {stack_lifo}')


for i in range(1,6):
    stack_lifo.append(f'item_{i}')
    print(f'\n[+] Añadido un elemento al stack_LIFO')
    print(f'[+] Contenido de la pila {stack_lifo}')
    time.sleep(0.3)


for i in range(0, len(stack_lifo)):
    stack_lifo.pop()
    print(f'\n[+] Eliminado un elemento al stack_LIFO')
    print(f'[+] Contenido de la pila {stack_lifo}')
    time.sleep(0.3)

stack_fifo = deque()

for i in range(1,6):
    stack_fifo.append(f'item_{i}')
    print(f'\n[+] Añadido un elemento al stack_FIFO')
    print(f'[+] Contenido de la pila {stack_fifo}')
    time.sleep(0.3)

for i in range(0, len(stack_fifo)):
    stack_fifo.popleft()
    print(f'\n[+] Eliminado un elemento al stack_FIFO')
    print(f'[+] Contenido de la pila {stack_fifo}')
    time.sleep(0.3)

# Ejercicios Extra
