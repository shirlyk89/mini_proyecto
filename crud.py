from utils import estudiantes, materias_disponibles

def registrar_estudiante():
    id_est = input("Ingrese ID del estudiante: ")
    if id_est in estudiantes:
        print("❌ El estudiante ya está registrado.")
    else:
        nombre = input("Ingrese nombre del estudiante: ")
        estudiantes[id_est] = {
            "nombre": nombre,
            "materias": set(),
            "calificaciones": {}
        }
        print(f"✅ Estudiante {nombre} registrado con éxito.")

def agregar_materia():
    materia = input("Ingrese nueva materia: ").capitalize()
    materias_disponibles.add(materia)
    print(f"✅ Materia '{materia}' añadida a las disponibles.")

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

def materias_comunes():
    id1 = input("ID del primer estudiante: ")
    id2 = input("ID del segundo estudiante: ")
    if id1 not in estudiantes or id2 not in estudiantes:
        print("❌ Alguno de los estudiantes no existe.")
        return
    comunes = estudiantes[id1]["materias"] & estudiantes[id2]["materias"]
    print(f"📘 Materias comunes: {comunes if comunes else 'Ninguna'}")

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

def salir():
    print("👋 Saliendo del sistema...")
    return False
