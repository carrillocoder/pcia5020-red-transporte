# PCIA5020 — Proyecto: Red de transporte de la ciudad

Universidad Sergio Arboleda · Estructuras de Datos No Lineales · Periodo 2026-2
Docente: Christian Pinzón

**Integrantes:**
- Juan David Carrillo Rojas
- Mar Suárez

## Qué es esto

Este repositorio es el proyecto completo del curso: un sistema de consulta y control de una
red de transporte masivo (zonas → estaciones → tramos, y secuencias de eventos de tarjeta).
El proyecto crece en tres cortes, cada uno con sus propias estructuras obligatorias:

| Corte | Estructuras | Qué debe hacer el software |
|---|---|---|
| **Corte 1** (semanas 1-6) | Árbol N-ario, Trie, Árbol de búsqueda binaria | Jerarquía ciudad → zonas → estaciones; autocompletar con Trie; buscar estación por código con BST y comparar contra recorrido secuencial. |
| Corte 2 (semanas 7-11) | Grafo, lista/matriz de adyacencia, DFS, BFS, montículo, Dijkstra | Conectividad, ruta con menos tramos, ruta más rápida (Dijkstra + montículo propio), comparar matriz vs. lista. |
| Corte 3 (semanas 12-16) | AFD, AFN, máquina de estados | Modelar el viaje de una tarjeta como autómata y validar secuencias de eventos. |

Nada se abandona entre cortes: el árbol de búsqueda del Corte 1 es el que ubica las estaciones
que el Corte 2 conecta como grafo, y así sucesivamente.

## Estructura del repositorio

```
pcia5020-red-transporte/
├── corte1/               ← lo que se entrega y sustenta en el parcial del Corte 1
│   ├── requerimientos/   ← el análisis de requerimientos de la pareja (documento calificable)
│   ├── src/               ← el código de la Fase 1 (.py que se sustenta)
│   ├── datos/              ← generador y archivos de datos de prueba
│   └── pruebas/           ← tabla de comparación de comparaciones (árbol vs. recorrido)
├── corte2/                ← se completa durante el Corte 2 (grafo, Dijkstra, montículo)
└── corte3/                ← se completa durante el Corte 3 (autómatas)
```

## Cómo correr el Corte 1

```bash
cd corte1/datos
python3 generador_datos.py        # genera zonas.txt, estaciones.txt, tramos.txt, secuencias.txt
cd ../src
python3 PCIA5020_Proyecto_Fase1_Pareja_NN_AAAA-MM-DD.py
```

El script de la Fase 1 carga los datos generados, arma la jerarquía, el Trie y el árbol de
búsqueda, y corre una demo con los criterios de aceptación (listar zona, autocompletar,
buscar por código, comparar comparaciones, y los tres casos de borde).

## Antes de entregar — lo que falta por hacer ustedes dos

Este repositorio trae una base de código que **funciona**, pero **falta lo que solo ustedes
pueden decidir y explicar en la sustentación**:

1. **Renombrar los archivos** reemplazando `Pareja_NN_AAAA-MM-DD` por el número de pareja que
   les asigne el docente en Teams y la fecha real de entrega (en `src/`, `requerimientos/` y el
   nombre en los encabezados de control de cambios).
2. **Completar el análisis de requerimientos** en `corte1/requerimientos/` — está en formato
   plantilla, con la guía de qué va en cada sección, pero el contenido (los datos que deciden
   guardar, los criterios de aceptación con SUS números, el alcance, los actores) lo escriben
   ustedes dos, sentados juntos, discutiendo cada sección. **No es válido entregar la plantilla
   sin editar.**
3. **Revisar y entender todo el código**, no solo correrlo: en la sustentación les preguntan a
   cualquiera de los dos por cualquier parte del código y del análisis, no solo por lo que cada
   uno escribió.
4. **Ajustar los datos de prueba si quieren** (el generador ya cumple los mínimos, pero pueden
   cambiar cuántas zonas/estaciones/tramos generar, siempre respetando los mínimos del
   documento base: 3 zonas, 40 estaciones, una zona con 10 o más, 60 tramos, 20 secuencias con
   al menos 5 inválidas).
5. **Llenar la tabla de comparación** en `corte1/pruebas/tabla_comparacion.md` con los números
   reales que arroje su ejecución.
6. Antes de subir la versión final, pasar el checklist de
   `corte1/requerimientos/checklist_antes_de_entregar.md`.

## Flujo de trabajo sugerido con git

- Trabajen sobre una rama por persona o por tarea (`feature/analisis`, `feature/trie`, etc.) y
  únanla a `main` con un Pull Request que el otro revise — así los dos leen todo antes de
  entregarlo, que es justamente lo que pide el docente.
- Hagan commits pequeños y descriptivos a medida que avanzan en cada taller semanal.
