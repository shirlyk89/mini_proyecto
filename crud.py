from collections import Counter
from utils import libros
import utils

def agregar_libro():
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
    libros[utils.contador_indice]=datos
    print(f"📚 {titulo} ha sido añadido a tu libreria con el indice {utils.contador_indice}")
    utils.contador_indice+=1

def ver_biblioteca():
    if not libros:
        print("NO hay libros añadidos en tu libreria") 
        print("-------------------------------------")
    else:
        for idx, datos in libros.items():
            estado_libro= "Leido" if datos["estado"] else "NO leido"
            print(f"ID: {idx:<2} | Titulo: {datos['titulo']:<15} | Autor: {datos['autor']:<10} | Género: {datos['genero']:<10} | Año: {datos['ano_publicacion']} | Estado: {estado_libro}")

def buscar_libro():
    print("1. Buscar por titulo")
    print("2. Buscar por autor")
    print("3. Buscar por genero")
    try:
        opcion=int(input("Seleccione una opcion (1-3): "))
        criterio=""
        if opcion == 1: criterio="titulo"
        elif opcion == 2: criterio="autor"
        elif opcion == 3: criterio="genero"
        else: 
            print("Debe elegir un numero entre (1-3)")
            return
        valor=input(f"Ingrese valor para buscar en {criterio} (búsqueda parcial): ").lower()
        resultados=[datos for datos in libros.values() if valor in datos[criterio].lower()]
        if resultados:
            for libro in resultados:
                estado_texto="Leído" if libro["estado"] else "No leído"
                print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['ano_publicacion']}, Género: {libro['genero']}, Estado: {estado_texto}")
        else:
            print("No se encontraron resultados")
    except ValueError:
        print("Se esperaba un número entre (1-3).")

def estado_lectura():
    try:
        indice=int(input("Ingrese el indice del libro: "))
        if indice in libros:
            libros[indice]['estado']=not libros[indice]['estado']
            estado="Leído" if libros[indice]['estado'] else "No leído"
            print(f"{libros[indice]['titulo']} ha sido marcado como {estado}")
        else:
            print("No se encontro el indice")
    except ValueError:
        print("Se esperaba un número válido")

def ver_estadisticas():
    total=len(libros)
    print(f"Total de libros añadidos: {total}")
    leidos=[d['titulo'] for d in libros.values() if d['estado']]
    por_leer=[d['titulo'] for d in libros.values() if not d['estado']]
    print(f"Libros leídos: {len(leidos)} -> {leidos}")
    print(f"Libros por leer: {len(por_leer)} -> {por_leer}")
    generos=[d['genero'] for d in libros.values()]
    if generos:
        genero_frec=Counter(generos).most_common(1)[0]
        print(f"Género más frecuente: {genero_frec[0]} ({genero_frec[1]} libros)")

def eliminar_libro():
    titulo=input("Ingrese título del libro a eliminar (búsqueda parcial): ").lower()
    resultados=[(i,d) for i,d in libros.items() if titulo in d['titulo'].lower()]
    if not resultados:
        print("No se encontraron coincidencias.")
        return
    for idx,(i,d) in enumerate(resultados,1):
        print(f"{idx}. {d['titulo']} (ID {i})")
    try:
        elegir=int(input("Seleccione el número a eliminar: "))
        if 1<=elegir<=len(resultados):
            id_elim=resultados[elegir-1][0]
            eliminado=libros.pop(id_elim)
            print(f"Libro eliminado: {eliminado['titulo']}")
    except ValueError:
        print("Entrada inválida")

def salir():
    print("GRACIAS POR USAR EL PROGRAMA DE GESTOR DE LIBROS. BYE BYE 😄 !!")
    return False
