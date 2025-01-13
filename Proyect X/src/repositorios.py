from typing import NamedTuple,List,Set,Tuple,Dict,Optional
from datetime import datetime,date
import csv
from collections import Counter, defaultdict
import statistics

Commit = NamedTuple("Commit",
    [("id", str), # Identificador alfanumérico del commit
    ("mensaje", str), # Mensaje asociado al commit
    ("fecha_hora", datetime) # Fecha y hora en la que se registró el commit
    ])
Repositorio = NamedTuple("Repositorio",
    [("nombre", str), # Nombre del repositorio
    ("propietario", str), # Nombre del usuario propietario
    ("lenguajes", Set[str]), # Conjunto de lenguajes usados
    ("privado", bool), # Indica si es privado o público
    ("commits", List[Commit]) # Lista de commits realizados
    ])

# Ejercicio 1
def parsea_commits(commits_str: str) -> List[Commit]:
    # '[b789101#Initial commit#2023-10-06 12:00:00;c567891#Added main functionality#2023-10-06 13:00:00]'
    commits = commits_str.strip('[ ]').split(';')
    if commits == ['']:
        return None
    else:
        res = []
        for i in commits:
            cadena = i.split('#')
            res.append(Commit(cadena[0], cadena[1], datetime.strptime(cadena[2], '%Y-%m-%d %H:%M:%S')))
        return res
def lee_repositorios(csv_filename: str) -> List[Repositorio]:
    res = []
    with open(csv_filename, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, propietario, lenguajes, privado, commits in lector:
            res.append(Repositorio(nombre, propietario, set(i for i in lenguajes.split(',')), privado == 'True', parsea_commits(commits)))
    return res

# Ejercicio 2
def total_commits_por_anyo(repositorios:List[Repositorio])->Dict[int, int]:
    dicc = defaultdict(int)
    for i in repositorios:
        if i.commits != None and i.privado == False:
            for j in i.commits:
                dicc[j.fecha_hora.year] += 1
    return dicc

# Ejercicio 3
def calcular_tasa_de_crecimiento(repositorio: Repositorio)->float:
    if repositorio.commits != None:
        n = len(repositorio.commits)
    else: return 0
    if n < 2:
        return 0
    else:
        dias = int((repositorio.commits[n-1].fecha_hora -repositorio.commits[0].fecha_hora).days)
        if dias < 1:
            return 0
        else:
            return n / dias
def n_mejores_repos_por_tasa_crecimiento(repositorios: List[Repositorio], n:Optional[int]=3)->List[Tuple[str,float]]:
    res = []
    for i in repositorios:
        res.append((i.nombre, calcular_tasa_de_crecimiento(i)))
    return sorted(res, key = lambda x: x[1], reverse=True)[:n]

# Ejercicio 4
def recomendar_lenguajes(repositorios:List[Repositorio], repositorio:Repositorio)->Set[str]:
    lenguajes = repositorio.lenguajes
    res = set()
    for i in repositorios:
        for j in i.lenguajes:
            if j in lenguajes:
                res.update(k for k in i.lenguajes if k not in lenguajes)
    return res

# Ejercicio 5
def media_minutos_entre_commits(commits: List[Commit]) -> float:
    media = None
    commits_ord = sorted(commits, key=lambda c: c.fecha_hora)
    res = []
    for c1, c2 in zip(commits_ord, commits_ord[1:]):
        dif = (c2.fecha_hora - c1.fecha_hora).total_seconds() / 60
        res.append(dif)
    if len(res) > 0:
        media = statistics.mean(res)
    return media

def media_minutos_entre_commits_por_usuario (repositorios:List[Repositorio],fecha_ini:Optional[date]=None,fecha_fin:Optional[date]=None)->Dict[str, float]:
    dicc = defaultdict(list) # Diccionario auxiliar
    res = defaultdict(float) # Respuesta

    for i in repositorios:
        if i.commits and (fecha_ini is None or i.commits[0].fecha_hora >= fecha_ini) and (fecha_fin is None or i.commits[-1].fecha_hora <= fecha_fin):
            dicc[i.propietario].extend(k for k in i.commits) # Con este diccionario auxilar damos a cada propietario una lista con todos los commits que ha hecho
    for i, j in dicc.items():
        if None in j:
            j.remove(None)
        else: res[i] = media_minutos_entre_commits(j) # Procesamos los commits de cada propietario con la función auxiliar para calcular la media
    return res