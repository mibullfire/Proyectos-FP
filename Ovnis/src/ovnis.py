import csv
from collections import namedtuple, Counter, defaultdict
from datetime import *
from typing import Optional
import math # La he importado para el cálculo de la raíz cuadrada en la función distancia

# Creación de la namedtuple para guardar los archivos, se puede usar tanto la de collections como la de typing
Ovni = namedtuple('Ovni', 'fechahora, ciudad, estado, forma, duracion, comentarios, coordenadas')
# Namedtuple auxiliar para guardar las coordenadas
Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def parse_datetime(str):
    '''
    Función que recibe un string con el formato 'mm/dd/yyyy hh:mm' y lo convierte a un objeto datetime
    '''
    return datetime.strptime(str, '%m/%d/%Y %H:%M')

# 1. Función de lectura de datos
def leer_fichero(fichero):
    '''
    Función que recibe un fichero csv y devuelve una lista de objetos Ovni
    '''
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for datetime,city,state,shape,duration,comments,latitude,longitude in lector:
            coordenadas = Coordenadas(float(latitude), float(longitude))
            res.append(Ovni(parse_datetime(datetime),city,state,shape,int(duration),comments,coordenadas))
    return res

# 2. Operaciones de filtrado, conteo y suma
def numero_avistamientos_fecha(lista:list, fecha:datetime.date)->int:
    '''
    Función que obtiene el número total de avistamientos que se han producido en una fecha determinada, dada por su día, mes y año. 
    Se contarán, por tanto, los avistamientos que hayan tenido lugar a cualquier hora del día. La función recibe una lista de namedtuple 
    de tipo Avistamiento, y una fecha de tipo datetime.date.
    '''
    # Nota: para funciones simples, puedes elegir entre usar un bucle for o una comprensión de listas con un filtro.
    filtrado = filter(lambda x: x.fechahora.date() == fecha, lista)
    return len(list(filtrado))  
    #return len([i for i in lista if i.fechahora.date() == fecha])

def formas_estados(lista:list, estados:set)->int:
    '''
    Función que obtiene el número de formas distintas que presentaron los avistamientos observados en uno o varios estados. 
    La función recibe una lista de namedtuple de tipo Avistamiento, y un conjunto de estados de tipo _str_.
    '''
    return len(set(i.forma for i in lista if i.estado in estados))

def duracion_total(lista:list, estado:str)->int:
    '''
    Función que devuelve la duración total en segundos de los avistamientos que se han observado en un estado. 
    La función recibe una lista de namedtuple de tipo Avistamiento, y un estado de tipo _str_.
    '''
    return sum([i.duracion for i in lista if i.estado == estado])

def distancia(punto1:Coordenadas, punto2:Coordenadas)->float:
    '''
    Función que calcula la distancia euclidea entre dos coordenadas. La función recibe dos tuplas de tipo _(float, float)_.
    '''
    return float(math.sqrt((punto1.latitud - punto2.latitud)**2 + (punto1.longitud - punto2.longitud)**2))

def avistamientos_cercanos_ubicacion(lista:list[Ovni], ubicacion:Coordenadas, distancia_max:float)->list:
    return [i for i in lista if distancia(i.coordenadas, ubicacion) <= distancia_max]

# 3. Operaciones con máximos, mínimos y ordenación
def avistamiento_mayor_duracion(lista:list, forma:Optional[str]=None)->Ovni:
    '''
    Función que obtiene el avistamiento de mayor duración de entre todos los avistamientos que tienen una forma determinada.
    La función recibe una lista de namedtuple de tipo Avistamiento y la forma del avistamiento de tipo _str_.
    '''
    return max([i for i in lista if (forma == None or i.forma == forma)], key = lambda x: x.duracion)

def avistamiento_cercano_mayor_duracion(lista:list[Ovni], ubicacion:Coordenadas, distancia_max:float)->Ovni:
    '''
    Función que devuelve el avistamiento que más tiempo ha durado de aquellos situados dentro de un radio de distancia de una ubicación dada; 
    es decir, la distancia entre las coordenadas del avistamiento y las coordenadas que se pasan como parámetro de entrada debe ser menor al 
    radio que también aparece como parámetro de la función. El resultado debe ser una tupla de la forma (duración, comentarios). 
    La función recibe una lista de namedtuple de tipo Avistamiento, una coordenada que será una tupla de tipo _(float, float)_, 
    y una distancia de tipo float.
    '''
    # Vamos a reusar la función avistamientos_cercanos_ubicacion, y vamos a sacar el máximo de esa lista
    return max(avistamientos_cercanos_ubicacion(lista, ubicacion, distancia_max), key=lambda x: x.duracion)

def avistamientos_fechas(lista:list[Ovni], fecha1:Optional[date]=None, fecha2:Optional[date]=None)->list[Ovni]:
    '''
    Función que devuelve una lista con los avistamientos observados entre una fecha inicial y una fecha final, ambas inclusive. 
    La lista devuelta estará ordenada de los avistamientos más recientes a los más antiguos. Si la fecha inicial es _None_, 
    se devolverán todos los avistamientos desde el más antiguo hasta la fecha final. Si la fecha final es _None_, se devolverán todos 
    los avistamientos desde la fecha inicial hasta el más reciente. Si ambas fechas son _None_, se devolverá la lista de avistamientos completa. 
    La función recibe una lista de namedtuple de tipo Avistamiento, y dos fechas de tipo datetime.date: una como principio del intervalo y otra como final. 
    Las fechas recibidas como parámetro tendrán como valor por defecto _None_.
    '''
    entre_fechas = list(filter(lambda x: (fecha1 == None or x.fechahora.date() >= fecha1) and (fecha2 == None or x.fechahora.date() <= fecha2), lista))
    return sorted(entre_fechas, key=lambda x: x.fechahora)

def comentario_mas_largo(lista:list[Ovni], año:int, palabra:str)->Ovni:
    '''
    Función que devuelve el avistamiento con el comentario más largo, de entre todos los avistamientos observados en un año dado 
    y cuyo comentario incluye una palabra concreta. La función recibe una lista de namedtuple de tipo Avistamiento, 
    un año de tipo int, y una palabra de tipo _str_.
    '''
    filtrado = list(filter(lambda x: x.fechahora.year == año and palabra in x.comentarios, lista))
    return max(filtrado, key=lambda x: len(x.comentarios))

def media_dias_entre_avistamientos(lista:list[Ovni], año:Optional[date]=None)->float:
    '''
    Función que devuelve la media de días transcurridos entre dos avistamientos consecutivos en el tiempo. La función permite hacer el cálculo para todos 
    los avistamientos, o solo para los de un año concreto. La función recibe una lista de namedtuple de tipo Avistamiento y un año de tipo int.
    '''
    # Filtra las fechas de los avistamientos que ocurrieron en el año especificado y las ordena cronológicamente
    fechas = sorted([i.fechahora.date() for i in lista if año == None or i.fechahora.year == año])
    # Crea pares de fechas consecutivas
    pares = zip(fechas[:-1], fechas[1:])
    # Calcula la diferencia en días entre cada par de fechas consecutivas con una comprensión de listas
    pares = list(map(lambda par: (par[1]-par[0]).days, pares))
    # Calcula y devuelve la media de días entre avistamientos consecutivos
    return sum(pares)/len(pares)

# 4. Operaciones con diccionarios
def avistamientos_por_fecha(lista:list[Ovni])->dict[datetime.date, list[Ovni]]:
    '''
    Función que crea un diccionario que relaciona las fechas con los avistamientos observados en dichas fechas. 
    Es decir, un diccionario cuyas claves son las fechas y cuyos valores son los conjuntos de avistamientos observados en cada fecha. 
    La función recibe una lista de namedtuple de tipo Avistamiento.
    '''
    diccionario = defaultdict(list)
    for i in lista:
        diccionario[i.fechahora.date()].append(i)
    return diccionario

def formas_por_mes(lista: list[Ovni]) -> dict[str, set[str]]:
    '''
    Función que devuelve un diccionario que indexa las distintas formas de avistamientos por los nombres de los meses en que se observaron.
    Para cada mes (por nombre), se tendrá un conjunto con todas las formas distintas observadas en dicho mes.
    La función recibe una lista de namedtuple de tipo Ovni.
    '''
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    diccionario = defaultdict(set)
    for avistamiento in lista:
        # Obtiene el nombre del mes basándose en el índice del mes (restando 1 porque los índices de listas empiezan en 0)
        mes_nombre = meses[avistamiento.fechahora.month - 1]
        diccionario[mes_nombre].add(avistamiento.forma)
    
    return diccionario

def numero_avistamientos_por_año(lista: list[Ovni]) -> dict[int, int]:
    '''
    Función que crea un diccionario que relaciona cada año con el número de avistamientos observados en dicho año. 
    Es decir, un diccionario cuyas claves son los años y cuyos valores son el número de avistamientos observados en cada año. 
    La función recibe una lista de namedtuple de tipo Avistamiento.
    '''
    diccionario = Counter(map(lambda x: x.fechahora.year, lista))
    return dict(sorted(diccionario.items()))

def coordenadas_mas_avistamientos(lista:list[Ovni])->None:
    '''
    Función que devuelve las coordenadas enteras que se corresponden con la zona donde más avistamientos se han observado. 
    Por ejemplo, si hay avistamientos en las coordenadas (40.1, -85.3), (41.13, -85.1) y (40.2, -85.4), la zona con más avistamientos 
    corresponde a las coordenadas enteras (40, -85) con 2 avistamientos.
    '''
    dicc = defaultdict(lambda: 0)
    for i in lista:
        dicc[i.coordenadas] += 1
    
    return max(dicc.items(), key = lambda x: x[1])

def hora_mas_avistamientos(lista:list[Ovni])->int:
    '''
    Función que devuelve la hora del día (de 0 a 23) en la que se han observado un mayor número de avistamientos.
    '''
    horas = map(lambda x: x.fechahora.hour, lista)
    c = Counter(horas)
    lista_maximos:list[tuple[int,int]] = c.most_common(1)
    tupla:tuple[int,int] = lista_maximos[0]
    return tupla[0], tupla[1]

def longitud_media_comentarios_por_estado(lista:list[Ovni])->dict[str, float]:
    '''
    Función que devuelve un diccionario en el que las claves son los estados donde se producen los avistamientos, 
    y los valores son la longitud media de los comentarios de los avistamientos observados en cada estado.
    '''
    dicc = defaultdict(lambda: [])
    for i in lista:
        dicc[i.estado].append(len(i.comentarios))
    return {k: sum(v)/len(v) for k,v in dicc.items()}

def porc_avistamientos_por_forma(lista:list[Ovni])->dict[str, float]:
    '''
    Función que devuelve un diccionario en el que las claves son las formas de los avistamientos, 
    y los valores son el porcentaje de avistamientos de cada forma con respecto al número total de avistamientos.
    '''
    dicc = Counter(map(lambda x: x.forma, lista))

    return {i: round(j / len(lista) *100, 3) for i, j in dicc.items()}

def avistamientos_mayor_duracion_por_estado(lista:list[Ovni], limite:Optional[int]=3)->dict[str, Ovni]:
    '''
    Función que devuelve un diccionario que relaciona los estados con los avistamientos de mayor duración observados 
    en dicho estado, ordenados de mayor a menor duración. Si no se indica nada, se obtendrán los tres avistamientos 
    de mayor duración. La función recibe una lista de namedtuple de tipo Avistamiento y un valor entero que representará 
    el límite que por defecto tendrá el valor 3.
    '''
    dicc = defaultdict(lambda: [])
    for i in lista:
        dicc[i.estado].append(i)
    return {i: sorted(j, key = lambda x: x.duracion, reverse=True)[:limite] for i, j in dicc.items()}

def año_mas_avistamientos_forma(lista:list[Ovni], forma:str)->int:
    '''
    Función que devuelve el año en el que se han observado más avistamientos de una forma dada. La función recibe 
    una lista de namedtuple de tipo Avistamiento y la forma a tener en cuenta que será de tipo str.
    '''
    lista = filter(lambda x: x.forma == forma, lista)
    contador = Counter(map(lambda x: x.fechahora.year, lista))
    return contador.most_common(1)[0][0]

def estados_mas_avistamientos(lista:list[Ovni], limite:Optional[int]=3)->list[tuple[str, int]]:
    '''
    Función que devuelve una lista con el nombre y el número de avistamientos de los estados con mayor número 
    de avistamientos, ordenados de mayor a menor número de avistamientos. Si no se indica nada, se obtendrán los 
    cinco estados con más avistamientos. La función recibe una lista de namedtuple de tipo Avistamiento y un valor 
    entero que representará el límite que por defecto tendrá el valor 3.
    '''
    dicc = Counter(map(lambda x: x.estado, lista))
    lista = list(dicc.items())
    return sorted(lista, key = lambda x: x[1], reverse = True)[:limite]

def duracion_total_avistamientos_año(lista:list[Ovni], estado:str)->dict[int, int]:
    '''
    Función que devuelve un diccionario que relaciona cada año con la suma de las duraciones de todos los avistamientos 
    observados durante ese año en un estado dado. La función recibe una lista de namedtuple de tipo Avistamiento y 
    el estado a tener en cuenta que será de tipo str.
    '''
    dicc = defaultdict(lambda: [])
    filtro = filter(lambda x: x.estado == estado, lista)
    for i in filtro:
            dicc[i.fechahora.year].append(i.duracion)
    return {i: sum(j) for i, j in dicc.items()}

def avistamiento_mas_reciente_estado(lista:list[Ovni])->dict[str, datetime]:
    '''
    Función que devuelve un diccionario que relaciona cada estado con la fecha del último avistamiento observado en el estado.
    '''
    dicc = defaultdict(lambda: [])
    for i in lista:
        dicc[i.estado].append(i.fechahora)
    return {i: max(j) for i, j in dicc.items()}

# Funciones Extras de Clases Teóricas
def año_con_mayor_duracion_total_avistamientos(lista:list[Ovni])->int:
    dicc = defaultdict(lambda: 0)
    for i in lista:
        dicc[i.fechahora.year] += i.duracion
    return max(dicc.items(), key = lambda x: x[1])[0]

def numero_avistamientos_por_dia(lista:list[Ovni])->dict[datetime.date, int]:
    contador = Counter(map(lambda x: x.fechahora.date(), lista))
    return contador

def estado_con_suma_top_n_duraciones_mas_larga(lista: list[Ovni], n: int = 3) -> str:
    res = defaultdict(list)
    for i in lista:
        res[i.estado].append(i.duracion)
    sumas = {
        estado: sum(sorted(duraciones, reverse=True)[:n])
        for estado, duraciones in res.items()
    }
    return max(sumas.items(), key=lambda x: x[1])[0]