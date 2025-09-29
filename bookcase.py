# Requerimientos Funcionales:

"""1. Agregar libro: Título, autor, género, año de publicación, estado (leído/no leído)
2. Ver biblioteca completa: Mostrar todos los libros con su información
3. Buscar libros: Por título, autor o género
4. Cambiar estado de lectura: Marcar como leído/no leído
5. Estadísticas: Mostrar total de libros, leídos, por leer, y géneros más frecuentes
6. Eliminar libro: Remover libro de la colección """


import os

def menu():
    print("████████ SISTEMA DE GESTION DE BIBLIOTECA PERSONAL ████████")
    print("1. Agregar libro")
    print("2. Ver biblioteca completa")
    print("3. Buscar libros")
    print("4. Cambiar estado de lectura")
    print("5. Ver estadisticas")
    print("6. Eliminar libro")
    print("7. Salir")
    opcion=input("Seleccione una opcion (1-7): ")
    return opcion

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione Enter para continuar...") 

libros={}
contador_indice=1

def agregar_libro():
    global contador_indice
    titulo=input("Nombre del libro: ")
    autor=input("Autor del libro: ")
    genero=input("Genero: ") 
    ano_publicacion=input("Año de publicacion: ")
    estado_libronuevo=input("Ya leiste este libro?, (s-n): ").lower()
    datos={ 
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "ano_publicacion": ano_publicacion,
        "estado": True if estado_libronuevo == "s" else False
    }

    libros[contador_indice]=datos
    print(f"📚 {titulo} ha sido añadido a tu libreria con el indice {contador_indice}")
    contador_indice+=1 

def ver_biblioteca():
    if not libros:
        print("NO hay libros añadidos en tu libreria") 
        print("-------------------------------------")
    else:
        for contador_indice, datos in libros.items():
            estado_libro= "Leido" if datos["estado"] else "NO leido"
            print(f"Libros almacenados: 💻 |ID: {contador_indice:<2} |titulo: {datos['titulo']:<5} |autor: {datos['autor']:<5} |genero: {datos['genero']:<5} |año de publicacion: {datos['ano_publicacion']:<4}")

def buscar_libro():
    print("1. Buscar por titulo: ")
    print("2. Buscar por autor: ")
    print("3. Buscar por genero: ")
    try:
        opcion=int(input("Seleccione una opcion: (1-3): "))
        criterio=""
        
        if opcion == 1:
            criterio="titulo" 
        elif opcion == 2:
            criterio="autor"
        elif opcion == 3:
            criterio="genero" 
        else: 
            print("Debe elegir un numero entre (1-3)")
        
        valor = input(f"Ingrese el valor para buscar en {criterio} (búsqueda parcial): ").lower()

        resultados = [datos for datos in libros.values() if valor in datos[criterio].lower()]


        if resultados:
            print(f"\n--- Resultados de la búsqueda parcial por '{criterio}' = '{valor}' ---")
            for libro in resultados:
                estado_texto = "Leído" if libro["estado"] == 's' else "No leído"
                print(f"Título: {libro['titulo'].title()}, Autor: {libro['autor'].title()}, Año: {libro['ano_publicacion']}, Género: {libro['genero'].title()}, Estado: {estado_texto}")
                print("»»»»»"*40)
        else:
            print("opcion no encontrada")
    except ValueError:
        print("Invalido. Se esperaba un numero entre (1-3), Intente nuevamente.")

leidos=[]
por_leer=[]
      
def estado_lectura():
    leido=input("Quieres marcar un libro como leido? (s/n): ")
    try:
        if leido.lower() == "s":
        
            indice=int(input("Ingrese el indice del libro: "))
            if indice in libros:
                libros[indice]['estado']=True
                estado_completado=libros[indice]['titulo']
                leidos.append(estado_completado)
                print(f" {estado_completado} ha sido marcado como leido ✔️" )

            else: 
                indice not in libros
                print("No se encontro el indice del libro en la biblioteca 👀")
        else:
            pendientes=libros[indice]['titulo']
            por_leer.append(pendientes)
            print("El libro ha sido marcado como NO leido ❌")
    except ValueError:
                print("Se esperaba un numero para buscar el ID del libro. Intentalo nuevamente 😉")

       
from collections import Counter

def ver_estadisticas():
    for contador_indice, (id_libro, datos) in enumerate(libros.items(), 1):
        print(f" Total de libros añadidos: {contador_indice}. titulo: {datos['titulo']}, autor: {datos['autor']}, ")

    leidos = [datos['titulo'] for _, datos in libros.items() if datos['estado']]
    por_leer = [datos['titulo'] for _, datos in libros.items() if not datos['estado']]

    print(f"Libros leídos: {len(leidos)} -> {leidos}")
    print(f"Libros por leer: {len(por_leer)} -> {por_leer}")

    generos=[datos['genero'] for _, datos in libros.items()]
    if generos:
        genero_frecuente=Counter(generos).most_common(1)[0]
        print(f"El genero mas frecuente es: {genero_frecuente[0]} ({genero_frecuente[1]}libros)")


def eliminar_libro():
    opcion_eliminar=input("Quiere eliminar un libro? (s-n): ")
    criterio=""

    if opcion_eliminar.lower() == "s":
        criterio="titulo"
        datos_busqueda = input(f"Ingrese el titulo del libro {criterio} (búsqueda parcial): ").lower()
        resultados = [(indice, datos) for indice, datos in libros.items() if datos_busqueda in datos[criterio].lower()]
        
        if resultados:
            print(f"\n--- Resultados de la búsqueda parcial por '{criterio}' = '{datos_busqueda}' ---")
            for i, (indice, datos) in enumerate(resultados, 1):
                print(f"{i}, {datos['titulo']} (ID: {indice})") 
        verificar=input(f"Estas seguro de que quieres eliminar {datos_busqueda}? (s-n):")
        if verificar == "s":
            if len(resultados)==1:
                libro_a_eliminar=resultados[0][0]
                eliminado=libros.pop(libro_a_eliminar)
                print(f"EL libro eliminado fue {eliminado['titulo']}")
                    
                    # Si la busqueda arroja mas de un resultado
            else: 
                buscar_indice=int(input("Escriba el indice del libro: "))
                if buscar_indice in libros:
                    eliminar=libros.pop(buscar_indice)
                    print(f"{eliminar['titulo']} ha sido eliminado ")
        else: 
            print(f"{datos_busqueda} No fue eliminado")
        
    else: 
        print("No se encontraron resultados similares")
            
         
            


def salir():
    print("GRACIAS POR USAR EL PROGRAMA DE GESTOR DE LIBROS. BYE BYE 😄 !!")
    return False

def main():
    isActive = True
    while isActive:
        clear_screen()
        opcion = menu()
        match opcion:
            case '1':
                clear_screen()
                agregar_libro()
                pause()
            case '2':
                clear_screen()
                ver_biblioteca()
                pause()
            case '3':
                clear_screen()
                buscar_libro()
                pause()
            case '4':
                clear_screen()
                estado_lectura()
                pause()
            case '5':
                clear_screen()
                ver_estadisticas()
                pause()
            case '6':
                  clear_screen()
                  eliminar_libro()
                  pause()
            case '7':
                    isActive = salir()
            case _:
                print("Error, Intente de nuevo.")
                pause()

if __name__ == "__main__":
    main()