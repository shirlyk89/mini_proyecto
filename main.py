import crud, utils
from messages import menu_text

def main():
    isActive=True
    while isActive:
        utils.clear_screen()
        print(menu_text())
        opcion=input("Seleccione una opción (1-7): ")
        match opcion:
            case '1': crud.agregar_libro(); utils.pause()
            case '2': crud.ver_biblioteca(); utils.pause()
            case '3': crud.buscar_libro(); utils.pause()
            case '4': crud.estado_lectura(); utils.pause()
            case '5': crud.ver_estadisticas(); utils.pause()
            case '6': crud.eliminar_libro(); utils.pause()
            case '7': isActive=crud.salir()
            case _: print("Error, intente de nuevo."); utils.pause()

if __name__=="__main__":
    main()
