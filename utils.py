from collections import Counter
from datetime import datetime

# ---------- Datos compartidos -----------
inventario: dict[int, dict] = {}
clientes: dict[str, dict] = {}
empleados: list[tuple] = []
plataformas: set[str] = {"PC", "PS5", "Xbox", "Switch"}
generos: set[str] = {"Acción", "Aventura", "RPG", "Indie", "Deportes", "Simulación"}
clientes_vip: set[str] = set()
ventas: list[tuple] = []

# Contadores (se usan como 'mutable globals' dentro de funciones que declaran global)
contador_producto = 1
contador_empleado = 1
contador_venta = 1

# Helpers
def employees_iter():
    for emp in empleados:
        yield emp

def now_iso():
    return datetime.now().isoformat(timespec="seconds")

def format_money(x: float) -> str:
    return f"${x:.2f}"
