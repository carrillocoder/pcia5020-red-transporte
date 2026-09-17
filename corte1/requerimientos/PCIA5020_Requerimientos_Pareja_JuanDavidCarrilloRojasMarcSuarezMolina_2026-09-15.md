# Análisis de requerimientos — Red de transporte de la ciudad

**Pareja NN** · Juan David Carrillo Rojas y Marc Suárez Molina · 2026-09-15

## 1. Contexto y alcance (20 %)

El sistema simula el sistema de consulta y control de una red de transporte masivo de la
ciudad. La red está organizada por zonas, cada zona agrupa estaciones, y las estaciones se
conectan entre sí por tramos que toman un tiempo determinado en minutos. Los usuarios
consultan cómo llegar de una estación a otra, y cada tarjeta va dejando una secuencia de
eventos (entrar, transbordar, salir, recargar) que el sistema debe poder validar.

Qué NO hace el sistema:

- NO persiste en base de datos: lee y escribe archivos de texto plano (zonas, estaciones,
  tramos y secuencias de eventos).
- NO tiene autenticación de usuario y contraseña: el rol (consultante u operador) se pasa
  como parámetro al arrancar, no se valida contra ninguna credencial.
- NO modela horarios ni frecuencias: el tiempo de cada tramo es un número entero de minutos
  fijo, no una tabla de horarios por hora del día.
- NO calcula tarifas ni cobra: ningún requerimiento maneja dinero.
- NO muestra mapas ni gráficas: los resultados se presentan como texto (listas, números de
  comparaciones, rutas), no como una interfaz visual.
- NO reconoce ningún evento distinto de los cuatro del alfabeto fijo (entrar, transbordar,
  salir, recargar); no se añadió un quinto evento.
- NO corrige datos de origen inconsistentes: si un tramo referencia una estación que no
  existe, esa línea del archivo se rechaza al cargar, no se "adivina" a qué estación se
  refería.

## 2. Actores (10 %)

**USUARIO CONSULTANTE:** busca estaciones por código y por nombre (autocompletado), pide la
lista de estaciones de una zona y consulta rutas entre dos estaciones. NO carga archivos de
datos ni modifica la red.

**OPERADOR DE RED:** hace todo lo del usuario consultante, y además carga los archivos de
zonas, estaciones, tramos y secuencias, y corre el generador de datos de prueba. NO puede
editar una estación ya cargada de forma individual: para cambiar la red se corrige el archivo
de origen y se vuelve a cargar completa.

El sistema no distingue a los dos por contraseña: el rol se pasa como parámetro al arrancar
(ver la sección de alcance).

## 3. Requerimientos funcionales (25 %)

| ID | Requerimiento | Fase |
|---|---|---|
| RF-01 | El sistema debe organizar la red como una jerarquía ciudad → zonas → estaciones y recorrerla. | 1 |
| RF-02 | El sistema debe autocompletar nombres de estación usando un Trie. | 1 |
| RF-03 | El sistema debe buscar una estación por su código usando un árbol de búsqueda binaria y reportar cuántas comparaciones costó. | 1 |
| RF-04 | El sistema debe buscar esa misma estación recorriendo la lista completa y reportar cuántas comparaciones costó. | 1 |
| RF-05 | El sistema debe representar la red como un grafo ponderado por el tiempo de cada tramo. | 2 |
| RF-06 | El sistema debe responder si existe algún camino entre dos estaciones, usando un recorrido en profundidad (DFS). | 2 |
| RF-07 | El sistema debe encontrar el camino con menos tramos entre dos estaciones, usando un recorrido en anchura (BFS). | 2 |
| RF-08 | El sistema debe construir un montículo de mínimos sobre los tramos, ordenado por su tiempo en minutos. | 2 |
| RF-09 | El sistema debe usar el montículo como cola de prioridad del algoritmo de Dijkstra, para encontrar la ruta más rápida entre dos estaciones y su tiempo total. | 2 |
| RF-10 | El sistema debe comparar memoria y tiempo entre la matriz de adyacencia y la lista de adyacencia, sobre la misma red. | 2 |
| RF-11 | El sistema debe modelar el viaje de una tarjeta como un autómata (estados, alfabeto de eventos, transiciones, estado inicial y estados de aceptación). | 3 |
| RF-12 | El sistema debe validar si una secuencia de eventos es un viaje correcto, e indicar en qué evento falló si no lo es. | 3 |
| RF-13 | El sistema debe modelar una variante del viaje como un autómata no determinista y convertirla a un autómata determinista equivalente. | 3 |
| RF-14 | El sistema debe reportar cuántas secuencias de un archivo de prueba fueron rechazadas, agrupadas por el evento en el que fallaron. | 3 |

## 4. Datos (15 %)

**Estación**

| Campo | Tipo | Obligatorio | Qué se valida |
|---|---|---|---|
| codigo | entero | sí | Es entero (y no texto) porque es la clave con la que se ordena el árbol de búsqueda binaria: si fuera texto, la estación "100" quedaría ordenada antes que la "20" por comparación de caracteres, no por valor numérico. No se repite. |
| nombre | texto | sí | No puede estar vacío; es lo que indexa el Trie de autocompletado. |
| zona | texto | sí | Debe existir como código de una zona ya definida; si no, la estación se rechaza al cargar. |

**Zona**

| Campo | Tipo | Obligatorio | Qué se valida |
|---|---|---|---|
| codigo | texto | sí | No se repite. |
| nombre | texto | sí | No puede estar vacío. |

**Tramo**

| Campo | Tipo | Obligatorio | Qué se valida |
|---|---|---|---|
| origen | entero | sí | Debe existir como código de una estación ya cargada. |
| destino | entero | sí | Debe existir como código de una estación ya cargada, y ser distinto de origen. |
| minutos | entero | sí | Debe ser mayor que 0: un tramo de 0 o negativos minutos se rechaza porque rompería el cálculo de la ruta más rápida (Dijkstra) en la Fase 2. |

**Secuencia de eventos** *(dato de la Fase 3, generado desde este corte)*

| Campo | Tipo | Obligatorio | Qué se valida |
|---|---|---|---|
| id | texto | sí | No se repite. |
| eventos | lista de texto | sí | Cada evento debe ser uno de: entrar, transbordar, salir, recargar. Un evento fuera de esos cuatro no rechaza el archivo: hace que esa secuencia se clasifique como inválida (Fase 3). |

**Tamaño de la red de prueba:** 5 zonas (una de ellas, "ZonaVacia", queda deliberadamente sin
estaciones para poder probar el caso de borde de listar una zona vacía), 48 estaciones (la
zona Norte tiene 14), 70 tramos y 24 secuencias de eventos (18 válidas y 6 inválidas) — todos
por encima de los mínimos exigidos (3 zonas, 40 estaciones con al menos una de 10 o más, 60
tramos, 20 secuencias con al menos 5 inválidas). Se generan con
`corte1/datos/generador_datos.py`, con una semilla fija para que sean reproducibles entre los
dos integrantes.

## 5. Restricciones técnicas (10 %)

1. Python 3. Las estructuras se implementan en el curso: no se permite resolver el problema
   con bibliotecas que ya lo resuelven (`networkx` y similares quedan fuera).
2. Los datos son simulados y los construye la pareja: un archivo de estaciones/zonas/tramos y
   otro de secuencias de eventos.
3. Mínimos de la red de prueba: al menos 3 zonas, 40 estaciones (una con 10 o más), 60 tramos y
   20 secuencias de eventos, de las cuales al menos 5 inválidas.
4. El tiempo de cada tramo es un número entero de minutos; no se modelan horarios ni
   frecuencias.
5. Toda entrega cumple el Estándar de Entregas de Código: nombre normalizado, encabezado de
   control de cambios y docstring por función.
6. **Restricción propia:** el generador de datos usa una semilla fija
   (`SEMILLA = 20260829` en `generador_datos.py`), PORQUE necesitamos poder reproducir
   exactamente la misma red de prueba entre los dos integrantes y entre distintas
   ejecuciones, sin tener que compartirnos manualmente los archivos generados cada vez que
   alguno corre el script.

## 6. Criterios de aceptación (20 %)

| RF | Qué se ejecuta | Qué debe salir |
|---|---|---|
| RF-01 | `listar_zona("Z1")` sobre la red de prueba (48 estaciones) | Las 14 estaciones de la zona Norte, ninguna de otra zona. Sobre la zona vacía (`listar_zona("Z5")`) devuelve una lista vacía, sin excepción. |
| RF-02 | `autocompletar("Pla")` | Los 4 nombres que empiezan por "Pla" (uno por zona: Plaza Norte 1, Plaza Sur 1, Plaza Centro 1, Plaza Occidente 1). `autocompletar("")` devuelve lista vacía, sin excepción. |
| RF-03 | `buscar_arbol(124)` sobre las 48 estaciones | Devuelve la estación 124 y reporta 1 comparación. Con el árbol balanceado, ninguna búsqueda cuesta más de 6 comparaciones (⌈log₂48⌉ = 6). `buscar_arbol(999999)` (código inexistente) devuelve `None` sin lanzar excepción. |
| RF-04 | `busqueda_secuencial(124)` sobre la misma red | Devuelve la misma estación y reporta 25 comparaciones. Diferencia: 25 − 1 = 24 comparaciones menos con el árbol de búsqueda. |
| RF-05 a RF-10 | Se definen y se prueban con números reales de ejecución al llegar al Corte 2 (grafo, DFS, BFS, montículo y Dijkstra sobre la red de 70 tramos ya generada). | Pendiente Corte 2. |
| RF-11 a RF-14 | Se definen y se prueban con las 24 secuencias ya generadas (18 válidas, 6 inválidas) al llegar al Corte 3 (autómata). | Pendiente Corte 3. |

## Requerimientos descartados y por qué

- Consideramos añadir un quinto evento al alfabeto, `reportar_fallo`, para que un operador
  pudiera marcar una tarjeta dañada directamente dentro de la secuencia de eventos. Lo
  descartamos porque el alcance de la Fase 3 solo pide validar secuencias ya registradas, no
  gestionar el estado físico de la tarjeta; añadirlo habría exigido una transición nueva desde
  cualquier estado hacia un estado de "tarjeta dañada", complicando el autómata sin que ningún
  criterio de aceptación del docente lo pidiera. Juan David lo propuso pensando en un caso de
  uso real de un sistema de transporte; Marc estuvo de acuerdo en descartarlo porque los
  criterios de aceptación de la Fase 3 solo evalúan las cuatro transiciones del alfabeto fijo.

---

**Nota de la pareja:** este documento parte de las estructuras ya implementadas en
`corte1/src/` y de los datos ya generados en `corte1/datos/`. Antes de sustentarlo, lean cada
sección los dos juntos: en la sustentación les preguntan por cualquiera de ellas, no solo por
la que cada uno redactó, y en particular por el requerimiento descartado de esta página —a
quien lo propuso y a quien lo aceptó. Si la conversación real que tuvieron fue distinta a la
que queda escrita aquí, ajústenla para que sea la que de verdad puedan explicar.
