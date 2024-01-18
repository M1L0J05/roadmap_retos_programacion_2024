import os
import sys
import signal
import time

### Paleta de colores ###
### FUNCIONES PREDEFINIDAS PARA IMPRIMIR EN COLORES ###
def info_1(skk): print("\033[34m{}\033[0m" .format(skk))        ###--- AZUL 1 ---###
def succes_1(skk): print("\033[32m{}\033[0m" .format(skk))      ###--- VERDE 1 ---###
def warning_1(skk): print("\033[33m{}\033[0m" .format(skk))     ###--- AMARILLO 1 ---###

### Funcion de captura de Ctrl+c ###
def sig_handler(sig, frame):
        info_1('\n\n[!] Saliendo del programa ...\n')
        sys.exit(0)


### Funcion para limpiar terminal
def clean_terminal():
    operative_system = os.name

    if operative_system == 'posix':  # Linux y macOS
        os.system('clear')
    elif operative_system == 'nt':  # Windows
        os.system('cls')
    else:
        warning_1('[!] No se pudo determinar el sistema operativo. La terminal no pudo ser limpiada.')

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
    if len(contacts) == 0:
        info_1('\n\n[+] Su agenda esta vacia.')
    else:
        info_1('\n\n[+] Su contactos son:')
        for contact, number in contacts.items():
            print('   \033[96m[-]\033[0m \033[32m{}\033[0m - {}'.format(contact, number))
            time.sleep(0.1)

def check_name(contacts, prompt):
    name_input = input(''.format(info_1(prompt)))
    if name_input in contacts:
        contact_exit = True
    else:
        contact_exit = False
    return (name_input, contact_exit)

def check_number(prompt):
    while True:
        number_input = input(''.format(info_1(prompt)))
        try:
            if int(number_input):
                if len(number_input) < 12:
                    return number_input
                else:
                    warning_1('\n[!] Número no valido. Excede la logitud máxima de 11 digitos, compruebelo. ')
        except ValueError as error:
            warning_1('[!] Por favor, introduzca un número valido. ')

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
        option_input = input(''.format(info_1('\n[+] Indique su eleccion:')))
        try:
            if int(option_input) <= 0 or int(option_input) > 5:
                warning_1('[!] Por favor, elija una opción valida. ')
            else:
                return int(option_input)
        except ValueError as error:
            warning_1('[!] Por favor, elija una opción valida. ')

def exit_book():
    info_1('\n\n[+] Cerrando la agenda.\n\n')
    time.sleep(0.5)
    return sys.exit(0)

def new_contact(contacts):
    prompt_name = '\n[+] Indique el nombre del contacto:'
    name_input = check_name(contacts, prompt_name)
    if name_input[1]:
        warning_1('\n[!] Ya existe el contacto.')
        time.sleep(1)
        return
    prompt_number = '\n[+] Indique el número del contacto:'
    number_input = check_number(prompt_number)
    contact_book[name_input[0]] = int(number_input)
    return

def delete_contact(contacts):
    prompt_name = '\n[+] Indique el nombre del contacto que quiere borrar:'
    name_input = check_name(contacts, prompt_name)
    if name_input[1] == False:
        warning_1('\n[!] No existe el contacto para borrar.')
        time.sleep(1)
        return
    else:
        del contacts[name_input[0]]
        info_1('\n[+] Contacto borrado correctamente.')
        return

    #contact_book[name_input[0]] = int(number_input)

def update_contact(contacts):
    prompt_name = '\n[+] Indique el nombre del contacto que quiere actulizar:'
    name_input = check_name(contacts, prompt_name)
    if name_input[1] == False:
        warning_1('\n[!] No existe el contacto para actualizar.')
        time.sleep(1)
        return
    prompt_number = '\n[+] Indique el número del nuevo contacto:'
    number_input = check_number(prompt_number)
    contact_book[name_input[0]] = int(number_input)

def delete_book(contacts):
    return contacts.clear()

def update_contact_book(user_option, contacts):
    if user_option == 1:
        new_contact(contacts)
    if user_option == 2:
        update_contact(contacts)   
    if user_option == 3:
        delete_contact(contacts)
    if user_option == 4:
        delete_book(contacts)
    if user_option == 5:
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
