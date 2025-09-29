import crud, utils
from messages import menu_text

def main():
    isActive=True
    while isActive:
        utils.clear_screen()
        opcion=input(menu_text()+"Seleccione una opcion entre (1-7): ")
        match opcion:
            case "1": utils.clear_screen(); crud.registrar_usuario(); utils.pause()
            case "2": utils.clear_screen(); crud.agregar_libro(); utils.pause()
            case "3": utils.clear_screen(); crud.prestar_libro(); utils.pause()
            case "4": utils.clear_screen(); crud.devolver_libro(); utils.pause()
            case "5": utils.clear_screen(); crud.recomendar_libros(); utils.pause()
            case "6": utils.clear_screen(); crud.analisis_usuarios(); utils.pause()
            case "7": isActive=crud.salir()
            case _: print("Opcion no encontrada. Intente de nuevo"); utils.pause()

if __name__=="__main__":
    main()
