from typing import NamedTuple, List
from datetime import date, datetime
import csv
from typing import *
from collections import defaultdict

Reserva = NamedTuple("Reserva",
    [("nombre", str),
    ("dni", str),
    ("fecha_entrada", date),
    ("fecha_salida", date),
    ("tipo_habitacion", str),
    ("num_personas", int),
    ("precio_noche", float),
    ("servicios_adicionales", List[str])
    ])

def parse_servicios_adicionales(servicios:str)->List[str]:
    # "Parking,Gimnasio,Spa"
    return servicios.strip().split(",")

def parse_fecha(fecha:str)->date:
    # "2021-08-01"
    return datetime.strptime(fecha, "%Y-%m-%d").date()

def total_dias(fecha_ini: date, fecha_fin: date) -> int:
    return (fecha_fin - fecha_ini).days

def lee_reservas(fichero:str)->list[Reserva]:
    res = []
    with open(fichero, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_no, servicios_adicionales in reader:
            res.append(Reserva(nombre,dni,parse_fecha(fecha_entrada),parse_fecha(fecha_salida),tipo_habitacion,int(num_personas),float(precio_no),parse_servicios_adicionales(servicios_adicionales)))
    return res


def total_facturado(reservas: List[Reserva], fecha_ini: Optional[date] = None, fecha_fin: Optional[date] = None) -> float:
    return sum([i.precio_noche * total_dias(i.fecha_entrada, i.fecha_salida) for i in reservas if (fecha_ini == None or i.fecha_entrada >= fecha_ini) and (fecha_fin == None or i.fecha_salida <= fecha_fin)])

def reservas_mas_largas(reservas:List[Reserva],n:int = 3) -> List[Tuple[str, date]]:
    reservas = sorted(reservas, key = lambda x: total_dias(x.fecha_entrada, x.fecha_salida), reverse=True)
    return [(i.nombre, i.fecha_entrada) for i in reservas][:n]

def cliente_mayor_facturacion(reservas: List[Reserva], servicios: Optional[Set[str]] = None) -> Tuple[str, float]:
    diccionario = defaultdict(float)
    for i in reservas:
        if servicios is None or any(servicio in i.servicios_adicionales for servicio in servicios):
            diccionario[i.dni] += i.precio_noche * total_dias(i.fecha_entrada, i.fecha_salida)
    if diccionario:
        return max(diccionario.items(), key=lambda x: x[1])
    else:
        return ("", 0.0)
