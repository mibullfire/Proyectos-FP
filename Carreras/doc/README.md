

# **Gestión de Carreras Deportivas**

En este boletín trabajarás con estructuras avanzadas de datos en Python para gestionar y analizar información sobre carreras deportivas y sus participantes. Resolverás ejercicios relacionados con la lectura, procesamiento y consulta de datos almacenados en archivos CSV.

### **Contexto**

Una organización de eventos deportivos necesita un sistema para gestionar información sobre sus carreras y participantes. Cada carrera incluye datos como la ubicación, fecha, tipo, distancia y desnivel, mientras que cada participante tiene detalles como su nombre, edad, sexo y el tiempo que tardó en completar la carrera (echa un vistazo a *carreras.csv* y *participantes.csv* para más detalles).

Tu objetivo será implementar funciones que permitan analizar esta información y responder preguntas clave.

----------

## **Ejercicio 1: Modelado de datos**

Define las siguientes estructuras de datos utilizando `NamedTuple`:

1.  **`Participante`**: Representa a un corredor con los siguientes campos:
    
    -   `carrera_id` (str): Identificador de la carrera.
    -   `nombre` (str): Nombre del participante.
    -   `apellidos` (str): Apellidos del participante.
    -   `edad` (int): Edad del participante.
    -   `sexo` (str): Sexo del participante (`"HOMBRE"` o `"MUJER"`).
    -   `duracion` (timedelta): Tiempo empleado en completar la carrera.
2.  **`Carrera`**: Representa una carrera deportiva con los siguientes campos:
    
    -   `carrera_id` (str): Identificador de la carrera.
    -   `localidad` (str): Lugar donde se realiza la carrera.
    -   `fecha_hora` (datetime): Fecha y hora de inicio.
    -   `tipo` (str): Tipo de carrera (por ejemplo, `"Trail"`, `"Ruta"`).
    -   `distancia` (int): Distancia total en metros.
    -   `desnivel` (int): Desnivel acumulado en metros.
    -   `participantes` (List[Participante]): Lista de participantes asociados.

----------

## **Ejercicio 2: Lectura de datos desde archivos CSV**

Implemente una función `leeCarreras` que reciba dos nombres de archivos CSV:

-   `nomfichCarreras`: Contiene información sobre las carreras.
-   `nomfichParticipantes`: Contiene información sobre los participantes.

La función debe:

1.  Leer ambos archivos y crear instancias de las tuplas `Participante` y `Carrera`.
2.  Asociar cada participante a su correspondiente carrera.
3.  Devolver una lista de objetos `Carrera`.

**Nota:** La duración de cada participante está en formato ISO 8601 (`PTxxx...xHyyy...yMzzz…zS`). Implemente una función auxiliar `parsear_duracion` que convierta este formato a un objeto `timedelta`.

----------

## **Ejercicio 3: Análisis de carreras y participantes**

### **3.1 Carrera con mayor desnivel**

Implemente la función `carreraMayorDesnivelParticipante`, que recibe una lista de carreras, y el nombre y apellidos de un participante. Debe devolver la carrera con el mayor desnivel en la que haya participado.  
En caso de empate en el desnivel, se devolverá la carrera con menor distancia.

Si el participante no ha participado en ninguna carrera, la función debe devolver `None`.

----------

### **3.2 Tiempo medio por kilómetro**

Implemente la función `tiempoMedioCarrera`, que recibe una lista de carreras y el identificador de una carrera. Debe calcular el tiempo medio por kilómetro (en minutos) de todos los participantes de esa carrera.

**Consideraciones:**

-   Si no hay participantes o la distancia de la carrera es 0, la función debe devolver 0.

----------

### **3.3 Ganadores por categoría**

Implemente la función `ganadoresPorCategoria`, que recibe una lista de carreras y el identificador de una carrera. Debe devolver un diccionario donde:

-   Las claves representan las categorías (basadas en edad y sexo, por ejemplo, `"18-25-HOMBRE"`).
-   Los valores contienen el nombre y apellidos del ganador de cada categoría (es decir, el participante con menor duración).

**Categorías de edad:**

-   18-25 años
-   26-35 años
-   36-45 años
-   46-55 años
-   56-65 años
-   66 años o más

Cree una función auxiliar `calcular_categoria` que asigne a cada participante su categoría correspondiente.

----------
### Salida esperada 
```
Total de carreras: 11

Primeros tres registros:
Carrera 1:
 CarreraID: tr_cobre_23
 Localidad: Gerena
 Fecha y Hora: 2023-11-26 10:30
 Tipo: TRAIL
 Distancia: 15000 metros
 Desnivel: 750 metros
 Número de participantes: 64
Carrera 2:
 CarreraID: tr_cazalla_24
 Localidad: Cazalla de la Sierra
 Fecha y Hora: 2024-01-14 10:30
 Tipo: TRAIL
 Distancia: 13500 metros
 Desnivel: 600 metros
 Número de participantes: 59
Carrera 3:
 CarreraID: cr_lmcp_23
 Localidad: Castilleja de la Cuesta
 Fecha y Hora: 2023-09-23 21:45
 Tipo: CROSS
 Distancia: 7800 metros
 Desnivel: 200 metros
 Número de participantes: 99

Últimos tres registros:
Carrera 9:
 CarreraID: imd_sev_noct_23
 Localidad: Sevilla
 Fecha y Hora: 2023-09-29 22:00
 Tipo: ASFALTO
 Distancia: 8500 metros
 Desnivel: 10 metros
 Número de participantes: 82
Carrera 10:
 CarreraID: medmar_sev_24
 Localidad: Sevilla
 Fecha y Hora: 2024-01-28 09:00
 Tipo: ASFALTO
 Distancia: 21097 metros
 Desnivel: 10 metros
 Número de participantes: 72
Carrera 11:
 CarreraID: tr_lima_pedr_24
 Localidad: El Pedroso
 Fecha y Hora: 2024-03-03 09:30
 Tipo: TRAIL
 Distancia: 14000 metros
 Desnivel: 520 metros
 Número de participantes: 55

EJERCICIO 3.1:
----- Carrera con mayor desnivel de participante: --------
Alejandro Ruiz Blanco: Carrera Carrera(carrera_id='tr_rutagu_24', localidad='Guillena', fecha_hora=datetime.datetime(2024, 4, 14, 10, 0), tipo='TRAIL', distancia=27500, desnivel=800, participantes=[Participante(carrera_id='tr_rutagu_24', nombre='Sara', apellidos='Gómez Molina', edad=18, sexo='MUJER', duracion=datetime.timedelta(seconds=8971, microseconds=547800)), Participante(carrera_id='tr_rutagu_24', nombre='Alejandro', apellidos='Sánchez Hernández', edad=43, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9780, microseconds=603671)), Participante(carrera_id='tr_rutagu_24', nombre='Lucía', apellidos='Jiménez Navarro', edad=19, sexo='MUJER', duracion=datetime.timedelta(seconds=10721, microseconds=983724)), Participante(carrera_id='tr_rutagu_24', nombre='Pedro', apellidos='Álvarez Álvarez', edad=46, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9970, microseconds=258541)), Participante(carrera_id='tr_rutagu_24', nombre='Nuria', apellidos='Gómez Hernández', edad=56, sexo='MUJER', duracion=datetime.timedelta(seconds=8814, microseconds=318506)), Participante(carrera_id='tr_rutagu_24', nombre='Alejandro', apellidos='Rodríguez Blanco', edad=46, sexo='HOMBRE', duracion=datetime.timedelta(seconds=10252, microseconds=556738)), Participante(carrera_id='tr_rutagu_24', nombre='Fernando', apellidos='Fernández Gil', edad=39, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8890, microseconds=529918)), Participante(carrera_id='tr_rutagu_24', nombre='Luis', apellidos='García Martín', edad=30, sexo='HOMBRE', duracion=datetime.timedelta(seconds=10533, microseconds=28980)), Participante(carrera_id='tr_rutagu_24', nombre='Miguel', apellidos='Serrano Rodríguez', edad=35, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9336, microseconds=498318)), Participante(carrera_id='tr_rutagu_24', nombre='Paula', apellidos='Martínez Martínez', edad=34, sexo='MUJER', duracion=datetime.timedelta(seconds=8116, microseconds=859570)), Participante(carrera_id='tr_rutagu_24', nombre='Sara', apellidos='Hernández Moreno', edad=34, sexo='MUJER', duracion=datetime.timedelta(seconds=7959, microseconds=861384)), Participante(carrera_id='tr_rutagu_24', nombre='Pedro', apellidos='García Sánchez', edad=26, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9877, microseconds=731805)), Participante(carrera_id='tr_rutagu_24', nombre='Enrique', apellidos='Pérez Alonso', edad=51, sexo='HOMBRE', duracion=datetime.timedelta(seconds=10065, microseconds=114935)), Participante(carrera_id='tr_rutagu_24', nombre='Alejandro', apellidos='Pérez Díaz', edad=53, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9968, microseconds=625044)), Participante(carrera_id='tr_rutagu_24', nombre='María', apellidos='Gutiérrez Vázquez', edad=48, sexo='MUJER', duracion=datetime.timedelta(seconds=10233, microseconds=522933)), Participante(carrera_id='tr_rutagu_24', nombre='Luis', apellidos='Jiménez Serrano', edad=42, sexo='HOMBRE', duracion=datetime.timedelta(seconds=10432, microseconds=817200)), Participante(carrera_id='tr_rutagu_24', nombre='Fernando', apellidos='Fernández García', edad=57, sexo='HOMBRE', duracion=datetime.timedelta(seconds=10626, microseconds=209832)), Participante(carrera_id='tr_rutagu_24', nombre='Luis', apellidos='Pérez Moreno', edad=51, sexo='HOMBRE', duracion=datetime.timedelta(seconds=7820, microseconds=220837)), Participante(carrera_id='tr_rutagu_24', nombre='Miguel', apellidos='Torres Romero', edad=22, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8219, microseconds=712806)), Participante(carrera_id='tr_rutagu_24', nombre='Teresa', apellidos='Martínez Gutiérrez', edad=55, sexo='MUJER', duracion=datetime.timedelta(seconds=7578, microseconds=422270)), Participante(carrera_id='tr_rutagu_24', nombre='Fernando', apellidos='López Torres', edad=34, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9359, microseconds=998798)), Participante(carrera_id='tr_rutagu_24', nombre='Carlos', apellidos='Ramírez Vázquez', edad=35, sexo='HOMBRE', duracion=datetime.timedelta(seconds=7700, microseconds=827745)), Participante(carrera_id='tr_rutagu_24', nombre='Enrique', apellidos='Martínez Moreno', edad=50, sexo='HOMBRE', duracion=datetime.timedelta(seconds=10260, microseconds=502201)), Participante(carrera_id='tr_rutagu_24', nombre='Francisco', apellidos='Navarro Pérez', edad=24, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9241, microseconds=887292)), Participante(carrera_id='tr_rutagu_24', nombre='Alejandro', apellidos='Ruiz Blanco', edad=39, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9527, microseconds=972422)), Participante(carrera_id='tr_rutagu_24', nombre='Nuria', apellidos='Gil Gutiérrez', edad=25, sexo='MUJER', duracion=datetime.timedelta(seconds=10311, microseconds=290536)), Participante(carrera_id='tr_rutagu_24', nombre='Enrique', apellidos='Díaz Gutiérrez', edad=55, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8497, microseconds=115054)), Participante(carrera_id='tr_rutagu_24', nombre='David', apellidos='Ruiz Ramos', edad=54, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9903, microseconds=804144)), Participante(carrera_id='tr_rutagu_24', nombre='Pilar', apellidos='Jiménez Gómez', edad=47, sexo='MUJER', duracion=datetime.timedelta(seconds=9234, microseconds=976013)), Participante(carrera_id='tr_rutagu_24', nombre='Carlos', apellidos='Gómez Domínguez', edad=35, sexo='HOMBRE', duracion=datetime.timedelta(seconds=7847, microseconds=593863)), Participante(carrera_id='tr_rutagu_24', nombre='Alejandro', apellidos='García Gómez', edad=23, sexo='HOMBRE', duracion=datetime.timedelta(seconds=7750, microseconds=159609)), Participante(carrera_id='tr_rutagu_24', nombre='Carmen', apellidos='Fernández Navarro', edad=54, sexo='MUJER', duracion=datetime.timedelta(seconds=7934, microseconds=203099)), Participante(carrera_id='tr_rutagu_24', nombre='Laura', apellidos='Martín Álvarez', edad=41, sexo='MUJER', duracion=datetime.timedelta(seconds=9323, microseconds=515714)), Participante(carrera_id='tr_rutagu_24', nombre='Manuel', apellidos='Jiménez Vázquez', edad=57, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9007, microseconds=920899)), Participante(carrera_id='tr_rutagu_24', nombre='Raúl', apellidos='Fernández Domínguez', edad=36, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8740, microseconds=950779)), Participante(carrera_id='tr_rutagu_24', nombre='Enrique', apellidos='Gutiérrez Gutiérrez', edad=23, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8705, microseconds=423718)), Participante(carrera_id='tr_rutagu_24', nombre='Álvaro', apellidos='Álvarez Molina', edad=48, sexo='HOMBRE', duracion=datetime.timedelta(seconds=7903, microseconds=261530)), Participante(carrera_id='tr_rutagu_24', nombre='Manuel', apellidos='Ramos Torres', edad=32, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8559, microseconds=883730)), Participante(carrera_id='tr_rutagu_24', nombre='Francisco', apellidos='García Díaz', edad=39, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8978, microseconds=435188)), Participante(carrera_id='tr_rutagu_24', nombre='Javier', apellidos='Pérez Fernández', edad=48, sexo='HOMBRE', duracion=datetime.timedelta(seconds=7591, microseconds=311364)), Participante(carrera_id='tr_rutagu_24', nombre='Manuel', apellidos='Serrano Alonso', edad=29, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8279, microseconds=343597)), Participante(carrera_id='tr_rutagu_24', nombre='Enrique', apellidos='Martínez Gómez', edad=24, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9391, microseconds=115754)), Participante(carrera_id='tr_rutagu_24', nombre='Enrique', apellidos='Martínez Rodríguez', edad=18, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8105, microseconds=1974)), Participante(carrera_id='tr_rutagu_24', nombre='Lucía', apellidos='Navarro Álvarez', edad=24, sexo='MUJER', duracion=datetime.timedelta(seconds=10139, microseconds=44697)), Participante(carrera_id='tr_rutagu_24', nombre='Pilar', apellidos='Ramírez Hernández', edad=34, sexo='MUJER', duracion=datetime.timedelta(seconds=10241, microseconds=973696)), Participante(carrera_id='tr_rutagu_24', nombre='Sara', apellidos='Pérez Ruiz', edad=40, sexo='MUJER', duracion=datetime.timedelta(seconds=9380, microseconds=924190)), Participante(carrera_id='tr_rutagu_24', nombre='Antonio', apellidos='Martín Jiménez', edad=56, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8949, microseconds=35955)), Participante(carrera_id='tr_rutagu_24', nombre='Carlos', apellidos='Domínguez García', edad=20, sexo='HOMBRE', duracion=datetime.timedelta(seconds=10673, microseconds=921693)), Participante(carrera_id='tr_rutagu_24', nombre='David', apellidos='Jiménez Fernández', edad=39, sexo='HOMBRE', duracion=datetime.timedelta(seconds=8016, microseconds=749420)), Participante(carrera_id='tr_rutagu_24', nombre='Francisco', apellidos='Álvarez Molina', edad=44, sexo='HOMBRE', duracion=datetime.timedelta(seconds=9145, microseconds=113878)), Participante(carrera_id='tr_rutagu_24', nombre='Ana', apellidos='Ramos Martínez', edad=19, sexo='MUJER', duracion=datetime.timedelta(seconds=9232, microseconds=181316)), Participante(carrera_id='tr_rutagu_24', nombre='Miguel', apellidos='Jiménez Martín', edad=18, sexo='HOMBRE', duracion=datetime.timedelta(seconds=7988, microseconds=867901))])
Elena Blanco Vázquez: Carrera Carrera(carrera_id='tr_cobre_23', localidad='Gerena', fecha_hora=datetime.datetime(2023, 11, 26, 10, 30), tipo='TRAIL', distancia=15000, desnivel=750, participantes=[Participante(carrera_id='tr_cobre_23', nombre='Antonio', apellidos='Ruiz Ramos', edad=50, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5286, microseconds=305983)), Participante(carrera_id='tr_cobre_23', nombre='Pilar', apellidos='Ramos Álvarez', edad=52, sexo='MUJER', duracion=datetime.timedelta(seconds=4634, microseconds=651263)), Participante(carrera_id='tr_cobre_23', nombre='Pedro', apellidos='Domínguez Ruiz', edad=22, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5265, microseconds=672413)), Participante(carrera_id='tr_cobre_23', nombre='Sara', apellidos='Navarro Díaz', edad=53, sexo='MUJER', duracion=datetime.timedelta(seconds=4993, microseconds=107446)), Participante(carrera_id='tr_cobre_23', nombre='Ana', apellidos='Gil Ramos', edad=57, sexo='MUJER', duracion=datetime.timedelta(seconds=5294, microseconds=923063)), Participante(carrera_id='tr_cobre_23', nombre='Carlos', apellidos='Serrano Torres', edad=36, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5741, microseconds=343167)), Participante(carrera_id='tr_cobre_23', nombre='Juan', apellidos='Jiménez García', edad=22, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4886, microseconds=273364)), Participante(carrera_id='tr_cobre_23', nombre='Luis', apellidos='Pérez Gómez', edad=19, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5413, microseconds=933086)), Participante(carrera_id='tr_cobre_23', nombre='Fernando', apellidos='Moreno Moreno', edad=20, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5704, microseconds=692418)), Participante(carrera_id='tr_cobre_23', nombre='Laura', apellidos='Gutiérrez Blanco', edad=27, sexo='MUJER', duracion=datetime.timedelta(seconds=4912, microseconds=744540)), Participante(carrera_id='tr_cobre_23', nombre='Manuel', apellidos='Moreno López', edad=40, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5052, microseconds=542012)), Participante(carrera_id='tr_cobre_23', nombre='Ana', apellidos='Blanco Vázquez', edad=21, sexo='MUJER', duracion=datetime.timedelta(seconds=5692, microseconds=47886)), Participante(carrera_id='tr_cobre_23', nombre='Álvaro', apellidos='García Muñoz', edad=27, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4283, microseconds=914187)), Participante(carrera_id='tr_cobre_23', nombre='Teresa', apellidos='Moreno Ramírez', edad=46, sexo='MUJER', duracion=datetime.timedelta(seconds=5498, microseconds=717354)), Participante(carrera_id='tr_cobre_23', nombre='Antonio', apellidos='Hernández Ramos', edad=26, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4362, microseconds=40443)), Participante(carrera_id='tr_cobre_23', nombre='Javier', apellidos='García Hernández', edad=50, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4472, microseconds=719611)), Participante(carrera_id='tr_cobre_23', nombre='Álvaro', apellidos='Martín Martín', edad=51, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5224, microseconds=166647)), Participante(carrera_id='tr_cobre_23', nombre='Manuel', apellidos='Gil Molina', edad=19, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5748, microseconds=354076)), Participante(carrera_id='tr_cobre_23', nombre='Elena', apellidos='Blanco Vázquez', edad=46, sexo='MUJER', duracion=datetime.timedelta(seconds=5741, microseconds=607873)), Participante(carrera_id='tr_cobre_23', nombre='Luis', apellidos='Navarro Navarro', edad=24, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4938, microseconds=244560)), Participante(carrera_id='tr_cobre_23', nombre='Álvaro', apellidos='Blanco Díaz', edad=54, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5645, microseconds=958157)), Participante(carrera_id='tr_cobre_23', nombre='Pedro', apellidos='Jiménez Domínguez', edad=49, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4543, microseconds=904817)), Participante(carrera_id='tr_cobre_23', nombre='Francisco', apellidos='García Díaz', edad=39, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4890, microseconds=146466)), Participante(carrera_id='tr_cobre_23', nombre='Francisco', apellidos='Torres Romero', edad=48, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5861, microseconds=71851)), Participante(carrera_id='tr_cobre_23', nombre='María', apellidos='Gutiérrez Vázquez', edad=48, sexo='MUJER', duracion=datetime.timedelta(seconds=5585, microseconds=376145)), Participante(carrera_id='tr_cobre_23', nombre='Carlos', apellidos='Álvarez Gutiérrez', edad=51, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5492, microseconds=573622)), Participante(carrera_id='tr_cobre_23', nombre='Juan', apellidos='Álvarez Díaz', edad=23, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5723, microseconds=323871)), Participante(carrera_id='tr_cobre_23', nombre='David', apellidos='Rodríguez Ruiz', edad=30, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4156, microseconds=848791)), Participante(carrera_id='tr_cobre_23', nombre='Lucía', apellidos='Alonso Muñoz', edad=25, sexo='MUJER', duracion=datetime.timedelta(seconds=4515, microseconds=113716)), Participante(carrera_id='tr_cobre_23', nombre='Álvaro', apellidos='Martínez Martínez', edad=52, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4161, microseconds=943516)), Participante(carrera_id='tr_cobre_23', nombre='Luis', apellidos='Fernández Moreno', edad=57, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4440, microseconds=568271)), Participante(carrera_id='tr_cobre_23', nombre='Javier', apellidos='Gil Sánchez', edad=58, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4596, microseconds=912885)), Participante(carrera_id='tr_cobre_23', nombre='Alicia', apellidos='Gómez Ramírez', edad=43, sexo='MUJER', duracion=datetime.timedelta(seconds=4812, microseconds=116475)), Participante(carrera_id='tr_cobre_23', nombre='Alejandro', apellidos='Molina Sánchez', edad=30, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4251, microseconds=3209)), Participante(carrera_id='tr_cobre_23', nombre='Luis', apellidos='Serrano Torres', edad=52, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4909, microseconds=715732)), Participante(carrera_id='tr_cobre_23', nombre='Raúl', apellidos='Torres Hernández', edad=18, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5782, microseconds=689411)), Participante(carrera_id='tr_cobre_23', nombre='Marta', apellidos='Pérez Gutiérrez', edad=49, sexo='MUJER', duracion=datetime.timedelta(seconds=4894, microseconds=440152)), Participante(carrera_id='tr_cobre_23', nombre='Martina', apellidos='García Serrano', edad=33, sexo='MUJER', duracion=datetime.timedelta(seconds=4318, microseconds=381977)), Participante(carrera_id='tr_cobre_23', nombre='Raúl', apellidos='Díaz Sánchez', edad=19, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4592, microseconds=780893)), Participante(carrera_id='tr_cobre_23', nombre='Elena', apellidos='Serrano Navarro', edad=48, sexo='MUJER', duracion=datetime.timedelta(seconds=5759, microseconds=924407)), Participante(carrera_id='tr_cobre_23', nombre='Elena', apellidos='Molina Ramos', edad=45, sexo='MUJER', duracion=datetime.timedelta(seconds=5261, microseconds=446812)), Participante(carrera_id='tr_cobre_23', nombre='Teresa', apellidos='Alonso Gil', edad=24, sexo='MUJER', duracion=datetime.timedelta(seconds=4424, microseconds=664528)), Participante(carrera_id='tr_cobre_23', nombre='Carmen', apellidos='Moreno Ramos', edad=45, sexo='MUJER', duracion=datetime.timedelta(seconds=4822, microseconds=876684)), Participante(carrera_id='tr_cobre_23', nombre='Álvaro', apellidos='García Blanco', edad=57, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5569, microseconds=364791)), Participante(carrera_id='tr_cobre_23', nombre='Raúl', apellidos='Blanco Domínguez', edad=18, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4383, microseconds=284612)), Participante(carrera_id='tr_cobre_23', nombre='Manuel', apellidos='Díaz Sánchez', edad=18, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4306, microseconds=522004)), Participante(carrera_id='tr_cobre_23', nombre='Fernando', apellidos='López Torres', edad=34, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5142, microseconds=908435)), Participante(carrera_id='tr_cobre_23', nombre='Álvaro', apellidos='Gil Alonso', edad=26, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5624, microseconds=449059)), Participante(carrera_id='tr_cobre_23', nombre='Carlos', apellidos='Gutiérrez Domínguez', edad=19, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5634, microseconds=237297)), Participante(carrera_id='tr_cobre_23', nombre='Pilar', apellidos='Martín Ramírez', edad=52, sexo='MUJER', duracion=datetime.timedelta(seconds=5099, microseconds=342738)), Participante(carrera_id='tr_cobre_23', nombre='Carlos', apellidos='Gómez Domínguez', edad=35, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4287, microseconds=869380)), Participante(carrera_id='tr_cobre_23', nombre='Manuel', apellidos='Fernández Gutiérrez', edad=24, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5118, microseconds=119723)), Participante(carrera_id='tr_cobre_23', nombre='Laura', apellidos='Alonso Jiménez', edad=34, sexo='MUJER', duracion=datetime.timedelta(seconds=5804, microseconds=702699)), Participante(carrera_id='tr_cobre_23', nombre='Fernando', apellidos='Álvarez López', edad=23, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4322, microseconds=851297)), Participante(carrera_id='tr_cobre_23', nombre='Martina', apellidos='Alonso Moreno', edad=58, sexo='MUJER', duracion=datetime.timedelta(seconds=5392, microseconds=731809)), Participante(carrera_id='tr_cobre_23', nombre='Miguel', apellidos='Domínguez Ramos', edad=47, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5144, microseconds=957097)), Participante(carrera_id='tr_cobre_23', nombre='Luis', apellidos='Álvarez Álvarez', edad=28, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4288, microseconds=570444)), Participante(carrera_id='tr_cobre_23', nombre='Pedro', apellidos='Romero Romero', edad=31, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4561, microseconds=802400)), Participante(carrera_id='tr_cobre_23', nombre='Francisco', apellidos='García González', edad=41, sexo='HOMBRE', duracion=datetime.timedelta(seconds=4324, microseconds=740667)), Participante(carrera_id='tr_cobre_23', nombre='Raúl', apellidos='Hernández Sánchez', edad=25, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5037, microseconds=890434)), Participante(carrera_id='tr_cobre_23', nombre='Fernando', apellidos='Navarro Gómez', edad=46, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5179, microseconds=315815)), Participante(carrera_id='tr_cobre_23', nombre='Pilar', apellidos='Pérez Vázquez', edad=49, sexo='MUJER', duracion=datetime.timedelta(seconds=4378, microseconds=184192)), Participante(carrera_id='tr_cobre_23', nombre='Luis', apellidos='Blanco Pérez', edad=51, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5545, microseconds=625455)), Participante(carrera_id='tr_cobre_23', nombre='Luis', apellidos='Jiménez Ruiz', edad=47, sexo='HOMBRE', duracion=datetime.timedelta(seconds=5552, microseconds=531386))])

EJERCICIO 3.2:
----- Tiempo medio de carrera: --------
tr_cobre_23: 5.577982387395834
tr_cazalla_24: 5.529027828750783
cr_lmcp_23: 5.481540259388765
imd_sev_sanpab_24: 5.5086215160784295
imd_sev_marlui_24: 5.483730391593405
imd_sev_tam_24: 5.579334107960785
cr_esqui_24: 5.511044962373148
tr_rutagu_24: 5.525579633811189
imd_sev_noct_23: 5.561806153132473
medmar_sev_24: 5.404397990290442
tr_lima_pedr_24: 5.408978925909092

EJERCICIO 3.3:
----- Ganadores por categoría: --------
tr_cobre_23: {'46-55-HOMBRE': 'Martínez Martínez, Álvaro', '46-55-MUJER': 'Pérez Vázquez, Pilar', '18-25-HOMBRE': 'Díaz Sánchez, Manuel', '56-65-MUJER': 'Gil Ramos, Ana', '36-45-HOMBRE': 'García González, Francisco', '26-35-MUJER': 'García Serrano, Martina', '18-25-MUJER': 'Alonso Gil, Teresa', '26-35-HOMBRE': 'Rodríguez Ruiz, David', '56-65-HOMBRE': 'Fernández Moreno, Luis', '36-45-MUJER': 'Gómez Ramírez, Alicia'}
tr_cazalla_24: {'46-55-HOMBRE': 'Gil Gutiérrez, Antonio', '46-55-MUJER': 'Sánchez Torres, Carmen', '26-35-MUJER': 'Navarro Ruiz, Laura', '26-35-HOMBRE': 'Navarro Ramírez, Álvaro', '56-65-MUJER': 'Álvarez González, Sofía', '36-45-MUJER': 'García Muñoz, Marta', '18-25-HOMBRE': 'Martínez Rodríguez, Enrique', '18-25-MUJER': 'Torres Fernández, Sofía', '36-45-HOMBRE': 'Fernández Jiménez, Carlos'}
cr_lmcp_23: {'36-45-HOMBRE': 'Sánchez Serrano, Álvaro', '46-55-HOMBRE': 'Gil Moreno, Manuel', '26-35-HOMBRE': 'Gómez Rodríguez, Juan', '26-35-MUJER': 'González Sánchez, Marta', '18-25-HOMBRE': 'López Fernández, Alejandro', '46-55-MUJER': 'Ramos Ramos, Elena', '36-45-MUJER': 'Romero Sánchez, Carmen', '18-25-MUJER': 'Torres Fernández, Sofía', '56-65-HOMBRE': 'Muñoz Álvarez, David', '56-65-MUJER': 'Moreno Torres, Martina'}
imd_sev_sanpab_24: {'36-45-MUJER': 'Gutiérrez Domínguez, Laura', '26-35-MUJER': 'García Serrano, Martina', '18-25-HOMBRE': 'Torres Jiménez, Álvaro', '56-65-MUJER': 'Serrano Jiménez, Elena', '26-35-HOMBRE': 'Fernández Moreno, Luis', '36-45-HOMBRE': 'Moreno Muñoz, Miguel', '56-65-HOMBRE': 'Gómez Alonso, Pedro', '46-55-HOMBRE': 'Domínguez Gómez, Antonio', '18-25-MUJER': 'Torres Fernández, Sofía', '46-55-MUJER': 'Gómez Rodríguez, Ana'}
imd_sev_marlui_24: {'56-65-HOMBRE': 'Fernández Martín, Juan', '46-55-HOMBRE': 'Domínguez Gómez, Antonio', '36-45-HOMBRE': 'Moreno Muñoz, Miguel', '26-35-MUJER': 'Sánchez Navarro, Ana', '46-55-MUJER': 'Martínez Gutiérrez, Teresa', '26-35-HOMBRE': 'Gutiérrez Moreno, Miguel', '18-25-HOMBRE': 'Muñoz Serrano, Manuel', '36-45-MUJER': 'Romero Sánchez, Carmen', '18-25-MUJER': 'Alonso Muñoz, Lucía', '56-65-MUJER': 'Molina Alonso, Elena'}
imd_sev_tam_24: {'56-65-HOMBRE': 'Fernández Moreno, Luis', '36-45-MUJER': 'Gil Álvarez, Pilar', '46-55-MUJER': 'Vázquez Gómez, Nuria', '36-45-HOMBRE': 'Gil Romero, Pedro', '26-35-MUJER': 'Martínez Martínez, Paula', '46-55-HOMBRE': 'Ramírez Ramos, Pedro', '56-65-MUJER': 'Molina Alonso, Elena', '18-25-HOMBRE': 'López Serrano, Miguel', '18-25-MUJER': 'Martínez Moreno, Martina', '26-35-HOMBRE': 'Navarro Romero, Manuel'}
cr_esqui_24: {'46-55-MUJER': 'Gómez Moreno, Laura', '46-55-HOMBRE': 'Torres Pérez, Raúl', '36-45-MUJER': 'Ruiz Alonso, María', '18-25-HOMBRE': 'Alonso Hernández, Carlos', '26-35-MUJER': 'Díaz Rodríguez, Ana', '26-35-HOMBRE': 'Navarro Romero, Manuel', '56-65-HOMBRE': 'Fernández Martín, Juan', '56-65-MUJER': 'García Domínguez, Ana', '36-45-HOMBRE': 'González Rodríguez, Enrique', '18-25-MUJER': 'Romero Hernández, Martina'}
tr_rutagu_24: {'18-25-MUJER': 'Gómez Molina, Sara', '36-45-HOMBRE': 'Jiménez Fernández, David', '46-55-HOMBRE': 'Pérez Fernández, Javier', '56-65-MUJER': 'Gómez Hernández, Nuria', '26-35-HOMBRE': 'Ramírez Vázquez, Carlos', '26-35-MUJER': 'Hernández Moreno, Sara', '46-55-MUJER': 'Martínez Gutiérrez, Teresa', '56-65-HOMBRE': 'Martín Jiménez, Antonio', '18-25-HOMBRE': 'García Gómez, Alejandro', '36-45-MUJER': 'Martín Álvarez, Laura'}
imd_sev_noct_23: {'56-65-HOMBRE': 'Gómez Alonso, Pedro', '26-35-MUJER': 'Gutiérrez Blanco, Laura', '18-25-HOMBRE': 'Muñoz Serrano, Manuel', '36-45-HOMBRE': 'González Rodríguez, Enrique', '18-25-MUJER': 'Ramírez Domínguez, Ana', '26-35-HOMBRE': 'García Muñoz, Álvaro', '36-45-MUJER': 'López Molina, Nuria', '46-55-HOMBRE': 'Gil Moreno, Manuel', '46-55-MUJER': 'Rodríguez Gil, María', '56-65-MUJER': 'García Fernández, Sara'}
medmar_sev_24: {'18-25-HOMBRE': 'Domínguez Blanco, Álvaro', '26-35-HOMBRE': 'Moreno Ruiz, Juan', '18-25-MUJER': 'Gutiérrez Ruiz, Teresa', '36-45-HOMBRE': 'González Rodríguez, Enrique', '46-55-MUJER': 'Ramos Ramos, Elena', '46-55-HOMBRE': 'González Ruiz, Miguel', '36-45-MUJER': 'Gutiérrez Domínguez, Laura', '56-65-MUJER': 'Gil Ramos, Ana', '56-65-HOMBRE': 'Fernández Martín, Juan', '26-35-MUJER': 'Pérez Ramírez, Carmen'}
tr_lima_pedr_24: {'18-25-HOMBRE': 'Torres Romero, Miguel', '56-65-HOMBRE': 'Pérez Álvarez, Enrique', '46-55-HOMBRE': 'Pérez Fernández, Javier', '36-45-HOMBRE': 'Gil Romero, Pedro', '36-45-MUJER': 'Gutiérrez Fernández, Lucía', '56-65-MUJER': 'Gómez Hernández, Nuria', '26-35-MUJER': 'García Serrano, Martina', '46-55-MUJER': 'Vázquez Moreno, Teresa', '26-35-HOMBRE': 'García Muñoz, Álvaro', '18-25-MUJER': 'Romero Domínguez, Carmen'}
```

