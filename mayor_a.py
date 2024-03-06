import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

def filtrar_ventas(ventas, umbral):
    ventas_filtradas = {mes: valor for mes, valor in ventas.items() if valor > umbral}
    return ventas_filtradas

if len(sys.argv) != 2:
    print("\033[;31mUso: python mayor_a.py [umbral]\033[0m")
    sys.exit(1)

try:
    umbral = int(sys.argv[1])
except ValueError:
    print("\033[;31mEl umbral debe ser un número entero.\033[0m")
    sys.exit(1)

ventas_filtradas = filtrar_ventas(ventas, umbral)
print(ventas_filtradas)