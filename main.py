from messages import *
import crud, utils

def submenu_inventario():
    while True:
        print(submenu_inventario_text())
        opt = input("opción: ").strip()
        match opt:
            case "1": crud.agregar_producto()
            case "2": crud.ver_inventario()
            case "3": crud.actualizar_stock()
            case "4": crud.actualizar_precio()
            case "5": break
            case _: print("Opción inválida.")

def submenu_clientes():
    while True:
        print(submenu_clientes_text())
        opt = input("opción: ").strip()
        match opt:
            case "1": crud.registrar_cliente()
            case "2": crud.ver_clientes()
            case "3": crud.marcar_vip()
            case "4": break
            case _: print("Opción inválida.")

def submenu_empleados():
    while True:
        print(submenu_empleados_text())
        opt = input("opción: ").strip()
        match opt:
            case "1": crud.agregar_empleado()
            case "2": crud.listar_empleados()
            case "3": break
            case _: print("Opción inválida.")

def submenu_ventas():
    while True:
        print(submenu_ventas_text())
        opt = input("opción: ").strip()
        match opt:
            case "1": crud.crear_venta()
            case "2": crud.ver_ventas()
            case "3": crud.reembolsar_venta()
            case "4": break
            case _: print("Opción inválida.")

def submenu_reportes():
    while True:
        print(submenu_reportes_text())
        opt = input("opción: ").strip()
        match opt:
            case "1": crud.reporte_ventas_totales()
            case "2": crud.reporte_inventario_bajo()
            case "3": crud.reporte_cliente()
            case "4": break
            case _: print("Opción inválida.")

def menu_principal():
    while True:
        print(menu_principal_text())
        opt = input("Seleccione opción: ").strip()
        match opt:
            case "1": submenu_inventario()
            case "2": submenu_clientes()
            case "3": submenu_empleados()
            case "4": submenu_ventas()
            case "5": submenu_reportes()
            case "6": crud.analisis_plataformas_y_generos()
            case "7": print("Saliendo..."); break
            case _: print("Opción inválida.")

if __name__ == "__main__":
    # Precarga de ejemplo
    utils.inventario[1] = {"producto": (1, "Hollow Knight", "PC", "Indie"), "precio": 14.99, "stock": 10}
    utils.inventario[2] = {"producto": (2, "God of War", "PS5", "Acción"), "precio": 59.99, "stock": 5}
    utils.inventario[3] = {"producto": (3, "Forza Horizon", "Xbox", "Deportes"), "precio": 49.99, "stock": 2}
    utils.plataformas.update({"PC", "PS5", "Xbox"})
    utils.generos.update({"Indie", "Acción", "Deportes"})
    menu_principal()
