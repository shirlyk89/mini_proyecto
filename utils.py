import os

libros = {}
contador_indice = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione Enter para continuar...")
