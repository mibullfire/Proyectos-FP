from collections import namedtuple
import csv

# Definimos una estructura de datos llamada 'estaciones' con los campos especificados
estaciones = namedtuple('Estaciones', 'name, slots, empty_slots, free_bikes, latitude, longitude')

# Función para leer un fichero CSV y devolver una lista de objetos 'estaciones'
def leer_fichero(fichero):
    res = []
    # Abrimos el fichero con codificación 'utf-8'
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)  # Saltamos la primera línea (cabecera)
        # Leemos cada línea del fichero y creamos un objeto 'estaciones' con los datos
        for name, slots, empty_slots, free_bikes, latitude, longitude in lector:
            res.append(estaciones(name, int(slots), int(empty_slots), int(free_bikes), float(latitude), float(longitude)))
    return res

# Función que devuelve una lista de estaciones con más de 'k' bicicletas libres
def estaciones_libres(lista, k):
    return [(x.free_bikes, x.name) for x in lista if x.free_bikes > k]

# Definimos una estructura de datos llamada 'punto' con los campos 'x' e 'y'
punto = namedtuple('Coordenada', 'latitud, longitud')

# Función para calcular la distancia euclidiana entre dos puntos
def calculo(punto1:float, punto2:float)->float:
    return ((punto1.x - punto2.x)**2 + (punto1.y - punto2.y)**2)**0.5

# Función que devuelve una lista de nombres de las 'k' estaciones más cercanas a una ubicación dada
def estaciones_cercanas_a_ubicacion(lista:list[estaciones], ubicacion:punto, k:int)->list[str]:
    # Calculamos la distancia de cada estación a la ubicación dada y ordenamos por distancia
    return sorted([(i.name, calculo(ubicacion, punto(i.latitude, i.longitude))) for i in lista], key = lambda x: x[1])[:k]

# Función que calcula la media de las coordenadas (latitud y longitud) de una lista de estaciones
def media_coordenadas(estaciones:list[estaciones])->punto:
    d = len(estaciones)  # Número de estaciones en la lista
    # Calculamos la media de las latitudes y longitudes
    return punto(sum([i.latitude for i in estaciones])/d, sum([i.longitude for i in estaciones])/d)