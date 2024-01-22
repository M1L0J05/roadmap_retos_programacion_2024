import os
import sys
import signal
import time

# Paleta de colores
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def info_1(skk): print(color_text(skk, '34'))  # AZUL 1
def succes_1(skk): print(color_text(skk, '32'))  # VERDE 1
def warning_1(skk): print(color_text(skk, '33'))  # AMARILLO 1

# Función de captura de Ctrl+C
def sig_handler(sig, frame):
    info_1('\n\n[!] Saliendo del programa ...\n')
    sys.exit(0)

# Función para limpiar la terminal
def clean_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

# Variables globales
contact_book = {
    'Juan': '1234567890',
    'Maria': '2345678901',
    'Carlos': '3456789012',
    'Laura': '4567890123',
    'Alejandro': '5678901234',
}

# Funciones
def welcome():
    info_1('\n\n[+] Bienvenido a su agenda de contactos')

def check_book(contacts):
    if not contacts:
        info_1('\n\n[+] Su agenda está vacía.')
    else:
        info_1('\n\n[+] Sus contactos son:')
        for contact, number in contacts.items():
            print(f'   \033[96m[-]\033[0m \033[32m{contact}\033[0m - {number}')
            time.sleep(0.1)

def check_name(contacts, prompt):
    while True:
        name_input = input(prompt)
        match name_input:
            case name if name in contacts:
                return name, True
            case _:
                warning_1('\n[!] No existe el contacto.')
                return name_input, False

def check_number(prompt):
    while True:
        number_input = input(prompt)
        if number_input.isdigit() and 0 < len(number_input) < 12:
            return number_input
        else:
            warning_1('\n[!] Número no válido. Debe contener solo dígitos y no exceder la longitud máxima de 11 dígitos.')

def user_options():
    info_1('\n\n[+] ¿Qué desea hacer?')
    time.sleep(0.1)
    succes_1('    [1] Introducir un nuevo contacto. ')
    time.sleep(0.1)
    succes_1('    [2] Actualizar un contacto.')
    time.sleep(0.1)
    succes_1('    [3] Borrar un contacto.')
    time.sleep(0.1)
    succes_1('    [4] Borrar la agenda.')
    time.sleep(0.1)
    succes_1('    [5] Salir de la agenda.')

    while True:
        try:
            option_input = int(input(info_1('\n[+] Indique su elección: ')))
            match option_input:
                case 1 | 2 | 3 | 4 | 5:
                    return option_input
                case _:
                    warning_1('[!] Por favor, elija una opción válida. ')
        except ValueError as error:
            warning_1('[!] Por favor, elija una opción válida. ')

def exit_book():
    info_1('\n\n[+] Cerrando la agenda.\n\n')
    time.sleep(0.5)
    sys.exit(0)

def new_contact(contacts):
    prompt_name = '\n[+] Indique el nombre del contacto: '
    name_input, contact_exists = check_name(contacts, prompt_name)
    if not contact_exists:
        prompt_number = '\n[+] Indique el número del contacto: '
        number_input = check_number(prompt_number)
        contacts[name_input] = number_input

def delete_contact(contacts):
    prompt_name = '\n[+] Indique el nombre del contacto que quiere borrar: '
    name_input, contact_exists = check_name(contacts, prompt_name)
    if contact_exists:
        del contacts[name_input]
        info_1('\n[+] Contacto borrado correctamente.')

def update_contact(contacts):
    prompt_name = '\n[+] Indique el nombre del contacto que quiere actualizar: '
    name_input, contact_exists = check_name(contacts, prompt_name)
    if contact_exists:
        prompt_number = '\n[+] Indique el número del nuevo contacto: '
        number_input = check_number(prompt_number)
        contacts[name_input] = number_input

def delete_book(contacts):
    contacts.clear()

def update_contact_book(user_option, contacts):
    match user_option:
        case 1:
            new_contact(contacts)
        case 2:
            update_contact(contacts)
        case 3:
            delete_contact(contacts)
        case 4:
            delete_book(contacts)
        case 5:
            exit_book()

# Entrada del programa
if __name__ == '__main__':
    signal.signal(signal.SIGINT, sig_handler)
    clean_terminal()
    while True:
        welcome()
        check_book(contact_book)
        user_option = user_options()
        update_contact_book(user_option, contact_book)
        clean_terminal()
