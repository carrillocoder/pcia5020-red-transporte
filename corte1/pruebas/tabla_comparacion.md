# Tabla de comparación — árbol de búsqueda vs. recorrido secuencial

Requisito de admisión del Corte 1. Debe traer más de un número y **la resta escrita**
(documento del docente: "La tabla de comparación trae un solo número, sin la resta escrita"
es motivo de devolución sin calificar).

Estos son los números que imprime `corte1/src/PCIA5020_Proyecto_Fase1_Pareja_NN_AAAA-MM-DD.py`
al correrlo con la red de prueba actual (48 estaciones) — el código ya no calcula una tabla de
varios códigos de muestra: solo ejecuta, literalmente, lo que pide la sección 6 del análisis de
requerimientos (RF-03 y RF-04).

## Resultado de referencia (con la red de prueba generada por defecto, 48 estaciones)

| Código buscado | Comparaciones (árbol) | Comparaciones (secuencial) | Diferencia (secuencial − árbol) |
|---:|---:|---:|---:|
| 124 | 1 | 25 | 24 |

**Lectura:** en un árbol balanceado de 48 estaciones, ninguna búsqueda cuesta más de 6
comparaciones (⌈log₂48⌉ = 6) — el código lo comprueba sobre las 48 estaciones, no solo sobre el
código 124. La búsqueda secuencial, en cambio, crece de forma lineal: como el código 124 es la
estación número 25 de la lista, cuesta exactamente 25 comparaciones encontrarla.

## Caso de borde: código que no existe

| Código buscado | Comparaciones (árbol) |
|---:|---:|
| 999999 | 5 |

`buscar_arbol(999999)` no lanza excepción: devuelve `None` de forma controlada (criterio de
aceptación de RF-03). El código ya no compara este caso contra la búsqueda secuencial, porque
esa comparación no es un criterio de aceptación que pida el análisis de requerimientos.

---

**Pendiente para la pareja:** si cambian el tamaño de la red de prueba (más o menos
estaciones), vuelvan a correr el script y reemplacen esta tabla con sus números reales.
