from ovnis import *
from colorama import Fore

# 1. Función de lectura de datos
def test_leer_fichero(fichero:str)->None:
    lista = leer_fichero(fichero)
    print(Fore.GREEN + '\nTest Leer fichero')
    print('Número de avistamientos:', len(lista))
    print('Primer avistamiento:', lista[0])

# 2. Operaciones de filtrado, conteo y suma
def test_numero_avistamientos_fecha(lista:list[Ovni], fecha:date)->None:
    print(Fore.LIGHTMAGENTA_EX + '\nNúmero de avistamientos en una fecha')
    print('Número de avistamientos en 2004-10-23:', numero_avistamientos_fecha(lista, fecha))

def test_formas_estados(lista:list[Ovni], estados:set[str])->None:
    print(Fore.BLUE + '\nFormas en los estados')
    print('Número de formas en los estados', estados)
    print(formas_estados(lista, estados))

def test_duracion_total(lista:list[Ovni], estado:str)->None:
    print(Fore.RED + '\nDuración total')
    print('Duración total en el estado', estado)
    print(duracion_total(lista, estado))

def test_distancia()->None:
    punto1 = Coordenadas(0, 0)
    punto2 = Coordenadas(40.1933333, -85.3863889)
    print(Fore.YELLOW + '\nDistancia entre dos puntos')
    print('Distancia entre', punto1, 'y', punto2)
    print(distancia(punto1, punto2))

def test_avistamientos_cercanos_ubicacion(lista:list[Ovni], ubicacion:Coordenadas, distancia:float)->None:
    print(Fore.YELLOW + '\nAvistamientos cercanos a una ubicación')
    print('Avistamientos cercanos a', ubicacion, 'a una distancia de', distancia)
    print(avistamientos_cercanos_ubicacion(lista, ubicacion, distancia))

# 3. Operaciones con máximos, mínimos y ordenación
def test_avistamiento_mayor_duracion(lista:list[Ovni], forma:str)->None:
    print(Fore.RED + '\nDuración máxima')
    print('Avistamiento con la duración máxima')
    print(avistamiento_mayor_duracion(lista, forma))

def test_avistamiento_cercano_mayor_duracion(lista:list[Ovni], ubicacion:Coordenadas, distancia:float)->None:
    print(Fore.CYAN + '\nAvistamiento cercano con mayor duración')
    print('Avistamiento cercano con mayor duración')
    print(avistamiento_cercano_mayor_duracion(lista, ubicacion, distancia))

def test_avistamientos_fechas(lista:list[Ovni], fecha:Optional[date]=None, fecha2:Optional[date]=None)->None:
    print(Fore.GREEN + '\nAvistamientos en fechas')
    print('Avistamientos entre las fechas', fecha, 'y', fecha2)
    print(avistamientos_fechas(lista, fecha, fecha2))

def test_comentario_mas_largo(lista:list[Ovni], año:int, palabra:str)->None:
    print(Fore.LIGHTWHITE_EX + '\nComentario más largo')
    print('Comentario más largo en el año', año, 'que contiene la palabra', palabra)
    print(comentario_mas_largo(lista, año, palabra))

def test_media_dias_entre_avistamientos(lista:list[Ovni], año:int)->None:
    print(Fore.LIGHTMAGENTA_EX + '\nMedia de días entre avistamientos')
    print('Media de días entre avistamientos del año', año)
    print(media_dias_entre_avistamientos(lista, año))

# 4. Operaciones con Diccionarios
def test_avistamientos_por_fecha(lista:list[Ovni])->None:
    print(Fore.LIGHTGREEN_EX + '\nAvistamientos por fecha')
    print(avistamientos_por_fecha(lista))

def test_formas_por_mes(lista:list[Ovni])->None:
    print(Fore.LIGHTWHITE_EX + '\nFormas por mes')
    print(formas_por_mes(lista))

def test_numero_avistamientos_por_año(lista:list[Ovni])->None:
    print(Fore.LIGHTYELLOW_EX + '\nNúmero de avistamientos por año')
    print(numero_avistamientos_por_año(lista))

def test_coordenada_mas_avistamientos(lista:list[Ovni])->None:
    print(Fore.LIGHTBLUE_EX + '\nCoordenada con más avistamientos')
    print(coordenadas_mas_avistamientos(lista))

def test_hora_mas_avistamientos(lista:list[Ovni])->None:
    print(Fore.BLUE + '\nTest Hora con más avistamientos')
    hora, numero = hora_mas_avistamientos(lista)
    print(f'La hora con más avistamientos es {hora} con {numero} avistamientos')

def test_longitud_media_comentarios_por_estado(lista:list[Ovni])->None:
    print(Fore.MAGENTA + '\ntest_longitud_media_comentarios_por_estado')
    print(longitud_media_comentarios_por_estado(lista))

def test_porc_avistamientos_por_forma(lista:list[Ovni])->None:
    print(Fore.MAGENTA + '\ntest_porc_avistamientos_por_forma')
    print(porc_avistamientos_por_forma(lista))

def test_avistamientos_mayor_duracion_por_estado(lista:list[Ovni], limite:Optional[int]=3)->None:
    print(Fore.LIGHTGREEN_EX + '\ntest_avistamientos_mayor_duracion_por_estado')
    print(avistamientos_mayor_duracion_por_estado(lista, limite))

def test_año_mas_avistamientos_forma(lista:list[Ovni], forma:str)->None:
    print(Fore.BLUE + '\ntest_año_mas_avistamientos_forma')
    print(año_mas_avistamientos_forma(lista, forma))

def test_estado_mas_avistamientos(lista:list[Ovni], limite:Optional[int]=5)->None:
    print(Fore.LIGHTBLUE_EX + '\ntest_estado_mas_avistamientos')
    print(estados_mas_avistamientos(lista, limite))

def test_duracion_total_avistamientos_año(lista:list[Ovni], estado:str)->None:
    print(Fore.LIGHTCYAN_EX + '\ntest_duracion_total_avistamientos_año')
    print(duracion_total_avistamientos_año(lista, estado))

def test_avistamiento_mas_reciente_estado(lista:list[Ovni])->None:
    print(Fore.LIGHTRED_EX + '\ntest_avistamiento_mas_reciente_estado')
    print(avistamiento_mas_reciente_estado(lista))

# Funciones Extras de Clases Teóricas
def test_año_con_mayor_duracion_total_avistamientos(lista:list[Ovni])->None:
    print(Fore.RED + '\nTest Año con mayor duración total de avistamientos')
    x = año_con_mayor_duracion_total_avistamientos(lista)
    print(x)

def test_numero_avistamientos_por_dia(lista:list[Ovni])->None:
    print(Fore.GREEN + '\ntest_numero_avistamientos_por_dia')
    print(numero_avistamientos_por_dia(lista))

def test_estado_con_suma_top_n_duraciones_mas_larga(lista:list[Ovni], n:int)->None:
    print(Fore.CYAN + '\ntest_estado_con_suma_top_n_duraciones_mas_larga')
    print(estado_con_suma_top_n_duraciones_mas_larga(lista, n))
    
def main():
    fichero = './data/ovnis.csv'
    # 1. Función de lectura de datos
    test_leer_fichero(fichero)
    lista = leer_fichero(fichero)
    # 2. Operaciones de filtrado, conteo y suma
    test_numero_avistamientos_fecha(lista, date(2010, 12, 3))
    test_formas_estados(lista, {'in', 'nm'})
    test_duracion_total(lista, 'in')
    test_distancia()
    test_avistamientos_cercanos_ubicacion(lista, ubicacion = Coordenadas(0, 0), distancia = 70)
    # 3. Operaciones con máximos, mínimos y ordenación
    test_avistamiento_mayor_duracion(lista, 'light')
    test_avistamiento_cercano_mayor_duracion(lista, ubicacion = Coordenadas(0, 0), distancia = 70)
    test_avistamientos_fechas(lista, date(2004, 10, 23), date(2004, 10, 24))
    test_comentario_mas_largo(lista, 2000, 'lights')
    test_media_dias_entre_avistamientos(lista, 1999)
    # 4 Operaciones con Diccionarios
    #test_avistamientos_por_fecha(lista) # No se puede testear porque el diccionario es muy grande
    test_formas_por_mes(lista)
    test_numero_avistamientos_por_año(lista)
    test_coordenada_mas_avistamientos(lista)
    test_hora_mas_avistamientos(lista)
    test_longitud_media_comentarios_por_estado(lista)
    test_porc_avistamientos_por_forma(lista)
    test_avistamientos_mayor_duracion_por_estado(lista, 1)
    test_año_mas_avistamientos_forma(lista, 'light')
    test_estado_mas_avistamientos(lista)
    test_duracion_total_avistamientos_año(lista, 'in')
    test_avistamiento_mas_reciente_estado(lista)

    Fore.RESET
    
if __name__ == '__main__':
    main()