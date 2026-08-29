# Datos de prueba — Corte 1

Generados por `generador_datos.py` (correr `python3 generador_datos.py` desde esta carpeta
para regenerarlos). Usa una semilla fija (`SEMILLA = 20260829`) para que la red sea
reproducible entre ustedes dos.

## Archivos

- **zonas.txt** — `codigo,nombre`. 5 zonas (mínimo exigido: 3). La última (`Z5`, "ZonaVacia")
  se deja **a propósito sin estaciones**, para poder probar el caso de borde "listar una zona
  sin estaciones".
- **estaciones.txt** — `codigo,nombre,zona`. 48 estaciones (mínimo exigido: 40), repartidas en
  4 zonas con 14/12/12/10 cada una (todas por encima del mínimo de "al menos una zona con 10 o
  más").
- **tramos.txt** — `origen,destino,minutos`. 70 tramos (mínimo exigido: 60) entre códigos de
  estación existentes, con tiempos entre 1 y 20 minutos. No se usan todavía en el Corte 1 (son
  para la Fase 2, grafo y Dijkstra), pero ya quedan generados porque el documento base los pide
  como parte de los datos de prueba desde este corte.
- **secuencias.txt** — `id,evento1,evento2,...`. 24 secuencias (mínimo exigido: 20), de las
  cuales 6 están construidas para ser inválidas (mínimo exigido: 5). Tampoco se procesan
  todavía (son para la Fase 3, autómatas), pero ya están generadas.

## Por qué algunas son inválidas (para su propia referencia, no hace falta entregarlo así)

El generador rompe a propósito el patrón `entrar → (transbordar)* → salir` de cuatro formas:
secuencia que no empieza con "entrar", doble "entrar" seguido, secuencia que nunca llega a
"salir", y "salir" repetido. Cuando lleguen a la Fase 3 y definan el autómata, estas son las
secuencias que su validador debería rechazar — es una buena forma de comprobar que el autómata
quedó bien construido.

## Si quieren generar otra red

Editen las constantes al principio de `generador_datos.py` (`NUM_ZONAS`,
`ESTACIONES_POR_ZONA`, `NUM_TRAMOS`, `NUM_SECUENCIAS`, `NUM_SECUENCIAS_INVALIDAS`) — siempre
por encima de los mínimos del documento base — y vuelvan a correr el script. Recuerden
actualizar después la sección de Datos de su análisis de requerimientos con el tamaño real que
usaron, y regenerar `corte1/pruebas/tabla_comparacion.md`.
