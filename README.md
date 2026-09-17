# PCIA5020 — Proyecto: Red de transporte de la ciudad

Universidad Sergio Arboleda · Estructuras de Datos No Lineales · Periodo 2026-2
Docente: Christian Pinzón

**Integrantes:**
- Juan David Carrillo Rojas
- Marc Suárez Molina

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

## Archivo de requerimientos
Para poder acceder al archivo markdown de los requerimientos toca ingresar a 

```
pcia5020-red-transporte/
├── corte1/
parcial del Corte 1
│   ├── requerimientos/
```
Se puede acceder a el archivo a travez de la terminal ejecutando

```bash
cd corte1/requerimientos

nano PCIA5020_Requerimientos_Pareja_JuanDavidCarrilloRojasMarcSuarezMolina_2026-09-15.md
```

## Cómo correr el Corte 1

```bash
cd corte1/datos
python3 generador_datos.py        # genera zonas.txt, estaciones.txt, tramos.txt, secuencias.txt
cd ../src
python3 PCIA5020_Proyecto_Fase1_Pareja_JuanDavidCarrilloRojasMarcSuarezMolina_2026-09-15.py
```

El script de la Fase 1 carga los datos generados, arma la jerarquía, el Trie y el árbol de
búsqueda, y corre una demo con los criterios de aceptación (listar zona, autocompletar,
buscar por código, comparar comparaciones, y los tres casos de borde).
