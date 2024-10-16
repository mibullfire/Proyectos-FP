import csv
from collections import namedtuple
from datetime import *

Ovni = namedtuple('Ovni', 'datetime,city,state,shape,duration,comments,ubicacion')
Coordenada = namedtuple('Coordenada', 'latitude,longitude')
def parse_datetime(str):
    return datetime.strptime(str, '%m/%d/%Y %H:%M')

def leer_fichero(fichero):
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for datetime,city,state,shape,duration,comments,latitude,longitude in lector:
            res.append(Ovni(parse_datetime(datetime),city,state,shape,duration,comments,Coordenada(float(latitude),float(longitude))))
    return res

def numero_avistamientos_fecha(lista:list[Ovni], fecha:datetime.date)->int:
    return len([i for i in lista if i.datetime.date() == fecha])