from ovnis import *
from colorama import Fore

def test_leer_fichero(fichero):
    lista = leer_fichero(fichero)
    print(Fore.GREEN + '\nTest Leer fichero')
    print('Número de avistamientos:', len(lista))
    print('Primer avistamiento:', lista[0])

def test_numero_avistamientos_fecha(fichero):
    lista = leer_fichero(fichero)
    print(Fore.LIGHTMAGENTA_EX + '\nNúmero de avistamientos en una fecha')
    print('Número de avistamientos en 2004-10-23:', numero_avistamientos_fecha(lista, date(2010, 12, 3)))

def test_formas_estados(fichero):
    avistamientos = leer_fichero(fichero)
    estados = {'in', 'nm'}
    print(Fore.BLUE + '\nFormas en los estados')
    print('Número de formas en los estados', estados)
    print(formas_estados(avistamientos, estados))

def test_avistamientos_cercanos_ubicacion(fichero):
    avistamientos = leer_fichero(fichero)
    ubicacion = Cordenadas(0, 0)
    distancia = 70
    print(Fore.YELLOW + '\nAvistamientos cercanos a una ubicación')
    print('Avistamientos cercanos a', ubicacion, 'a una distancia de', distancia)
    print(avistamientos_cercanos_ubicacion(avistamientos, ubicacion, distancia))

def test_prueba(fichero):
    avistamientos = leer_fichero(fichero)
    print(prueba(avistamientos))

def test_duracion_maxima(fichero):
    avistamientos = leer_fichero(fichero)
    print(Fore.RED + '\nDuración máxima')
    print('Duración máxima')
    print(duracion_maxima(avistamientos))

def test_avistamiento_cercano_mayor_duracion(fichero):
    avistamientos = leer_fichero(fichero)
    ubicacion = Cordenadas(0, 0)
    distancia = 70
    print(Fore.CYAN + '\nAvistamiento cercano con mayor duración')
    print('Avistamiento cercano con mayor duración')
    print(avistamiento_cercano_mayor_duracion(avistamientos, ubicacion, distancia))

def test_avistamiento_mayor_duracion(fichero, forma=None):
    avistamientos = leer_fichero(fichero)
    print(Fore.MAGENTA + '\nAvistamiento con mayor duración de x forma',)
    print('Avistamiento con mayor duración de forma', forma)
    print(avistamiento_mayor_duracion(avistamientos, forma))

def test_comentario_mas_largo(fichero):
    avistamientos = leer_fichero(fichero)
    print(Fore.GREEN + '\nComentario más largo')
    print('Comentario más largo')
    print(comentario_mas_largo(avistamientos))


def main():
    fichero = './data/ovnis.csv'
    test_leer_fichero(fichero)
    test_numero_avistamientos_fecha(fichero)
    test_formas_estados(fichero)
    test_avistamientos_cercanos_ubicacion(fichero)
    test_duracion_maxima(fichero)
    test_avistamiento_cercano_mayor_duracion(fichero)
    test_avistamiento_mayor_duracion(fichero)
    test_comentario_mas_largo(fichero)
    Fore.RESET
    
if __name__ == '__main__':
    main()