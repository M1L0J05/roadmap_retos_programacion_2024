# Ejercicio Extra

# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que analice dos palabras diferentes y realice comprobaciones
# * para descubrir si son:
# * - Palíndromos
# * - Anagramas
# * - Isogramas

"""
Definicion:
    Palíndromo: 
    - Una palabra, frase o secuencia que se lee igual en ambos sentidos.
    Ejemplos: "reconocer, radar, oso, salas, anilina".
    Anagrama: 
    - Una palabra o frase formada reorganizando las letras de otra palabra o frase.
    Ejemplos: "amor/Roma, Avisar/Varias, Posta/Pasto", 
    Isograma: 
    - Una palabra en la que no hay letras repetidas (cada letra aparece una sola vez).
    Ejemplo: "murciélago, ligero, cumbre, farsante, ajedrez".

"""

import os
import signal
import sys
import time

## utilidades
# Colores y estilos
COLOR_RED = '91'
COLOR_BLUE = '34'
COLOR_CYAN = '96'
COLOR_GREEN = '32'
COLOR_YELLOW = '33'
COLOR_GRAY = '90'
COLOR_PURPLE = '95'
COLOR_BLACK = '30'
COLOR_WHITE = '37'

# Funcion generica para imprimir en color
def color_text(text, color_code, bold=False):
    bold_code = '1;' if bold else ''    
    return f"\033[{bold_code}{color_code}m{text}\033[0m"

# Funciones de impresión
def error(text, bold=False): print(color_text(text, COLOR_RED, bold=bold))       ###--- ROJO ---###
def info(text, bold=False): print(color_text(text, COLOR_BLUE, bold=bold))       ###--- AZUL ---###
def info_2(text, bold=False): print(color_text(text, COLOR_CYAN, bold=bold))       ###--- CYAN ---###
def success(text, bold=False): print(color_text(text, COLOR_GREEN, bold=bold))    ###--- VERDE ---###
def warning(text, bold=False): print(color_text(text, COLOR_YELLOW, bold=bold))  ###--- AMARILLO ---###
def debug(text, bold=False): print(color_text(text, COLOR_PURPLE, bold=bold))    ###--- PURPURA ---###
def debug_2(text, bold=False): print(color_text(text, COLOR_GRAY, bold=bold))      ###--- GRIS ---###
def others(text, bold=False): print(color_text(text, COLOR_BLACK, bold=bold))    ###--- NEGRO ---###
def standard(text, bold=False): print(color_text(text, COLOR_WHITE, bold=bold))  ###--- BLANCO ---###

# Función de captura de Ctrl+C
def sig_handler(sig, frame):
    warning('\n\n[!] Ejecucion cancelada por el usuario ...\n')
    sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)

# Función para limpiar la terminal
def clean_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def welcome():
    info('\n\n[+] Bienvenido al comprobador de palabras'.upper())
    info_2('\n[i] Introduzca una palabra para comprobar si es: Palindromo, Isograma, Anagrama')
    info_2('[i] Para salir escriba pulse "ctrl + C"')

def user_input():
    prompt_1 = '\n[+] Escriba la primera palabra:'
    prompt_2 = '\n[+] Escriba la segunda palabra:'
    
    while True:
        word_1 = input(''.format(info(prompt_1))).lower().strip()
        word_2 = input(''.format(info(prompt_2))).lower().strip()
        
        # Comprobar que solo sean letras
        if not word_1.isalpha() or not word_2.isalpha():
            warning('[!] Solo se permiten palabras, evite números, símbolos y espacios.')
        else:
            return (word_1.lower(), word_2.lower())
        
# Comprabar si text_ y word_2 son un palindromo
def is_palindrome(word_1: str, word_2: str):
    if word_1 == word_2[::-1]:
        success("[+] Las palabras forman un palíndromo.")
    else:
        error("[-] Las palabras no forman un palíndromo.")

# Comprobar si son isogramas
def is_isogram(word_1: str, word_2: str):
    success("[+] La primera palabra es un isograma.") if len(word_1) == len(set(word_1)) else error("[-] La primera palabra no es un isograma.")
    success("[+] La segunda palabra es un isograma.") if len(word_2) == len(set(word_2)) else error("[-] La segunda palabra no es un isograma.")
    
    word_3 = word_1 + word_2
    success("[+] El conjunto de las dos palabras forman un isograma.") if len(word_3) == len(set(word_3)) else error("[-] El conjunto de las dos palabras no forman un isograma.")

# Comprobar si es anagrama
def is_anagram(word_1: str, word_2: str):
    success("[+] Las palabras son un anagrama.") if sorted(list(word_1)) == sorted(list(word_2)) else error("[-] Las palabras no son un anagrama.")


# Entrada del programa
if __name__ == '__main__':

    clean_terminal()
    welcome()
    texts = user_input()
    info_2('\n[-]- SUS RESULTADOS -[-]\n')
    # Palindromo
    is_palindrome(word_1=texts[0], word_2=texts[1])
    # Isograma
    is_isogram(word_1=texts[0], word_2=texts[1])
    # Anagrama
    is_anagram(word_1=texts[0], word_2=texts[1])
    info_2('\n[-]- FINAL -[-]\n\n')
