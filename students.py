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

# ==============================
# Sistema de Gestión Académica
# ==============================

# Diccionario principal: {id_estudiante: {nombre, materias}}
estudiantes = {}

# Conjunto de materias disponibles
materias_disponibles = {"Matemáticas", "Física", "Química", "Historia", "Inglés"}


# 1. Registrar estudiante
def registrar_estudiante():
    id_est = input("Ingrese ID del estudiante: ")
    if id_est in estudiantes:
        print("❌ El estudiante ya está registrado.")
    else:
        nombre = input("Ingrese nombre del estudiante: ")
        estudiantes[id_est] = {
            "nombre": nombre,
            "materias": set(),  # conjunto de materias inscritas
            "calificaciones": {}  # {materia: [notas]}
        }
        print(f"✅ Estudiante {nombre} registrado con éxito.")


# 2. Agregar materias al conjunto disponible
def agregar_materia():
    materia = input("Ingrese nueva materia: ").capitalize()
    materias_disponibles.add(materia)
    print(f"✅ Materia '{materia}' añadida a las disponibles.")


# 3. Inscribir estudiante a materia
def inscribir_materia():
    id_est = input("ID del estudiante: ")
    if id_est not in estudiantes:
        print("❌ Estudiante no encontrado.")
        return

    print(f"Materias disponibles: {materias_disponibles}")
    materia = input("Ingrese materia a inscribir: ").capitalize()

    if materia in materias_disponibles:
        estudiantes[id_est]["materias"].add(materia)
        estudiantes[id_est]["calificaciones"].setdefault(materia, [])
        print(f"✅ {estudiantes[id_est]['nombre']} inscrito en {materia}.")
    else:
        print("❌ Materia no disponible.")


# 4. Registrar calificación
def registrar_calificacion():
    id_est = input("ID del estudiante: ")
    if id_est not in estudiantes:
        print("❌ Estudiante no encontrado.")
        return

    materia = input("Materia: ").capitalize()
    if materia not in estudiantes[id_est]["materias"]:
        print("❌ El estudiante no está inscrito en esta materia.")
        return

    try:
        nota = float(input("Ingrese calificación: "))
        estudiantes[id_est]["calificaciones"][materia].append(nota)
        print(f"✅ Nota {nota} registrada en {materia}.")
    except ValueError:
        print("❌ Calificación inválida.")


# 5. Ver materias comunes entre dos estudiantes
def materias_comunes():
    id1 = input("ID del primer estudiante: ")
    id2 = input("ID del segundo estudiante: ")

    if id1 not in estudiantes or id2 not in estudiantes:
        print("❌ Alguno de los estudiantes no existe.")
        return

    comunes = estudiantes[id1]["materias"] & estudiantes[id2]["materias"]
    print(f"📘 Materias comunes: {comunes if comunes else 'Ninguna'}")


# 6. Generar reporte académico
def generar_reporte():
    for id_est, datos in estudiantes.items():
        print("\n------------------------------------")
        print(f"📌 Estudiante: {datos['nombre']} (ID: {id_est})")
        if not datos["materias"]:
            print("No tiene materias inscritas.")
            continue

        for materia, notas in datos["calificaciones"].items():
            if notas:
                promedio = sum(notas) / len(notas)
                print(f"📖 {materia}: {notas} -> Promedio: {promedio:.2f}")
            else:
                print(f"📖 {materia}: Sin calificaciones registradas.")


# ==============================
# Menú principal
# ==============================
def menu():
    while True:
        print("\n===== SISTEMA ACADÉMICO =====")
        print("1. Registrar estudiante")
        print("2. Agregar materia disponible")
        print("3. Inscribir estudiante en materia")
        print("4. Registrar calificación")
        print("5. Ver materias comunes entre estudiantes")
        print("6. Generar reporte académico")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            agregar_materia()
        elif opcion == "3":
            inscribir_materia()
        elif opcion == "4":
            registrar_calificacion()
        elif opcion == "5":
            materias_comunes()
        elif opcion == "6":
            generar_reporte()
        elif opcion == "7":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()