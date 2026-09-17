# Tabla de comparación — árbol de búsqueda vs. recorrido secuencial

Requisito de admisión del Corte 1. Debe traer más de un número y **la resta escrita**
(documento del docente: "La tabla de comparación trae un solo número, sin la resta escrita"
es motivo de devolución sin calificar).

Se genera corriendo `corte1/src/PCIA5020_Proyecto_Fase1_Pareja_NN_AAAA-MM-DD.py`: al final
imprime esta misma tabla con los datos de la red de prueba actual. Cópienla aquí (o
regenérenla si cambian los datos).

## Resultado de referencia (con la red de prueba generada por defecto, 48 estaciones)

| Código buscado | Comparaciones (árbol) | Comparaciones (secuencial) | Diferencia (secuencial − árbol) |
|---:|---:|---:|---:|
| 100 | 6 | 1 | -5 |
| 108 | 5 | 9 | 4 |
| 116 | 6 | 17 | 11 |
| 124 | 1 | 25 | 24 |
| 132 | 5 | 33 | 28 |
| 140 | 6 | 41 | 35 |

**Lectura:** en un árbol balanceado de 48 estaciones, ninguna búsqueda cuesta más de 6
comparaciones (⌈log₂48⌉ = 6), sin importar dónde esté la estación. La búsqueda secuencial, en
cambio, crece de forma lineal: si el código está al final de la lista, cuesta tantas
comparaciones como estaciones haya. La única fila donde el árbol "pierde" es el código 100
(comparado contra una búsqueda secuencial que lo encuentra de primeras, en el mejor caso
posible para ese método) — eso es normal y vale la pena explicarlo en la sustentación.

## Caso de borde: código que no existe

| Código buscado | Comparaciones (árbol) | Comparaciones (secuencial) |
|---:|---:|---:|
| 999999 | 5 | 48 |

Ninguna de las dos búsquedas lanza excepción: ambas devuelven `None` de forma controlada.

---

**Pendiente para la pareja:** si cambian el tamaño de la red de prueba (más o menos
estaciones), vuelvan a correr el script y reemplacen esta tabla con sus números reales.
