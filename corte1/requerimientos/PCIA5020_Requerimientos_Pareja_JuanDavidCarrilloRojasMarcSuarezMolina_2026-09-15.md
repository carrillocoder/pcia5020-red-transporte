<!--
  PLANTILLA — bórrense estas notas antes de entregar.

  Regla de oro: escriban en el orden 1→6 de "Cómo se saca un análisis de requerimientos"
  (requerimientos → datos → criterios → alcance → actores → restricciones), pero el
  documento final va en ESTE orden (contexto, actores, RF, datos, restricciones, criterios).
  Ya está ordenado así abajo; solo tienen que llenarlo.

  Recuerden: se hace SENTADOS JUNTOS, discutiendo cada sección antes de escribirla.
  En la sustentación le preguntan a cualquiera de los dos por cualquier sección.

  Cuando terminen, exporten esto a .docx con el nombre exacto:
  PCIA5020_Requerimientos_Pareja_NN_AAAA-MM-DD.docx
  (reemplacen NN por el número de pareja y la fecha real de entrega)
-->

# Análisis de requerimientos — Red de transporte de la ciudad

**Pareja NN** · Juan David Carrillo Rojas y Marc Suárez · 2026-09-15

## 1. Contexto y alcance (20 %)

<!-- Dos frases de qué simula el sistema (pueden basarse en la sección 2 del documento base,
     no hay que inventar). Después la parte que SÍ se califica: contesten estas preguntas
     mirando SU lista de requerimientos (sección 3) y escriban un párrafo con lo que el
     sistema NO hace. -->

El sistema simula... *(complete)*

Qué NO hace el sistema (mínimo tres exclusiones, cada una con su porqué si no es evidente):

- ¿Alguno de sus RF guarda algo en base de datos? Si no → el sistema NO persiste en base de datos *(ajusten la frase)*.
- ¿Alguno pide usuario y contraseña? Si no → el sistema NO tiene autenticación.
- ¿Alguno maneja fechas u horas? Si no → el sistema NO modela horarios ni frecuencias.
- ¿Alguno cobra o calcula plata? Si no → el sistema NO calcula tarifas.
- ¿Alguno dibuja algo? Si no → el sistema NO muestra mapas ni gráficas.
- El alfabeto de eventos es fijo (entrar, transbordar, salir, recargar) → el sistema NO
  reconoce ningún otro evento *(a menos que decidan añadir uno propio: si lo hacen, decláren lo
  aquí y justifiquen qué transición nueva obliga a crear)*.
- *(Añadan una séptima exclusión propia, de algo que decidieron que el sistema no hace.)*

## 2. Actores (10 %)

<!-- Recorran sus RF y pregunten: ¿quién haría esto en la vida real? Agrupen. Necesitan al
     menos DOS actores distintos (normalmente alguien que solo consulta y alguien que además
     carga/modifica). Por cada uno: qué puede hacer y qué NO puede hacer. -->

**ACTOR 1 — *(nombre)*:** *(qué puede hacer)*. NO *(qué no puede hacer)*.

**ACTOR 2 — *(nombre)*:** *(qué puede hacer)*. NO *(qué no puede hacer)*.

## 3. Requerimientos funcionales (25 %)

<!-- Salen de partir, por punto y coma y por "y", la columna "Qué debe hacer el software" de
     las TRES fases del documento base (el análisis cubre todo el proyecto, aunque este corte
     solo entreguen el código de la Fase 1). "El sistema debe...", numerados, con su fase.
     Los de Fase 1 son prácticamente estos cuatro (verifiquen contra el documento base y
     ajusten la redacción si hace falta); COMPLETEN los de Fase 2 y Fase 3 ustedes. -->

| ID | Requerimiento | Fase |
|---|---|---|
| RF-01 | El sistema debe organizar la red como una jerarquía ciudad → zonas → estaciones y recorrerla. | 1 |
| RF-02 | El sistema debe autocompletar nombres de estación usando un Trie. | 1 |
| RF-03 | El sistema debe buscar una estación por su código usando un árbol de búsqueda binaria y reportar cuántas comparaciones costó. | 1 |
| RF-04 | El sistema debe buscar esa misma estación recorriendo la lista completa y reportar cuántas comparaciones costó. | 1 |
| RF-05 | *(Fase 2: conectividad — DFS)* | 2 |
| RF-06 | *(Fase 2: ruta con menos tramos — BFS)* | 2 |
| RF-07 | *(Fase 2: ruta más rápida con Dijkstra sobre un montículo propio)* | 2 |
| RF-08 | *(Fase 2: comparar memoria/tiempo entre matriz y lista de adyacencia)* | 2 |
| RF-09 | *(Fase 3: clasificar secuencia como válida/inválida)* | 3 |
| RF-10 | *(Fase 3: indicar en qué evento falló una secuencia inválida)* | 3 |
| RF-11 | *(Fase 3: reportar cuántas secuencias fueron rechazadas y por qué)* | 3 |

## 4. Datos (15 %)

<!-- Entidades = sustantivos de sus RF que SÍ se guardan (no las estructuras como "Trie" o
     "árbol", no los números calculados como "comparaciones"). Por cada entidad: campos con
     tipo, obligatoriedad y qué se valida. Justifiquen POR QUÉ ese tipo y no otro en al menos
     un campo. Los campos de Estación de abajo son los que ya usa el código de ejemplo en
     src/ — revísenlos, complétenlos o cámbienlos si deciden otra cosa (siempre que el código
     y el análisis queden coherentes entre sí). -->

**Estación**

| Campo | Tipo | Obligatorio | Qué se valida |
|---|---|---|---|
| codigo | entero | sí | *(¿por qué entero y no texto? — esta es la justificación que se pregunta en la sustentación)* |
| nombre | texto | sí | *(complete)* |
| zona | texto | sí | *(complete: tiene que existir como zona ya definida)* |

**Zona**

| Campo | Tipo | Obligatorio | Qué se valida |
|---|---|---|---|
| *(complete)* | | | |

**Tramo**

| Campo | Tipo | Obligatorio | Qué se valida |
|---|---|---|---|
| origen | entero | sí | tiene que existir como código de estación |
| destino | entero | sí | tiene que existir como código de estación |
| minutos | entero | sí | *(¿qué pasa con 0 o negativo?)* |

**Secuencia de eventos** *(para la Fase 3, pero los datos se generan desde ahora)*

| Campo | Tipo | Obligatorio | Qué se valida |
|---|---|---|---|
| id | texto | sí | no se repite |
| eventos | lista de texto | sí | cada evento debe ser uno de: entrar, transbordar, salir, recargar |

Tamaño de la red de prueba con la que van a trabajar: *(digan cuántas zonas, estaciones,
tramos y secuencias generaron — el generador en `datos/generador_datos.py` ya trae unos
valores por defecto por encima de los mínimos; escriban aquí los que realmente usaron)*.

## 5. Restricciones técnicas (10 %)

Las cinco del documento base (se copian tal cual):

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

Restricción(es) propia(s) — **obligatorio añadir al menos una, con su "porque"**:

- *(Ejemplo de forma, no de contenido: "La red de prueba tiene como máximo N estaciones,
  PORQUE...". No copien el ejemplo del documento 4 — tiene que ser una decisión suya.)*

## 6. Criterios de aceptación (20 %)

<!-- Por cada RF: qué línea se ejecuta y qué debe salir, CON NÚMEROS DE SU PROPIA RED. Los
     números de la tabla de abajo son de ejemplo/orientativos del formato — reemplácenlos por
     lo que realmente arroje su ejecución (ver corte1/pruebas/tabla_comparacion.md). -->

| RF | Qué se ejecuta | Qué debe salir |
|---|---|---|
| RF-01 | `listar_zona("...")` sobre la red de prueba | *(complete con su número real de estaciones en esa zona)* |
| RF-02 | `autocompletar("...")` con tres letras | *(nombres esperados, y lista vacía si no hay ninguno)* |
| RF-03 | `buscar_arbol(codigo)` | Devuelve la estación y reporta *(N)* comparaciones o menos |
| RF-04 | `busqueda_secuencial(codigo)` sobre la misma red | Devuelve la misma estación y reporta *(N)* comparaciones — la resta entre los dos queda escrita |
| RF-05..RF-11 | *(Fase 2 y 3 — se completan en esos cortes)* | |

## Requerimientos descartados y por qué

<!-- Obligatorio: en la sustentación se pregunta por esto, a quien lo propuso y a quien lo
     aceptó. Cuando los dos no estén de acuerdo en algo, elijan uno y dejen escrito por qué
     descartaron el otro. -->

- *(Ejemplo de forma: "Consideramos añadir un quinto evento 'reportar_fallo' al alfabeto, pero
  lo descartamos porque... Lo decidimos así: [quién lo propuso] propuso X, [quién lo aceptó]
  estuvo de acuerdo porque...")*
