from repositorios import *
from colorama import Fore

def test_lee_repositorios(csv_filename: str)->None:
    res = lee_repositorios(csv_filename)
    print(Fore.GREEN + "test lee_repositorios")
    print(len(res))
    print(res[0])

def test_total_commits_por_anyo(repositorios:List[Repositorio])->None:
    res = total_commits_por_anyo(repositorios)
    print(Fore.BLUE + 'test total_commits_por_anyo')
    print (res)

def test_n_mejores_repos_por_tasa_crecimiento(repositorios: List[Repositorio], n:Optional[int]=3)->None:
    res = n_mejores_repos_por_tasa_crecimiento(repositorios)
    print(Fore.RED + 'n_mejores_repos_por_tasa_crecimiento')
    print (res)

def test_recomendar_lenguajes(repositorios:List[Repositorio], repositorio:Repositorio)->None:
    res = recomendar_lenguajes(repositorios, repositorio)
    print(Fore.YELLOW + 'test recomendar_lenguajes')
    print (res)

def test_media_minutos_entre_commits_por_usuario(repositorios:List[Repositorio],fecha_ini:Optional[date]=None,fecha_fin:Optional[date]=None)->None:
    res = media_minutos_entre_commits_por_usuario(repositorios,fecha_ini,fecha_fin)
    print(Fore.MAGENTA + 'test media_minutos_entre_commits_por_usuario')
    print (res)

def main()->None:
    test_lee_repositorios("./data/data.csv")
    repositorios = lee_repositorios('./data/data.csv')
    test_total_commits_por_anyo(repositorios)
    test_n_mejores_repos_por_tasa_crecimiento(repositorios, 3)
    test_recomendar_lenguajes(repositorios, repositorios[0])
    test_media_minutos_entre_commits_por_usuario(repositorios)
    Fore.RESET

if __name__ == "__main__":
    main()