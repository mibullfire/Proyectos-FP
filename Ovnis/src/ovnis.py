import csv
from collections import namedtuple
from datetime import *

Ovni = namedtuple('Ovni', 'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')
#Coordenada = namedtuple('Coordenada', 'latitude,longitude')
def parse_datetime(str):
    return datetime.strptime(str, '%m/%d/%Y %H:%M')

def leer_fichero(fichero):
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for datetime,city,state,shape,duration,comments,latitude,longitude in lector:
            res.append(Ovni(parse_datetime(datetime),city,state,shape,duration,comments,float(latitude),float(longitude)))
    return res

def numero_avistamientos_fecha(lista:list[Ovni], fecha:datetime.date)->int:
    return len([i for i in lista if i.datetime.date() == fecha])

def numero_avistamientos_fecha(lista:list, fecha:datetime.date)->int:
    return len([i for i in lista if i.fechahora.date() == fecha])

def formas_estados(lista:list, estados:set)->int:
    return len(set(i.forma for i in lista if i.estado in estados))

def duracion_total(lista:list, estado:str)->int:
    return sum(i.duracion for i in lista if i.estado == estado)

Cordenadas = namedtuple('Cordenadas', 'latitud, longitud')

import math

def distancia(punto1:Cordenadas, punto2:Cordenadas)->float:
    return float(math.sqrt((punto1.latitud - punto2.latitud)**2 + (punto1.longitud - punto2.longitud)**2))

punto1 = Cordenadas(0, 0)
punto2 = Cordenadas(40.1933333, -85.3863889)
print(distancia(punto1, punto2)<1000)  

def prueba(lista):
    return [Cordenadas(i.latitud, i.longitud) for i in lista][0]

def avistamientos_cercanos_ubicacion(lista:list, ubicacion:Cordenadas, distancia_max:float)->list:
    return [i for i in lista if distancia(Cordenadas(i.latitud, i.longitud), ubicacion) <= distancia_max]


def duracion_maxima(lista):
    return max(lista, key=lambda x: x.duracion)

def avistamiento_cercano_mayor_duracion(lista, ubicacion, distancia_max):
    return max(avistamientos_cercanos_ubicacion(lista, ubicacion, distancia_max), key=lambda x: x.duracion)

def avistamientos_fechas(lista, fecha1, fecha2):
    return [i for i in lista if fecha1 <= i.fechahora.date() <= fecha2]

def comentario_mas_largo(lista):
    return max(lista, key=lambda x: len(x.comentarios))

def media_dias_entre_avistamientos(lista):
    fechas = sorted([i.fechahora.date() for i in lista])
    return sum((fechas[i] - fechas[i-1]).days for i in range(1, len(fechas))) / (len(fechas) - 1)

def avistamientos_por_fecha(lista):
    return {i.fechahora.date(): len([j for j in lista if j.fechahora.date() == i.fechahora.date()]) for i in lista}

def formas_por_mes(lista):
    return {i: len([j for j in lista if j.fechahora.month == i]) for i in range(1, 13)}