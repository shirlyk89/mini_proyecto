from utils import usuarios, libros, generos_disponibles, contador_libros
import utils

def registrar_usuario():
    cedula = input("Ingrese cedula del usuario: ")
    if cedula in usuarios:
        print("❌ El usuario ya esta registrado.")
        return
    nombre = input("Ingrese nombre del usuario: ")
    print(f"Géneros disponibles: {generos_disponibles}")
    generos_favoritos = set(input("Ingrese sus generos favoritos separados por coma: ").split(","))
    generos_favoritos = {g.strip().title() for g in generos_favoritos}
    generos_disponibles.update(generos_favoritos)
    usuarios[cedula] = {"nombre": nombre,"generos_favoritos": generos_favoritos,"historial": []}
    print(f"✅ Usuario {nombre} registrado correctamente.")

def agregar_libro():
    global contador_libros
    titulo = input("Ingrese titulo del libro: ")
    autor = input("Ingrese autor del libro: ")
    genero = input("Ingrese genero del libro: ").title()
    if genero not in generos_disponibles:
        print("⚠️ El genero no estaba en la biblioteca, pero sera añadido.")
        generos_disponibles.add(genero)
    libros[utils.contador_libros] = {"titulo": titulo,"autor": autor,"genero": genero,"disponible": True}
    print(f"✅ Libro '{titulo}' agregado con codigo {utils.contador_libros}.")
    utils.contador_libros += 1

def prestar_libro():
    cedula = input("Ingrese cedula del usuario: ")
    if cedula not in usuarios:
        print("❌ Usuario no registrado.")
        return
    try:
        codigo = int(input("Ingrese codigo del libro: "))
        if codigo not in libros:
            print("❌ Libro no encontrado."); return
        if not libros[codigo]["disponible"]:
            print("❌ El libro ya está prestado."); return
        libros[codigo]["disponible"] = False
        usuarios[cedula]["historial"].append(codigo)
        print(f"📚 {usuarios[cedula]['nombre']} ha tomado prestado '{libros[codigo]['titulo']}'.")
    except ValueError:
        print("❌ Codigo invalido.")

def devolver_libro():
    try:
        codigo = int(input("Ingrese código del libro a devolver: "))
        if codigo not in libros:
            print("❌ Libro no encontrado."); return
        if libros[codigo]["disponible"]:
            print("⚠️ Este libro ya esta disponible."); return
        libros[codigo]["disponible"] = True
        print(f"✅ Libro '{libros[codigo]['titulo']}' devuelto correctamente.")
    except ValueError:
        print("❌ Código inválido.")

def recomendar_libros():
    cedula = input("Ingrese cédula del usuario: ")
    if cedula not in usuarios:
        print("❌ Usuario no registrado."); return
    favoritos = usuarios[cedula]["generos_favoritos"]
    print(f"\n🎯 Recomendaciones para {usuarios[cedula]['nombre']} (géneros: {favoritos}):")
    recomendaciones = [datos for datos in libros.values() if datos["genero"] in favoritos and datos["disponible"]]
    if recomendaciones:
        for libro in recomendaciones:
            print(f"- {libro['titulo']} ({libro['genero']}) de {libro['autor']}")
    else:
        print("❌  No hay recomendaciones disponibles.")

def analisis_usuarios():
    if len(usuarios) < 2:
        print("⚠️ Se necesitan al menos dos usuarios."); return
    ced1 = input("Ingrese cedula del primer usuario: ")
    ced2 = input("Ingrese cedula del segundo usuario: ")
    if ced1 not in usuarios or ced2 not in usuarios:
        print("❌ Alguno de los usuarios no esta registrado."); return
    g1 = usuarios[ced1]["generos_favoritos"]
    g2 = usuarios[ced2]["generos_favoritos"]
    print(f"\n📊 Análisis entre {usuarios[ced1]['nombre']} y {usuarios[ced2]['nombre']}:")
    print(f"- Géneros en común: {g1 & g2}")
    print(f"- Géneros únicos: {g1 ^ g2}")
    print(f"- ¿{usuarios[ced1]['nombre']} subconjunto de {usuarios[ced2]['nombre']}? {g1 <= g2}")
    print(f"- ¿{usuarios[ced2]['nombre']} subconjunto de {usuarios[ced1]['nombre']}? {g2 <= g1}")

def salir():
    print("Salida del programa.👋 ")
    return False
