# Corte 1 — Fase 1: jerarquía, Trie y árbol de búsqueda

## Qué se entrega el día del parcial (todo junto, una sola fecha — la publica Teams)

| Pieza | Dónde está en este repo | Cuánto pesa |
|---|---|---|
| Análisis de requerimientos de la pareja (1 solo documento) | `requerimientos/PCIA5020_Requerimientos_Pareja_NN_AAAA-MM-DD` | 40 % (4 pts) |
| Código de la Fase 1 (.py que corre entero) | `src/PCIA5020_Proyecto_Fase1_Pareja_NN_AAAA-MM-DD.py` | 60 % (6 pts) |
| Datos de prueba (≥3 zonas, ≥40 estaciones, 1 zona ≥10, ≥60 tramos, ≥20 secuencias con ≥5 inválidas) | `datos/` | requisito de admisión |
| Tabla de comparación (árbol vs. recorrido secuencial, con la resta escrita) | `pruebas/tabla_comparacion.md` | requisito de admisión |

**El montículo NO va en este corte** — eso es Fase 2, con Dijkstra.

## Criterios de aceptación que se ejecutan delante del docente

1. Listar las estaciones de una zona: salen todas las de esa zona y ninguna de otra.
2. Autocompletar a partir de tres letras: nombres que empiezan así, o lista vacía si no hay ninguno.
3. Buscar una estación por código en el árbol de búsqueda: la encuentra y reporta comparaciones.
4. La misma búsqueda recorriendo la lista completa: reporta su propio número de comparaciones.
5. Casos de borde: código que no existe, autocompletar con cadena vacía, listar una zona sin
   estaciones — ninguno lanza excepción sin capturar.

## Lo que devuelve la entrega sin calificar

- El archivo no corre entero.
- Falta el encabezado de control de cambios o el nombre normalizado (sin tildes ni espacios).
- Se usa `networkx` o cualquier librería que ya resuelva la estructura.
- La tabla de comparación trae un solo número, sin la resta escrita.
- El Trie está implementado como un diccionario de cadenas completas (eso es un diccionario, no
  un Trie).
- La red de prueba no llega a los mínimos.

Ver el checklist completo de las 9 comprobaciones en
`requerimientos/checklist_antes_de_entregar.md`.
