from collections import namedtuple
import csv

estaciones = namedtuple('Estaciones', 'name, slots, empty_slots, free_bikes, latitude, longitude')

def leer_fichero(fichero):
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for name, slots, empty_slots, free_bikes, latitude, longitude in lector:
            res.append(estaciones(name, int(slots), int(empty_slots), int(free_bikes), float(latitude), float(longitude)))
    return res

def estaciones_libres(lista, k):
    return [(x.free_bikes, x.name) for x in lista if x.free_bikes > k]

punto = namedtuple('Punto', 'x, y')
def calculo(punto1, punto2):
    return ((punto1.x - punto2.x)**2 + (punto1.y - punto2.y)**2)**0.5

def estaciones_cercanas_a_ubicacion(lista:list[estaciones], ubicacion:punto, k:int)->list[str]:
    res = sorted([i for i in lista], key=lambda x: calculo(ubicacion, punto(x.latitude, x.longitude)))
    return [(x.name, calculo(ubicacion, punto(x.latitude, x.longitude))) for x in res][:k]

#print(estaciones_libres(leer_fichero('./data/estaciones.csv'), 10))

#print(estaciones_cercanas_a_ubicacion(leer_fichero('./data/estaciones.csv'), punto(40.4169, -3.7038)))