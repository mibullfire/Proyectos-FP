from carreras_ext import *
from colorama import Fore

# Test de la función leeCarreras
def test_leeCarreras():
    # Archivos de ejemplo (puedes usar tus propios archivos CSV aquí)
    nomfichCarreras = './data/carreras.csv'
    nomfichParticipantes = './data/participantes.csv'

    # Llamamos a la función
    carreras = leeCarreras(nomfichCarreras, nomfichParticipantes)

    # Mostrar número de carreras
    print(Fore.BLUE+f"Total de carreras: {len(carreras)}\n")

    # Mostrar los tres primeros registros
    print("Primeros tres registros:")
    for i, carrera in enumerate(carreras[:3], 1):
        print(f"\nCarrera {i}:")
        print(f"  CarreraID: {carrera.carrera_id}")
        print(f"  Localidad: {carrera.localidad}")
        print(f"  Fecha y Hora: {carrera.fecha_hora.strftime('%Y-%m-%d %H:%M')}")
        print(f"  Tipo: {carrera.tipo}")
        print(f"  Distancia: {carrera.distancia} metros")
        print(f"  Desnivel: {carrera.desnivel} metros")
        print(f"  Número de participantes: {len(carrera.participantes)}")

    # Mostrar los tres últimos registros
    print("\nÚltimos tres registros:")
    for i, carrera in enumerate(carreras[-3:], len(carreras) - 2):
        print(f"\nCarrera {i}:")
        print(f"  CarreraID: {carrera.carrera_id}")
        print(f"  Localidad: {carrera.localidad}")
        print(f"  Fecha y Hora: {carrera.fecha_hora.strftime('%Y-%m-%d %H:%M')}")
        print(f"  Tipo: {carrera.tipo}")
        print(f"  Distancia: {carrera.distancia} metros")
        print(f"  Desnivel: {carrera.desnivel} metros")
        print(f"  Número de participantes: {len(carrera.participantes)}")

def test_carreraMayorDesnivelParticipante() -> None:
    print(Fore.GREEN+"\nEJERCICIO 4.1:")
    print("----- Carrera con mayor desnivel de participante: --------")

    # Cargar las carreras y participantes desde los archivos
    carreras = leeCarreras('./data/carreras.csv', './data/participantes.csv')

    # Prueba de la función
    resultado = carreraMayorDesnivelParticipante(carreras, "Alejandro", "Ruiz Blanco")
    print(f"Alejandro Ruiz Blanco: Carrera {resultado}")

    resultado = carreraMayorDesnivelParticipante(carreras, "Elena", "Blanco Vázquez")
    print(f"Elena Blanco Vázquez: Carrera {resultado}")

def test_tiempoMedioCarrera() -> None:
    print(Fore.RED+"\nEJERCICIO 4.2:")
    print("----- Tiempo medio de carrera: --------")

    # Cargar las carreras y participantes desde los archivos
    carreras = leeCarreras('./data/carreras.csv', './data/participantes.csv')

    # Prueba de la función
    for carrera in carreras:
        resultado = tiempoMedioCarrera(carreras, carrera.carrera_id)
        print(f"{carrera.carrera_id}: {resultado}")

def test_ganadoresPorCategoria() -> None:
    print(Fore.CYAN+"\nEJERCICIO 4.3:")
    print("----- Ganadores por categoría: --------")

    # Cargar las carreras y participantes desde los archivos
    carreras = leeCarreras('./data/carreras.csv', './data/participantes.csv')

    # Prueba de la función
    for carrera in carreras:
        resultado = ganadoresPorCategoria(carreras, carrera.carrera_id)
        print(f"{carrera.carrera_id}: {resultado}")


if __name__ == "__main__":
    test_leeCarreras()
    test_carreraMayorDesnivelParticipante()
    test_tiempoMedioCarrera()
    test_ganadoresPorCategoria()
    Fore.RESET