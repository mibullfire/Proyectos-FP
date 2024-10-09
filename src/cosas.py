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

def filtra(lista, k):
    return [(x.free_bikes, x.name) for x in lista if x.free_bikes > k]

print(filtra(leer_fichero('./data/estaciones.csv'), 10))