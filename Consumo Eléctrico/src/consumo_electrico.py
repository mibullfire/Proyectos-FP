from typing import *
from datetime import date, datetime
import csv
from collections import defaultdict

IntervaloFechas = NamedTuple("IntervaloFechas",
        [("inicio", date), ("fin", date)])

Factura = NamedTuple("Factura",
        [("id_vivienda", str),
        ("tipo_vivienda", str),
        ("barrio", str),
        ("tipo_tarifa", str),
        ("periodo_facturado", IntervaloFechas),
        ("coste_potencia", float),
        ("consumo_punta", float),
        ("consumo_valle", float),
        ("precio_punta", float),
        ("precio_valle", float),
        ("importe_total", float)])

def lee_facturas(ruta_fichero: str) -> List[Factura]:
    res = []

    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for ID_Vivienda,Tipo_Vivienda,Barrio,Tipo_Tarifa,Periodo_Inicio,Periodo_Fin,Coste_Potencia_EUR,Consumo_Punta_kWh,Consumo_Valle_kWh,Precio_kWh,Importe_Total_EUR in lector:
            if Tipo_Tarifa != 'tramos':
                precio_punta = Precio_kWh
                precio_valle = Precio_kWh
            else:
                precio_punta, precio_valle = Precio_kWh.split('/')
            res.append(Factura(ID_Vivienda,Tipo_Vivienda,Barrio,Tipo_Tarifa,IntervaloFechas(datetime.strptime(Periodo_Inicio, '%Y-%m-%d'),datetime.strptime(Periodo_Fin, '%Y-%m-%d')),float(Coste_Potencia_EUR),float(Consumo_Punta_kWh),float(Consumo_Valle_kWh),float(precio_punta),float(precio_valle),float(Importe_Total_EUR)))
        
    return res

def extrae_precio_por_mes(facturas: List[Factura], tipo_tarifa: str) -> Dict[str, Tuple[float, float]]:
    res = {}
    for i in facturas:
        if i.tipo_tarifa == tipo_tarifa:
            res[date.strftime(i.periodo_facturado.inicio, '%Y-%m')] = (i.precio_punta, i.precio_valle)
    return res

def busca_vivienda_mayor_consumo_acumulado(facturas: List[Factura]) -> Tuple[str, float]:
    aux_dicc = defaultdict(float)
    for i in facturas:
        consumo = i.consumo_punta + i.consumo_valle
        aux_dicc[i.id_vivienda] += consumo
    return max(aux_dicc.items(), key = lambda x: x[1])

def barrios_mayor_consumo_valle_medio(facturas: List[Factura], top_n: int) -> List[str]:
    aux_dicc = defaultdict(list)
    for i in facturas:
        aux_dicc[i.barrio].append(i.consumo_valle)
    dicc = {
        i: sum(j)/len(j) for i, j in aux_dicc.items()
    }
    lista = sorted(dicc.items(), key = lambda x: x[1], reverse = True)
    return [x[0] for x in lista][:top_n]

def compara_importe_tipos_factura(facturas: List[Factura], id_vivienda: str) -> Optional[Tuple[str, float, float]]:
    facturas_id = [i for i in facturas if i.id_vivienda == id_vivienda]
    tipo = facturas_id[0][3]
    pagado = []
    pagaria = []
    
    for i in facturas_id:
        if tipo == 'única':
            res = 'única->tramos'
            pagado.append(i.importe_total)
            pagaria.append(i.coste_potencia + i.consumo_punta * i.precio_punta + i.consumo_valle * i.precio_valle)
        if tipo == 'tramos':
            res = 'tramos->única'
            pagado.append(i.importe_total)
            pagaria.append(i.coste_potencia + (i.consumo_punta + i.consumo_valle) * i.precio_punta)

    return (res, sum(pagado), sum(pagaria))

def busca_cambios_beneficiosos(facturas: List[Factura]) -> List[Tuple[str, int, float]]:
    aux_dicc = {}
    for i in facturas:
        aux_dicc[i.id_vivienda] = (compara_importe_tipos_factura(facturas, i.id_vivienda))
    
    res = list(aux_dicc.values())

    return res

def calcula_mes_incremento_maximo_consumo_acumulado(facturas: List[Factura], tipo_vivienda: Optional[str] = None) -> Tuple[str, float]:
    pass