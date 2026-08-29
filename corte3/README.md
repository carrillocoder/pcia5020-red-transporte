# Corte 3 — Fase 3: autómata finito determinista, autómata no determinista, máquina de estados

Pendiente por trabajar (semanas 12-16). Esta carpeta se completa durante el Corte 3.

## Estructuras obligatorias

Autómata finito determinista (AFD), autómata no determinista (AFN), máquina de estados.

## Qué debe hacer el software (documento base)

- Modelar el viaje de una tarjeta como autómata: estados, alfabeto de eventos (entrar,
  transbordar, salir, recargar), transiciones, estado inicial y estados de aceptación.
- Validar si una secuencia de eventos es un viaje correcto, e indicar en qué evento falló si no
  lo es.
- Modelar una variante con un autómata no determinista y convertirla a determinista.
- Reportar cuántas secuencias de un archivo de prueba fueron rechazadas y por qué.

## Datos ya generados

`corte1/datos/secuencias.txt` ya trae secuencias de prueba (algunas válidas, algunas
inválidas a propósito) para validar el autómata que construyan aquí — no hace falta generar un
archivo nuevo, aunque pueden ampliarlo si quieren más casos.

## Nota sobre la sustentación de este corte

Es individual en la forma de preguntar: a cada integrante se le pide explicar decisiones de
diseño por separado y modificar algo en vivo (por ejemplo, añadir una transición). La nota de
esa parte es individual aunque el código sea de los dos.

## Estructura sugerida (a crear cuando empiecen)

```
corte3/
├── requerimientos/   ← análisis final con RF-09..RF-11 completos
├── src/               ← PCIA5020_Proyecto_Fase3_Pareja_NN_AAAA-MM-DD.py
└── pruebas/           ← reporte de secuencias rechazadas y diagrama de estados
```
