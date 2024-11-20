import csv
from collections import namedtuple, Counter, defaultdict
from datetime import *
from typing import Optional

Ovni = namedtuple('Ovni', 'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')
#Coordenada = namedtuple('Coordenada', 'latitude,longitude')
def parse_datetime(str):
    return datetime.strptime(str, '%m/%d/%Y %H:%M')

# 1. Función de lectura de datos
def leer_fichero(fichero):
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for datetime,city,state,shape,duration,comments,latitude,longitude in lector:
            res.append(Ovni(parse_datetime(datetime),city,state,shape,int(duration),comments,float(latitude),float(longitude)))
    return res

# 2. Operaciones de filtrado, conteo y suma
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

# 3. Operaciones con máximos, mínimos y ordenación
def avistamiento_mayor_duracion(lista:list, forma:Optional[str]=None)->Ovni:
    return max([i for i in lista if (forma == None or i.forma == forma)], key = lambda x: x.duracion)

def avistamiento_cercano_mayor_duracion(lista, ubicacion, distancia_max):
    return max(avistamientos_cercanos_ubicacion(lista, ubicacion, distancia_max), key=lambda x: x.duracion)

def avistamientos_fechas(lista, fecha1, fecha2):
    return [i for i in lista if fecha1 <= i.fechahora.date() <= fecha2]

def comentario_mas_largo(lista:list[Ovni], año:int, palabra:str)->Ovni:
    return max(
        [i for i in lista if i.fechahora.year == año and palabra in i.comentarios],
        key=lambda x: len(x.comentarios)
    )

def duracion_maxima(lista):
    return max(lista, key=lambda x: x.duracion)

def media_dias_entre_avistamientos(lista:list[Ovni], año:int)->float:
    agua = sorted([i.fechahora.date() for i in lista if i.fechahora.year == año])
    pares = zip(agua, agua[1:])
    return sum((j - i).days for i, j in pares) / len(agua) - 1
    # fechas = sorted([i.fechahora.date() for i in lista if i.fechahora.year == año])
    # if len(fechas) < 2:
    #     return 0.0
    # else:
    #     return sum((fechas[i] - fechas[i-1]).days for i in range(1, len(fechas))) / (len(fechas) - 1)

# 4. Operaciones con diccionarios
def avistamientos_por_fecha(lista):
    return {i.fechahora.date(): len([j for j in lista if j.fechahora.date() == i.fechahora.date()]) for i in lista}

def formas_por_mes(lista):
    return {i: len([j for j in lista if j.fechahora.month == i]) for i in range(1, 13)}

#...

def hora_mas_avistamientos(lista:list[Ovni])->int:
    horas = map(lambda x: x.fechahora.hour, lista)
    c = Counter(horas)
    lista_maximos:list[tuple[int,int]] = c.most_common(1)
    tupla:tuple[int,int] = lista_maximos[0]
    return tupla[0], tupla[1]

## Extra, mismo código pero con una lista de mas comunes
def hora_mas_avistamientos2(lista:list[Ovni])->int:
    horas = map(lambda x: x.fechahora.hour, lista)
    c = Counter(horas)
    frecuencia_maxima = c.most_common(1)[0][1]
    return list(filter(lambda x: x[1] == frecuencia_maxima, c.items()))

def coordenadas_mas_avistamientos(lista:list[Ovni])->None:
    dicc = defaultdict(lambda: 0)
    for i in lista:
        coordenada = Cordenadas(int(i.latitud), int(i.longitud))
        dicc[coordenada] += 1
    
    return max(dicc.items(), key = lambda x: x[1])

def año_con_mayor_duracion_total_avistamientos(lista:list[Ovni])->int:
    dicc = defaultdict(lambda: 0)
    for i in lista:
        dicc[i.fechahora.year] += i.duracion
    return max(dicc.items(), key = lambda x: x[1])[0]

def top_n_avistamientos_mas_largos_por_año(lista:list[Ovni], n:int=3)->dict[int, list[Ovni]]:
    pass