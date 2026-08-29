# Corte 2 — Fase 2: grafo, listas/matriz de adyacencia, DFS, BFS, montículo y Dijkstra

Pendiente por trabajar (semanas 7-11). Esta carpeta se completa durante el Corte 2.

## Estructuras obligatorias

Grafo, lista y matriz de adyacencia, DFS, BFS, montículo de mínimos, Dijkstra.

## Qué debe hacer el software (documento base)

- Representar la red como grafo ponderado por tiempo.
- Responder si dos estaciones están conectadas (DFS).
- Encontrar la ruta con menos tramos (BFS).
- Construir un montículo de mínimos sobre los tramos (ordenado por tiempo en minutos) y usarlo
  como cola de prioridad de Dijkstra para la ruta más rápida.
- Comparar memoria y tiempo entre matriz y lista de adyacencia.

## Costura con el Corte 1

El árbol de búsqueda binaria del Corte 1 (`corte1/src/`) es el que localiza las estaciones que
aquí se van a conectar como grafo — no se vuelve a escribir desde cero, se reutiliza.

## Estructura sugerida (a crear cuando empiecen)

```
corte2/
├── requerimientos/   ← actualización del análisis con RF-05..RF-08 ya con criterios reales
├── src/               ← PCIA5020_Proyecto_Fase2_Pareja_NN_AAAA-MM-DD.py
├── datos/             ← reutiliza o regenera tramos.txt si hace falta
└── pruebas/           ← comparación matriz vs. lista de adyacencia
```
