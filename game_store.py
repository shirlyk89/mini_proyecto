# tienda_videojuegos.py
# Requiere Python 3.10+ (match/case)

from collections import Counter
from datetime import datetime

# -------------------------
# Estructuras principales
# -------------------------
# Inventario: {codigo: {"producto": (id, titulo, plataforma, genero), "precio": float, "stock": int}}
# dentro del diccionario inventario la claves es un entero "int" y el valor es otro diccionario "dic()"
inventario: dict[int, dict] = {}

# Clientes: {dni: {"nombre": str, "compras": [], "vip": bool}}
clientes: dict[str, dict] = {}

# Empleados: lista de tuplas inmutables (id_empleado, nombre, rol)
empleados: list[tuple] = []

# Conjuntos
plataformas: set[str] = {"PC", "PS5", "Xbox", "Switch"}
generos: set[str] = {"Acción", "Aventura", "RPG", "Indie", "Deportes", "Simulación"}

clientes_vip: set[str] = set()  # DNIs VIP

# Historial de ventas: lista de transacciones (tuplas inmutables)
# transaccion = (tx_id, fecha_iso, dni_cliente, empleado_id, items_tuple, total)
ventas: list[tuple] = []

# Contadores
contador_producto = 1
contador_empleado = 1
contador_venta = 1

# -----------------------------------
# Funciones de inventario y productos
# -----------------------------------
def agregar_producto():
    """Agregar un nuevo producto (tupla inmutable) al inventario."""
    global contador_producto
    titulo = input("Título del juego: ").strip()
    plataforma = input(f"Plataforma ({', '.join(sorted(plataformas))}): ").strip().title()
    genero = input(f"Género ({', '.join(sorted(generos))}): ").strip().capitalize()
    try:
        precio = float(input("Precio (USD): "))
        stock = int(input("Stock inicial (unidades): "))
    except ValueError:
        print("⚠️ Precio o stock inválido.")
        return

    # Normalizar conjuntos si aparecen géneros/plataformas nuevos
    plataformas.add(plataforma)
    generos.add(genero)

    producto = (contador_producto, titulo, plataforma, genero)  # tuple (inmutable)
    inventario[contador_producto] = {"producto": producto, "precio": precio, "stock": stock}
    print(f"✅ Producto agregado: ID {contador_producto} -> {titulo} ({plataforma} / {genero})")
    contador_producto += 1

def ver_inventario():
    """Mostrar inventario formateado (usa enumerate)."""
    if not inventario:
        print("El inventario está vacío.")
        return
    print("ID | Título | Plataforma | Género | Precio | Stock")
    print("-" * 70)
    for codigo, info in inventario.items():
        prod = info["producto"]
        print(f"{codigo} | {prod[1]:30.30} | {prod[2]:7} | {prod[3]:10} | ${info['precio']:7.2f} | {info['stock']}")

def actualizar_stock():
    """Aumentar o disminuir stock (validar)."""
    try:
        codigo = int(input("Código del producto: "))
        if codigo not in inventario:
            print("Código no encontrado.")
            return
        delta = int(input("Ingrese cantidad a añadir (+) o retirar (-): "))
    except ValueError:
        print("Entrada numérica inválida.")
        return

    nuevo = inventario[codigo]["stock"] + delta
    if nuevo < 0:
        print("No puedes dejar stock negativo.")
        return
    inventario[codigo]["stock"] = nuevo
    print(f"Stock actualizado. Nuevo stock: {inventario[codigo]['stock']}")

def actualizar_precio():
    """Actualizar precio de un producto (validar)."""
    try:
        codigo = int(input("Código del producto: "))
        if codigo not in inventario:
            print("Código no encontrado.")
            return
        nuevo_precio = float(input("Nuevo precio: "))
    except ValueError:
        print("Entrada inválida.")
        return
    inventario[codigo]["precio"] = nuevo_precio
    print(f"Precio actualizado: ${nuevo_precio:.2f}")

# ---------------------------
# Funciones de clientes
# ---------------------------
def registrar_cliente():
    """Registrar cliente (dni único)."""
    dni = input("DNI del cliente: ").strip()
    if dni in clientes:
        print("Cliente ya registrado.")
        return
    nombre = input("Nombre del cliente: ").strip()
    clientes[dni] = {"nombre": nombre, "compras": [], "vip": False}
    print(f"✅ Cliente {nombre} registrado con DNI {dni}.")

def marcar_vip():
    """Marcar o desmarcar cliente VIP (uso de conjuntos)."""
    dni = input("DNI del cliente: ").strip()
    if dni not in clientes:
        print("Cliente no encontrado.")
        return
    accion = input("Marcar VIP? (s/n): ").lower()
    if accion == "s":
        clientes[dni]["vip"] = True
        clientes_vip.add(dni)
        print(f"{clientes[dni]['nombre']} ahora es VIP.")
    else:
        clientes[dni]["vip"] = False
        clientes_vip.discard(dni)
        print(f"{clientes[dni]['nombre']} ya no es VIP.")

def ver_clientes():
    """Ver clientes (usa enumerate)."""
    if not clientes:
        print("No hay clientes registrados.")
        return
    for i, (dni, data) in enumerate(clientes.items(), 1):
        vip_text = "VIP" if data["vip"] else "regular"
        print(f"{i}. {data['nombre']} (DNI: {dni}) - {vip_text} - Compras: {len(data['compras'])}")

# ---------------------------
# Funciones de empleados
# ---------------------------
def agregar_empleado():
    """Agregar empleado como tupla inmutable y añadir a la lista."""
    global contador_empleado
    nombre = input("Nombre del empleado: ").strip()
    rol = input("Rol (vendedor/administrador): ").strip().lower()
    empleado = (contador_empleado, nombre, rol)  # tupla inmutable
    empleados.append(empleado)
    print(f"✅ Empleado agregado ID {contador_empleado}: {nombre} ({rol})")
    contador_empleado += 1

def listar_empleados():
    """Listar empleados (usa enumerate)."""
    if not empleados:
        print("No hay empleados.")
        return
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. ID: {emp[0]} | {emp[1]} | Rol: {emp[2]}")

# ---------------------------
# Funciones de ventas
# ---------------------------
def crear_venta():
    """Crear venta: seleccionar cliente, empleado, items; controlar stock y calcular total."""
    global contador_venta
    dni = input("DNI del cliente: ").strip()
    if dni not in clientes:
        print("Cliente no registrado.")
        return
    if not empleados:
        print("No hay empleados registrados.")
        return

    try:
        empleado_id = int(input("ID del empleado que atiende: "))
    except ValueError:
        print("ID inválido.")
        return
    # verificar empleado existe por buscando en empleados
    if not any(emp[0] == empleado_id for emp in employees_iter()):
        print("Empleado no encontrado.")
        return

    carrito: list[tuple[int, int]] = []  # list of (codigo, cantidad)
    while True:
        ver_inventario()
        try:
            codigo = int(input("Código a añadir (0 para terminar): "))
        except ValueError:
            print("Entrada inválida.")
            continue
        if codigo == 0:
            break
        if codigo not in inventario:
            print("Código no existe.")
            continue
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad inválida.")
            continue
        if cantidad <= 0:
            print("Cantidad debe ser positiva.")
            continue
        if inventario[codigo]["stock"] < cantidad:
            print("Stock insuficiente.")
            continue
        carrito.append((codigo, cantidad))

    if not carrito:
        print("Carrito vacío, venta cancelada.")
        return

    # Calcular total y aplicar descuento si VIP
    subtotal = 0.0
    for codigo, cantidad in carrito:
        subtotal += inventario[codigo]["precio"] * cantidad

    descuento = 0.0
    if clientes[dni]["vip"]:
        descuento = subtotal * 0.10  # 10% para VIP
        print(f"Aplicando descuento VIP 10%: -${descuento:.2f}")

    total = subtotal - descuento

    # Confirmar venta
    print(f"Subtotal: ${subtotal:.2f} | Descuento: ${descuento:.2f} | Total: ${total:.2f}")
    confirmar = input("Confirmar venta? (s/n): ").lower()
    if confirmar != "s":
        print("Venta cancelada.")
        return

    # Reducir stock y registrar transacción
    for codigo, cantidad in carrito:
        inventario[codigo]["stock"] -= cantidad

    # crear items inmutables para la transacción
    items_tuple = tuple((codigo, cantidad, inventario[codigo]["precio"]) for codigo, cantidad in carrito)
    tx_id = contador_venta
    fecha = datetime.now().isoformat(timespec="seconds")
    transaccion = (tx_id, fecha, dni, empleado_id, items_tuple, total)  # tupla inmutable
    ventas.append(transaccion)
    clientes[dni]["compras"].append(tx_id)
    contador_venta += 1
    print(f"✅ Venta registrada ID {tx_id}. Total ${total:.2f}")

def employees_iter():
    """Helper generator to iterate empleados cleanly (returns tuples)."""
    for emp in empleados:
        yield emp

def ver_ventas():
    """Mostrar historial de ventas (tuplas)."""
    if not ventas:
        print("No hay ventas registradas.")
        return
    for tx in ventas:
        print(f"ID:{tx[0]} Fecha:{tx[1]} Cliente:{tx[2]} EmpleadoID:{tx[3]} Total:${tx[5]:.2f}")
        for item in tx[4]:
            codigo, cantidad, precio = item
            titulo = inventario.get(codigo, {}).get("producto", (None, "Desconocido"))[1]
            print(f"  - {titulo} (ID {codigo}) x{cantidad} @${precio:.2f}")

def reembolsar_venta():
    """Reembolsar (simple): buscar venta por ID y revertir stock y registros."""
    try:
        tx_id = int(input("ID de venta a reembolsar: "))
    except ValueError:
        print("ID inválido.")
        return
    tx = next((t for t in ventas if t[0] == tx_id), None)
    if tx is None:
        print("Venta no encontrada.")
        return
    # revertir stock
    for item in tx[4]:
        codigo, cantidad, _ = item
        if codigo in inventario:
            inventario[codigo]["stock"] += cantidad
    ventas.remove(tx)
    # quitar de historial cliente si existe
    dni = tx[2]
    if dni in clientes and tx_id in clientes[dni]["compras"]:
        clientes[dni]["compras"].remove(tx_id)
    print(f"✅ Venta {tx_id} reembolsada y stock actualizado.")

# ---------------------------
# Reportes y análisis
# ---------------------------
def reporte_ventas_totales():
    """Reporte: totales por día y top vendedores (empleado)."""
    if not ventas:
        print("No hay datos de ventas.")
        return
    # agrupar por fecha (día)
    ventas_por_dia: dict[str, float] = {}
    for tx in ventas:
        fecha_dia = tx[1].split("T")[0]
        ventas_por_dia.setdefault(fecha_dia, 0.0)
        ventas_por_dia[fecha_dia] += tx[5]
    print("Ventas por día:")
    for dia, total in ventas_por_dia.items():
        print(f" {dia}: ${total:.2f}")

    # top productos
    contador_prod = Counter()
    for tx in ventas:
        for item in tx[4]:
            codigo, cantidad, _ = item
            contador_prod[codigo] += cantidad
    print("\nTop productos vendidos:")
    for codigo, qty in contador_prod.most_common(5):
        titulo = inventario.get(codigo, {}).get("producto", (None, "Desconocido"))[1]
        print(f" {titulo} (ID {codigo}) - {qty} unidades")

def reporte_inventario_bajo(min_stock=3):
    """Reporte de productos con stock bajo (comparación)."""
    print("Productos con stock bajo:")
    for codigo, info in inventario.items():
        if info["stock"] <= min_stock:
            prod = info["producto"]
            print(f"ID {codigo} - {prod[1]} | Stock: {info['stock']}")

def reporte_cliente(dni=None):
    """Reporte por cliente: historial y gasto total."""
    if dni is None:
        dni = input("DNI del cliente para reporte: ").strip()
    if dni not in clientes:
        print("Cliente no encontrado.")
        return
    data = clientes[dni]
    print(f"Reporte de {data['nombre']} (DNI {dni})")
    print(f"Compras realizadas (IDs): {data['compras']}")
    total_gastado = sum(tx[5] for tx in ventas if tx[2] == dni)
    print(f"Total gastado: ${total_gastado:.2f}")

def analisis_plataformas_y_generos():
    """Análisis con conjuntos: plataformas, géneros, intersecciones, uniones, diferencias."""
    # conjuntos desde inventario
    plataformas_inv = {info["producto"][2] for info in inventario.values()}
    generos_inv = {info["producto"][3] for info in inventario.values()}
    print(f"Plataformas en inventario: {plataformas_inv}")
    print(f"Géneros en inventario: {generos_inv}")

    # ejemplo de operaciones de conjuntos
    comunes = plataformas & plataformas_inv
    union_gen = generos | generos_inv
    diferencia = generos_inv - generos
    simetrica = generos ^ generos_inv
    print(f"Intersección plataformas definidas ∧ inventario: {comunes}")
    print(f"Unión géneros definidos ∪ inventario: {union_gen}")
    print(f"Diferencia (inventario - definidos): {diferencia}")
    print(f"Diferencia simétrica géneros ^ inventario: {simetrica}")

# ---------------------------
# Menús (match-case) y main
# ---------------------------
def menu_principal():
    while True:
        print("\n=== TIENDA DE VIDEOJUEGOS ===")
        print("1. Inventario")
        print("2. Clientes")
        print("3. Empleados")
        print("4. Ventas")
        print("5. Reportes")
        print("6. Análisis plataformas/géneros")
        print("7. Salir")
        opt = input("Seleccione opción: ").strip()
        match opt:
            case "1":
                submenu_inventario()
            case "2":
                submenu_clientes()
            case "3":
                submenu_empleados()
            case "4":
                submenu_ventas()
            case "5":
                submenu_reportes()
            case "6":
                analisis_plataformas_y_generos()
            case "7":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida.")

# Submenús (más match-case)
def submenu_inventario():
    while True:
        print("\n--- INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Actualizar stock")
        print("4. Actualizar precio")
        print("5. Volver")
        opt = input("opción: ").strip()
        match opt:
            case "1":
                agregar_producto()
            case "2":
                ver_inventario()
            case "3":
                actualizar_stock()
            case "4":
                actualizar_precio()
            case "5":
                break
            case _:
                print("Opción inválida.")

def submenu_clientes():
    while True:
        print("\n--- CLIENTES ---")
        print("1. Registrar cliente")
        print("2. Ver clientes")
        print("3. Marcar/desmarcar VIP")
        print("4. Volver")
        opt = input("opción: ").strip()
        match opt:
            case "1":
                registrar_cliente()
            case "2":
                ver_clientes()
            case "3":
                marcar_vip()
            case "4":
                break
            case _:
                print("Opción inválida.")

def submenu_empleados():
    while True:
        print("\n--- EMPLEADOS ---")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Volver")
        opt = input("opción: ").strip()
        match opt:
            case "1":
                agregar_empleado()
            case "2":
                listar_empleados()
            case "3":
                break
            case _:
                print("Opción inválida.")

def submenu_ventas():
    while True:
        print("\n--- VENTAS ---")
        print("1. Crear venta")
        print("2. Ver ventas")
        print("3. Reembolsar venta")
        print("4. Volver")
        opt = input("opción: ").strip()
        match opt:
            case "1":
                crear_venta()
            case "2":
                ver_ventas()
            case "3":
                reembolsar_venta()
            case "4":
                break
            case _:
                print("Opción inválida.")

def submenu_reportes():
    while True:
        print("\n--- REPORTES ---")
        print("1. Ventas totales y top productos")
        print("2. Inventario bajo")
        print("3. Reporte por cliente")
        print("4. Volver")
        opt = input("opción: ").strip()
        match opt:
            case "1":
                reporte_ventas_totales()
            case "2":
                reporte_inventario_bajo()
            case "3":
                reporte_cliente()
            case "4":
                break
            case _:
                print("Opción inválida.")

# Ejecutar si es main
if __name__ == "__main__":
    # precarga de ejemplo (opcional)
    inventario[1] = {"producto": (1, "Hollow Knight", "PC", "Indie"), "precio": 14.99, "stock": 10}
    inventario[2] = {"producto": (2, "God of War", "PS5", "Acción"), "precio": 59.99, "stock": 5}
    inventario[3] = {"producto": (3, "Forza Horizon", "Xbox", "Deportes"), "precio": 49.99, "stock": 2}
    plataformas.update({"PC", "PS5", "Xbox"})
    generos.update({"Indie", "Acción", "Deportes"})
    menu_principal()