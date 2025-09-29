import crud
from messages import menu_text

def main():
    isActive = True
    while isActive:
        print(menu_text())
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1": crud.registrar_estudiante()
            case "2": crud.agregar_materia()
            case "3": crud.inscribir_materia()
            case "4": crud.registrar_calificacion()
            case "5": crud.materias_comunes()
            case "6": crud.generar_reporte()
            case "7": isActive = crud.salir()
            case _: print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
