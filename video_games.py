"""Ejercicio: Sistema de Inventario de Videojuegos
Enunciado:
Desarrolla un sistema simple para gestionar una colección personal de videojuegos. El sistema debe permitir agregar juegos, ver la colección, marcar juegos como completados y mostrar estadísticas básicas.
Requisitos Técnicos Específicos:
Tipos de Datos Obligatorios:

Listas: Para almacenar la colección de videojuegos
Tuplas: Para representar cada juego (nombre, género, estado_completado)
Strings: Para nombres de juegos y géneros
Booleanos: Para el estado de completado (True/False)
Enteros: Para números de opciones del menú y contadores

Operadores Requeridos:

Aritméticos: +, - (para contadores y cálculos)
Comparación: ==, <=, >= (para validaciones)
Lógicos: and, or, not (para condiciones)
Pertenencia: in (para verificar elementos en listas)

Estructuras de Control Obligatorias:

Condicionales: if, elif, else (mínimo 3 usos diferentes)
Bucle while: Para el menú principal del programa
Bucle for: Para iterar sobre la colección de juegos
Enumerate: Para mostrar números de índice

Funciones Requeridas (mínimo 6):

menu() - Mostrar opciones y retornar elección
add_game() - Agregar nuevo juego
view_games() - Mostrar colección completa
complete_game() - Marcar juego como completado
show_stats() - Mostrar estadísticas
main() - Función principal

Validaciones Obligatorias:

Verificar que la lista no esté vacía antes de mostrar
Validar números de opciones del menú
Controlar índices de la lista al marcar juegos

Funcionalidades Requeridas:

Agregar juego: Solicitar nombre y género, crear tupla, agregar a lista
Ver colección: Mostrar todos los juegos con estado visual (✓/✗)
Marcar completado: Seleccionar juego por número y cambiar estado
Estadísticas: Contar total, completados y pendientes usando bucles
Control de flujo: Menú que se repita hasta seleccionar salir

Elementos Adicionales:

Usar os.system() para limpiar pantalla
Función pause() con input() para control de flujo
Mensajes informativos claros para el usuario

Tiempo estimado: 50 minutos
Nivel: Básico-Intermedio"""

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione Enter para continuar...")

# Lista global para juegos
juegos = []

def clear_screen():
    # Usar os.system para limpiar
    pass

def menu():
  print("1. add game")
  print("2. view games")
  print("3. Complete game")
  print("4. show stats")
  print("5. exit")
  chioce=input("Selecccione una opcion: ")
  return chioce

def add_game():
    nombre=input("Ingrese el Juego: ")
    genero=input("Ingrese el genero: ")
    game=(nombre, genero, False)
    juegos.append(game)
    print(f"{nombre} ha sido añadido a tu lista")

def view_games():
    if not juegos:
        print("No hay juegos añadidos en la lista")
    else: 
        print("===LISTA DE JUEGOS===")
        for indice, (nombre, genero, completado) in enumerate(juegos, 1):
            estado = "✅" if completado else "💀"
            print(f"{indice}. {nombre} ({genero}) - {estado}")

def complete_game():
        if not juegos:
            print("No hay juegos añadidos")
            return 
        else:
            completed=input("Ingrese el numero del juego: ")
            if 1 <= completed <= len(juegos):
                nombre, genero, _=juegos[completed-1]
            print(f"{nombre} Ha sido completado!!!")

def show_stats():
    contador=1
    for juegos in juegos:
        print(f"{contador}. {juegos}")
        contador+=1

def exit_program():
    print("Gracias por usar el programa. !Bye Bye!")
    return False

def main():
    isActive = True
    while isActive:
        clear_screen()
        choice = menu()
        match choice:
            case '1':
                clear_screen()
                add_game()
                pause()
            case '2':
                clear_screen()
                view_games()
                pause()
            case '3':
                clear_screen()
                complete_game()
                pause()
            case '4':
                clear_screen()
                show_stats()
                pause()
            case '5':
                isActive = exit()
            case _:
                print("Opción inválida. Intente de nuevo.")
                pause()

if __name__ == "__main__":
    main()