import os

# Diccionarios y conjuntos globales
usuarios = {}
libros = {}
generos_disponibles = {"Novela", "Ciencia ficcion", "Historia", "Fantasia", "Misterio"}
contador_libros = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione Enter para continuar...") 
