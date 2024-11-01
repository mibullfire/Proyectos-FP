# Operaciones con listas
Autor: Mariano González. Revisión: Toñi Reina
Última actualización: 27/10/2023


Vamos a repasar las operaciones más típicas que podemos hacer con listas de tuplas. Para ello, consideremos la siguiente lista de ríos (fuente: [Wikipedia](https://es.wikipedia.org/wiki/Anexo:R%C3%ADos_m%C3%A1s_largos_de_la_Tierra)). Usaremos namedtuple para poder llamar a cada elemento de la tupla por su nombre.


```python
from collections import namedtuple

Rio = namedtuple("Rio", "nombre longitud continente")
rios = [Rio("Amazonas", 7062, "América del Sur"), Rio("Nilo", 6853, "África"),
        Rio("Yangtsé", 6300, "Asia"), Rio("Misisipi", 6275, "América del Norte"),
        Rio("Amarillo", 5464, "Asia"), Rio("Mekong", 4880, "Asia"),
        Rio("Congo", 4700, "África"), Rio("Danubio", 2850, "Europa")]
```

Sobre esta lista realizaremos las siguientes operaciones:
- Recorrer la lista
- Filtrar la lista
- Transformar la lista
- Filtrar y transformar la lista a la vez
- Eliminar elementos duplicados de la lista
- Ordenar la lista
- Encontrar el mínimo o el máximo
- Obtener los n mayores elementos de la lista

### Recorrido

Recorrido usando una tupla:


```python
for rio in rios:
    print(rio)
```

Recorrido usando una variable para cada elemento de la tupla:


```python
for nombre, longitud, continente in rios:
    print(f"Río {nombre} ({continente}). Longitud: {longitud} kms")
```

Si no usamos un elemento de la tupla no es necesario darle un nombre, pero hay que indicar que existe y cuál es su posición:


```python
for nombre, longitud, _ in rios:
    print(f"El río " + nombre + " tiene una longitud de {longitud} kms")
```

Si usamos namedtuple este recorrido se simplifica, ya que podemos referirnos al elemento por su nombre y no por su posición:


```python
for r in rios:
    print(f"El río {r.nombre} tiene una longitud de {r.longitud} kms")
```

### Filtrado

En esta operación creamos una lista de tuplas que contiene una parte de la lista original, concretamente aquellas tuplas que cumplen una condición determinada. Para ello, usamos un if dentro del recorrido. Por ejemplo, vamos a construir una lista con los ríos situados en África:


```python
rios_africa = [r for r in rios if r.continente == "África"]
print(rios_africa)
```

### Transformación

Podemos transformar la lista de tuplas en otra lista de tuplas, pero con tuplas diferentes. Por ejemplo, una tupla que tenga solo el nombre y la longitud del río:


```python
nombre_longitud_rios = [(r.nombre, r.longitud) for r in rios]
print(nombre_longitud_rios)
```

Observa que la tupla de salida no tiene por qué estar formada por elementos de la tupla original. Puede que algún elemento se obtenga realizando algún cálculo a partir de estos elementos. Por ejemplo, vamos a obtener una lista de tuplas formada por el nombre y la longitud, expresada en miles de kilómetros:


```python
nombre_longitud_rios = [(r.nombre, r.longitud/1000) for r in rios]
print(nombre_longitud_rios)
```

Incluso podemos quedarnos solo con un elemento de la tupla:


```python
nombres_rios = [r.nombre for r in rios]
print(nombres_rios)
```

### Filtrado y transformación

Podemos combinar las operaciones de filtrado y transformación. Por ejemplo, podemos obtener los nombres de los ríos de Asia, filtrando el continente y transformando la tupla original en el nombre del río:


```python
nombres_rios_asia = [r.nombre for r in rios if r.continente == "Asia"]
print(nombres_rios_asia)
```

### Eliminación de elementos duplicados

Observa el siguiente ejemplo, que nos dice en qué continentes hay ríos:


```python
lista_continentes = [r.continente for r in rios]
print(lista_continentes)
```

Vemos que los continentes se repiten, y nos interesa que solo aparezcan una vez. Para ello, en lugar de crear una lista, podemos crear un conjunto, ya que un conjunto no admite elementos duplicados:


```python
conjunto_continentes = {r.continente for r in rios}
print(conjunto_continentes)
```

Hay que tener en cuenta que el orden en que se muestran los continentes es aleatorio, ya que los elementos de un conjunto no ocupan una posición en el mismo y por tanto no se pueden ordenar. Si queremos que los continentes estén ordenados alfabéticamente, hemos de convertir el conjunto en una lista, que sí se puede ordenar:


```python
conjunto_continentes = {r.continente for r in rios}
lista_continentes = list(conjunto_continentes)
lista_continentes.sort()
print(lista_continentes)
```

Podemos abreviar este código utilizando la función sorted, que realiza la misma operación que el método sort, pero se puede aplicar a un conjunto, devolviendo una lista ordenada con los elementos del conjunto:


```python
conjunto_continentes = {r.continente for r in rios}
lista_continentes = sorted(conjunto_continentes)
print(lista_continentes)
```

### Ordenación, máximo y mínimo

Para ordenar los elementos de una lista se utiliza el método sort. Observa por ejemplo cómo creamos una lista con las longitudes de los ríos y luego la ordenamos en orden creciente de longitud:


```python
longitudes = [r.longitud for r in rios]
print(f"Lista sin ordenar: {longitudes}")
longitudes.sort()
print(f"Lista ordenada: {longitudes}")
```

El método sort ordena la lista según el orden natural del elemento, que es el orden creciente en los números, el alfabético en las cadenas o el cronológico en las fechas y horas. Si queremos que se ordene de forma decreciente, hemos de añadir el parámetro reverse al método sort:


```python
longitudes.sort(reverse = True)
print(f"Lista en orden decreciente: {longitudes}")
```

Con las funciones max y min podemos obtener el mayor elemento de una lista. Por ejemplo, la longitud mayor de un río la obtenemos con max:


```python
mayor_longitud = max(longitudes)
print(mayor_longitud)
```

Y si en lugar de la longitud mayor queremos obtener las tres mayores, entonces nos quedamos con los tres primeros elementos de la lista, de la siguiente forma:


```python
n = 3
lista_n_mayores_longitudes = longitudes[:n]
print(f"Las {n} mayores longitudes son: {lista_n_mayores_longitudes}")
```

### Ordenación, máximo y mínimo con listas de tuplas

Supongamos que queremos ordenar la lista de tuplas original. Podemos aplicarle el método sort:


```python
rios.sort()
print(rios)
```

Cuando aplicamos sort a una lista de tuplas, la lista se ordena según el orden natural del primer elemento de la tupla. En este caso, el primer elemento es el nombre del río, así que se ordena la lista de tuplas en orden alfabético del nombre del río. Si queremos que el orden sea el alfabético inverso, usamos el parámetro reverse:


```python
rios.sort(reverse = True)
print(rios)
```

Esto está bien, pero, ¿qué pasa si queremos ordenar la lista por la longitud de los ríos? Una opción sería crear una nueva lista donde la longitud fuese el primer elemento de la tupla. Al ordenar esta lista, tendríamos el orden deseado:


```python
rios_2 = [(r.longitud, r.nombre, r.continente) for r in rios]
rios_2.sort()
print(rios_2)
```

Afortunadamente, existe una forma de hacer esto sin tener que crear una nueva lista: añadir al método sort un parámetro que indique el elemento de la tupla por el cual queremos ordenar. Esto se hace de la siguiente forma:


```python
rios.sort(key=lambda r:r.longitud)
print(rios)
```

El parámetro key indica el elemento de la tupla por el cual queremos ordenar, de la forma r:r.longitud. Si queremos que el orden sea el inverso, es decir, de mayor a menor, usamos el parámetro reverse como hicimos antes:


```python
rios.sort(key=lambda r:r.longitud, reverse=True)
print(rios)
```

Ya podemos pues ordenar una lista de tuplas por cualquier elemento, y no necesariamente por el primero. Recuerda: si no indicamos nada, se ordena por el primer elemento; si añadimos el parámetro key de la forma que hemos visto, cambiamos el elemento por el cual se ordena la lista. Y si además añadimos el parámetro reverse, se ordena de forma inversa.

### Otras operaciones

Existen otros métodos que podemos aplicar a las listas, como len (calcula el tamaño de la lista) o sum (calcula la suma de los elementos de la lista). Combinando ambos podemos hacer operaciones como calcular la longitud media de los ríos de Asia:


```python
longitudes = [rio.longitud for rio in rios if rio.continente == continente]    
longitud_media = None
if len(longitudes)>0:
    longitud_media = sum(longitudes)/len(longitudes)
print(f"Longitud media de los ríos de Asia: {longitud_media)}")
```
Aunque la media también se puede calcular usando la función `means` del paquete `statistics`(recuerde que debe importar este paquete). La diferencia de `means` con la implementación anterior es que en caso de que no se pueda calcular la media, en lugar de devolver `None`, eleva la excepción `StatisticsError`.

```python
longitud_media=statistics.mean (rio.longitud for rio in rios if rio.continente == continente)  
print(f"Longitud media de los ríos de Asia: {longitud_media)}")
```
## Ejercicio

Ahora te toca a ti poner en práctica las ideas anteriores. Para ello trabajarás con la siguiente lista. Resuelve los siguientes ejercicios en el módulo `picos.py` y testéalos en el módulo `picos_test.py`:


```python
Pico = namedtuple("Pico", "nombre altitud provincia")
picos = [Pico("Mulhacén", 3479, "Granada"), Pico("Torreón", 1648, "Cádiz"),
         Pico("Peña Santa", 2596, "León"), Pico("Naranjo", 2519, "Asturias"),
         Pico("Alcazaba", 3371, "Granada"), Pico("Veleta", 3396, "Granada"),
         Pico("Torrecilla", 1919, "Málaga"), Pico("Llambrión", 2647, "León"),
         Pico("Teide", 3718, "Santa Cruz de Tenerife")]
```

Realiza las siguientes operaciones sobre esta lista:

### 1. Obtener una lista con los nombres de los picos ordenada alfabéticamente
Resultado esperado: ['Alcazaba', 'Llambrión', 'Mulhacén', 'Naranjo', 'Peña Santa', 'Teide', 'Torrecilla', 'Torreón', 'Veleta']


```python

```

### 2. Obtener una lista con la altitud en kms y el nombre de los picos
Resultado esperado: [(3.479, 'Mulhacén'), (1.648, 'Torreón'), (2.596, 'Peña Santa'), (2.519, 'Naranjo'), (3.371, 'Alcazaba'), (3.396, 'Veleta'), (1.919, 'Torrecilla'), (2.647, 'Llambrión'), (3.718, 'Teide')]


```python

```

### 3. Obtener una lista con los picos que están en la provincia de Granada
Resultado esperado: [('Mulhacén', 3479, 'Granada'), ('Alcazaba', 3371, 'Granada'), ('Veleta', 3396, 'Granada')]


```python

```

### 4. Obtener una lista con la altitud y el nombre de los picos que tienen más de 2000 metros de altitud, ordenada de mayor a menor altitud
Resultado esperado: [(3718, 'Teide'), (3479, 'Mulhacén'), (3396, 'Veleta'), (3371, 'Alcazaba'), (2647, 'Llambrión'), (2596, 'Peña Santa'), (2519, 'Naranjo')]


```python

```

### 5. Obtener la suma de las altitudes de los picos que están en la provincia de León
Resultado esperado: 5243


```python

```

### 6. Obtener el nombre y la altitud del pico más alto de la lista
Resultado esperado: (3718, 'Teide')


```python

```

### 7. Obtener la altitud media de los picos
Resultado esperado: 2810.3333333333335


```python

```

### 8. Obtener una lista ordenada con las provincias donde hay picos, sin repetir ninguna
Resultado esperado: ['Asturias', 'Cádiz', 'Granada', 'León', 'Málaga', 'Santa Cruz de Tenerife']


```python

```
