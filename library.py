# ==============================
# SISTEMA DE GESTIÓN DE BIBLIOTECA
# ==============================
import os

# Diccionario de usuarios
usuarios = {}
# Diccionario de libros
libros = {}
# Conjunto de géneros literarios disponibles
generos_disponibles = {"Novela", "Ciencia ficcion", "Historia", "Fantasia", "Misterio"}
# Contador de códigos de libros
contador_libros = 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione Enter para continuar...") 

#menu
def menu():
    print("\n===== MENU BIBLIOTECA =====")
    print("1. Registrar usuario")
    print("2. Agregar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Recomendar libros")
    print("6. Análisis de usuarios")
    print("7. Salir")
    opcion = input("Seleccione una opcion entre (1-7): ")
    return opcion
    

# 1. Registrar usuario
def registrar_usuario():
    cedula = input("Ingrese cedula del usuario: ")
    if cedula in usuarios:
        print("❌ El usuario ya esta registrado.")
        return

    nombre = input("Ingrese nombre del usuario: ")
    print(f"Géneros disponibles: {generos_disponibles}")
    generos_favoritos = set(input("Ingrese sus generos favoritos separados por coma: ").split(","))

    # Limpiar espacios y normalizar
    generos_favoritos = {g.strip().title() for g in generos_favoritos}

    # Actualizamos el conjunto global de generos con los nuevos
    generos_disponibles.update(generos_favoritos)

    usuarios[cedula] = {
        "nombre": nombre,
        "generos_favoritos": generos_favoritos,
        "historial": []  # lista de prestamos (codigos de libros)
    }
    print(f"✅ Usuario {nombre} registrado correctamente.")


# 2. Agregar libro al catalogo
def agregar_libro():
    global contador_libros
    titulo = input("Ingrese titulo del libro: ")
    autor = input("Ingrese autor del libro: ")
    genero = input("Ingrese genero del libro: ").title()

    if genero not in generos_disponibles:
        print("⚠️ El genero no estaba en la biblioteca, pero sera añadido a tus generos favoritos.")
        generos_disponibles.add(genero)

    libros[contador_libros] = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "disponible": True
    }

    print(f"✅ Libro '{titulo}' agregado con codigo {contador_libros}.")
    contador_libros += 1


# 3. Prestar libro
def prestar_libro():
    cedula = input("Ingrese cedula del usuario: ")
    if cedula not in usuarios:
        print("❌ Usuario no registrado.")
        return

    try:
        codigo = int(input("Ingrese codigo del libro: "))
        if codigo not in libros:
            print("❌ Libro no encontrado.")
            return

        if not libros[codigo]["disponible"]:
            print("❌ El libro ya está prestado.")
            return

        # Marcar como prestado
        libros[codigo]["disponible"] = False
        usuarios[cedula]["historial"].append(codigo)
        print(f"📚 {usuarios[cedula]['nombre']} ha tomado prestado '{libros[codigo]['titulo']}'.")

    except ValueError:
        print("❌ Codigo invalido, se esperaba una secuencia de numeros.")


# 4. Devolver libro
def devolver_libro():
    try:
        codigo = int(input("Ingrese código del libro a devolver: "))
        if codigo not in libros:
            print("❌ Libro no encontrado.")
            return

        if libros[codigo]["disponible"]:
            print("⚠️ Este libro ya no esta disponible en la biblioteca.")
            return

        libros[codigo]["disponible"] = True
        print(f"✅ Libro '{libros[codigo]['titulo']}' devuelto correctamente.")

    except ValueError:
        print("❌ Código inválido.")


# 5. Recomendar libros basados en géneros favoritos
def recomendar_libros():
    cedula = input("Ingrese cédula del usuario: ")
    if cedula not in usuarios:
        print("❌ Usuario no registrado.")
        return

    favoritos = usuarios[cedula]["generos_favoritos"]
    print(f"\n🎯 Recomendaciones para {usuarios[cedula]['nombre']} (géneros: {favoritos}):")

    recomendaciones = [
        datos for datos in libros.values()
        if datos["genero"] in favoritos and datos["disponible"]
    ]

    if recomendaciones:
        for libro in recomendaciones:
            print(f"- {libro['titulo']} ({libro['genero']}) de {libro['autor']}")
    else:
        print("❌  No hay recomendaciones disponibles en este momento.")


# 6. Análisis de usuarios
def analisis_usuarios():
    if len(usuarios) < 2:
        print("⚠️  Se necesitan al menos dos usuarios para el analisis.")
        return

    ced1 = input("Ingrese cedula del primer usuario: ")
    ced2 = input("Ingrese cedula del segundo usuario: ")

    if ced1 not in usuarios or ced2 not in usuarios:
        print("❌ Alguno de los usuarios no esta registrado.")
        return

    g1 = usuarios[ced1]["generos_favoritos"]
    g2 = usuarios[ced2]["generos_favoritos"]

    print(f"\n📊 Análisis entre {usuarios[ced1]['nombre']} y {usuarios[ced2]['nombre']}:")
    print(f"- Géneros en común: {g1 & g2}")
    print(f"- Géneros únicos: {g1 ^ g2}")
    print(f"- ¿{usuarios[ced1]['nombre']} tiene subconjunto de {usuarios[ced2]['nombre']}? {g1 <= g2}")
    print(f"- ¿{usuarios[ced2]['nombre']} tiene subconjunto de {usuarios[ced1]['nombre']}? {g2 <= g1}")

def salir():
    print("Salida del programa.👋 ")
    return

# ==============================
# main para ejecutar el menu
# ==============================
def main():
    isActive=True
    while isActive:
        clear_screen()
        opcion=menu()
        match opcion: 
            case "1":
                clear_screen()
                registrar_usuario()
                pause()
            case "2":
                clear_screen
                agregar_libro()
                pause()
            case "3":
                clear_screen()
                prestar_libro()
                pause()
            case "4":
                clear_screen()
                devolver_libro()
                pause()
            case "5":
                clear_screen()
                recomendar_libros()
                pause()
            case "6":
                clear_screen()
                analisis_usuarios()
                pause()
            case "7":
                    isActive=salir()
            case _:
                print("Opcion no encontrada. Intente de nuevo")
                pause()

# Ejecutar
if __name__ == "__main__":
    main()