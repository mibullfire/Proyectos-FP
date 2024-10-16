from ovnis import *

def test_leer_fichero(fichero):
    lista = leer_fichero(fichero)
    print('Número de avistamientos:', len(lista))
    print('Primer avistamiento:', lista[0])

def test_numero_avistamientos_fecha(fichero):
    lista = leer_fichero(fichero)
    print('Número de avistamientos en 2004-10-23:', numero_avistamientos_fecha(lista, date(2010, 12, 3)))

def test_formas_estados(fichero):
    avistamientos = leer_fichero(fichero)
    estados = {'in', 'nm'}
    print('\nNúmero de formas en los estados', estados)
    print(formas_estados(avistamientos, estados))

def test_avistamientos_cercanos_ubicacion(fichero):
    avistamientos = leer_fichero(fichero)
    ubicacion = Cordenadas(0, 0)
    distancia = 70
    print('\nAvistamientos cercanos a', ubicacion, 'a una distancia de', distancia)
    print(avistamientos_cercanos_ubicacion(avistamientos, ubicacion, distancia))

def test_prueba(fichero):
    avistamientos = leer_fichero(fichero)
    print(prueba(avistamientos))

def test_duracion_maxima(fichero):
    avistamientos = leer_fichero(fichero)
    print('\nDuración máxima')
    print(duracion_maxima(avistamientos))

def test_avistamiento_cercano_mayor_duracion(fichero):
    avistamientos = leer_fichero(fichero)
    ubicacion = Cordenadas(0, 0)
    distancia = 70
    print('\nAvistamiento cercano con mayor duración')
    print(avistamiento_cercano_mayor_duracion(avistamientos, ubicacion, distancia))

def main():
    fichero = './data/ovnis.csv'
    test_leer_fichero(fichero)
    test_numero_avistamientos_fecha(fichero)
    test_formas_estados(fichero)
    test_avistamientos_cercanos_ubicacion(fichero)
    test_duracion_maxima(fichero)
    test_avistamiento_cercano_mayor_duracion(fichero)
    
if __name__ == '__main__':
    main()