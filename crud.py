from utils import inventario, plataformas, generos, clientes, clientes_vip, empleados, ventas, contador_producto, contador_empleado, contador_venta, employees_iter, now_iso, format_money
import utils

# ---------- Inventario ----------
def agregar_producto():
    global contador_producto
    try:
        titulo = input("Título del juego: ").strip()
        plataforma = input(f"Plataforma ({', '.join(sorted(plataformas))}): ").strip().title()
        genero = input(f"Género ({', '.join(sorted(generos))}): ").strip().capitalize()
        precio = float(input("Precio (USD): "))
        stock = int(input("Stock inicial (unidades): "))
    except Exception as e:
        print("⚠️ Entrada inválida.", e)
        return
    plataformas.add(plataforma)
    generos.add(genero)
    producto = (utils.contador_producto, titulo, plataforma, genero)
    inventario[utils.contador_producto] = {"producto": producto, "precio": precio, "stock": stock}
    print(f"✅ Producto agregado: ID {utils.contador_producto} -> {titulo} ({plataforma} / {genero})")
    utils.contador_producto += 1

def ver_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    print("ID | Título | Plataforma | Género | Precio | Stock")
    print("-" * 70)
    for codigo, info in inventario.items():
        prod = info["producto"]
        print(f"{codigo} | {prod[1]:30.30} | {prod[2]:7} | {prod[3]:10} | {format_money(info['precio']):7} | {info['stock']}")

def actualizar_stock():
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
    print(f"Precio actualizado: {format_money(nuevo_precio)}")

# ---------- Clientes ----------
def registrar_cliente():
    dni = input("DNI del cliente: ").strip()
    if dni in clientes:
        print("Cliente ya registrado.")
        return
    nombre = input("Nombre del cliente: ").strip()
    clientes[dni] = {"nombre": nombre, "compras": [], "vip": False}
    print(f"✅ Cliente {nombre} registrado con DNI {dni}.")

def marcar_vip():
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
    if not clientes:
        print("No hay clientes registrados.")
        return
    for i, (dni, data) in enumerate(clientes.items(), 1):
        vip_text = "VIP" if data["vip"] else "regular"
        print(f"{i}. {data['nombre']} (DNI: {dni}) - {vip_text} - Compras: {len(data['compras'])}")

# ---------- Empleados ----------
def agregar_empleado():
    nombre = input("Nombre del empleado: ").strip()
    rol = input("Rol (vendedor/administrador): ").strip().lower()
    empleado = (utils.contador_empleado, nombre, rol)
    empleados.append(empleado)
    print(f"✅ Empleado agregado ID {utils.contador_empleado}: {nombre} ({rol})")
    utils.contador_empleado += 1

def listar_empleados():
    if not empleados:
        print("No hay empleados.")
        return
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. ID: {emp[0]} | {emp[1]} | Rol: {emp[2]}")

# ---------- Ventas ----------
def crear_venta():
    if not clientes:
        print("No hay clientes registrados.")
        return
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
    if not any(emp[0] == empleado_id for emp in employees_iter()):
        print("Empleado no encontrado.")
        return
    carrito = []
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
    subtotal = sum(inventario[c]['precio'] * q for c, q in carrito)
    descuento = 0.0
    if clientes[dni]["vip"]:
        descuento = subtotal * 0.10
        print(f"Aplicando descuento VIP 10%: -{format_money(descuento)}")
    total = subtotal - descuento
    print(f"Subtotal: {format_money(subtotal)} | Descuento: {format_money(descuento)} | Total: {format_money(total)}")
    confirmar = input("Confirmar venta? (s/n): ").lower()
    if confirmar != "s":
        print("Venta cancelada.")
        return
    for codigo, cantidad in carrito:
        inventario[codigo]["stock"] -= cantidad
    items_tuple = tuple((codigo, cantidad, inventario[codigo]["precio"]) for codigo, cantidad in carrito)
    tx_id = utils.contador_venta
    fecha = now_iso()
    transaccion = (tx_id, fecha, dni, empleado_id, items_tuple, total)
    ventas.append(transaccion)
    clientes[dni]["compras"].append(tx_id)
    utils.contador_venta += 1
    print(f"✅ Venta registrada ID {tx_id}. Total {format_money(total)}")

def ver_ventas():
    if not ventas:
        print("No hay ventas registradas.")
        return
    for tx in ventas:
        print(f"ID:{tx[0]} Fecha:{tx[1]} Cliente:{tx[2]} EmpleadoID:{tx[3]} Total:{format_money(tx[5])}")
        for item in tx[4]:
            codigo, cantidad, precio = item
            titulo = inventario.get(codigo, {}).get("producto", (None, "Desconocido"))[1]
            print(f"  - {titulo} (ID {codigo}) x{cantidad} @{format_money(precio)}")

def reembolsar_venta():
    try:
        tx_id = int(input("ID de venta a reembolsar: "))
    except ValueError:
        print("ID inválido.")
        return
    tx = next((t for t in ventas if t[0] == tx_id), None)
    if tx is None:
        print("Venta no encontrada.")
        return
    for item in tx[4]:
        codigo, cantidad, _ = item
        if codigo in inventario:
            inventario[codigo]["stock"] += cantidad
    ventas.remove(tx)
    dni = tx[2]
    if dni in clientes and tx_id in clientes[dni]["compras"]:
        clientes[dni]["compras"].remove(tx_id)
    print(f"✅ Venta {tx_id} reembolsada y stock actualizado.")

# ---------- Reportes ----------
def reporte_ventas_totales():
    if not ventas:
        print("No hay datos de ventas.")
        return
    ventas_por_dia = {}
    for tx in ventas:
        fecha_dia = tx[1].split("T")[0]
        ventas_por_dia.setdefault(fecha_dia, 0.0)
        ventas_por_dia[fecha_dia] += tx[5]
    print("Ventas por día:")
    for dia, total in ventas_por_dia.items():
        print(f" {dia}: {format_money(total)}")
    from collections import Counter
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
    print("Productos con stock bajo:")
    for codigo, info in inventario.items():
        if info["stock"] <= min_stock:
            prod = info["producto"]
            print(f"ID {codigo} - {prod[1]} | Stock: {info['stock']}")

def reporte_cliente(dni=None):
    if dni is None:
        dni = input("DNI del cliente para reporte: ").strip()
    if dni not in clientes:
        print("Cliente no encontrado.")
        return
    data = clientes[dni]
    print(f"Reporte de {data['nombre']} (DNI {dni})")
    print(f"Compras realizadas (IDs): {data['compras']}")
    total_gastado = sum(tx[5] for tx in ventas if tx[2] == dni)
    print(f"Total gastado: {format_money(total_gastado)}")

def analisis_plataformas_y_generos():
    plataformas_inv = {info["producto"][2] for info in inventario.values()}
    generos_inv = {info["producto"][3] for info in inventario.values()}
    print(f"Plataformas en inventario: {plataformas_inv}")
    print(f"Géneros en inventario: {generos_inv}")
    comunes = plataformas & plataformas_inv
    union_gen = generos | generos_inv
    diferencia = generos_inv - generos
    simetrica = generos ^ generos_inv
    print(f"Intersección plataformas definidas ∧ inventario: {comunes}")
    print(f"Unión géneros definidos ∪ inventario: {union_gen}")
    print(f"Diferencia (inventario - definidos): {diferencia}")
    print(f"Diferencia simétrica géneros ^ inventario: {simetrica}")
