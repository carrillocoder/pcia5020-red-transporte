"""
================================================================================
 PCIA5020 - Generador de datos de prueba
--------------------------------------------------------------------------------
 Control de cambios:
   v1.0  2026-08-29  Juan David Carrillo Rojas y Marc Suarez Molina  Version inicial.
--------------------------------------------------------------------------------
 Genera los archivos de datos de prueba de la red de transporte, respetando
 los minimos exigidos por el documento base del proyecto:
   - al menos 3 zonas
   - al menos 40 estaciones, con al menos una zona con 10 estaciones o mas
   - al menos 60 tramos
   - al menos 20 secuencias de eventos, de las cuales al menos 5 invalidas

 Los datos NO se entregan hechos: este script es la evidencia de que la
 pareja decidio los campos, los tipos y las validaciones (ver el analisis de
 requerimientos). Ajusten las constantes de abajo si cambian esas decisiones,
 pero sin bajar de los minimos.

 Uso:
   python3 generador_datos.py
================================================================================
"""

import random

# --------------------------------------------------------------------------
# Parametros de generacion (ajustables, siempre por encima de los minimos)
# --------------------------------------------------------------------------
SEMILLA = 20260829          #: semilla fija para que la red sea reproducible
NUM_ZONAS = 4                #: minimo exigido: 3
ESTACIONES_POR_ZONA = [14, 12, 12, 10]  #: una zona con >=10 (se exige al menos una)
NUM_TRAMOS = 70               #: minimo exigido: 60
NUM_SECUENCIAS = 24            #: minimo exigido: 20
NUM_SECUENCIAS_INVALIDAS = 6    #: minimo exigido: 5

ALFABETO_EVENTOS = ["entrar", "transbordar", "salir", "recargar"]

NOMBRES_ZONA = ["Norte", "Sur", "Centro", "Occidente", "Oriente", "Autopista"]


def generar_zonas(num_zonas):
    """Genera la lista de zonas como diccionarios {codigo, nombre}."""
    zonas = []
    for i in range(num_zonas):
        codigo = f"Z{i + 1}"
        nombre = NOMBRES_ZONA[i % len(NOMBRES_ZONA)]
        zonas.append({"codigo": codigo, "nombre": nombre})
    # Se agrega a proposito una zona SIN estaciones, para poder probar el
    # caso de borde "listar una zona sin estaciones" pedido en los criterios
    # de aceptacion.
    zonas.append({"codigo": f"Z{num_zonas + 1}", "nombre": "ZonaVacia"})
    return zonas


def generar_estaciones(zonas, estaciones_por_zona):
    """Genera estaciones con codigo entero unico, nombre y zona a la que pertenecen.

    La ultima zona de la lista queda deliberadamente sin estaciones (caso de
    borde de "zona vacia").
    """
    estaciones = []
    codigo_actual = 100
    tipos_nombre = [
        "Plaza", "Terminal", "Parque", "Universidad", "Hospital", "Mercado",
        "Estadio", "Biblioteca", "Museo", "Centro Comercial", "Aeropuerto",
        "Cementerio", "Iglesia", "Coliseo",
    ]
    for idx_zona, zona in enumerate(zonas[:-1]):  # la ultima zona queda vacia
        cantidad = estaciones_por_zona[idx_zona]
        for j in range(cantidad):
            nombre = f"{tipos_nombre[j % len(tipos_nombre)]} {zona['nombre']} {j + 1}"
            estaciones.append({
                "codigo": codigo_actual,
                "nombre": nombre,
                "zona": zona["codigo"],
            })
            codigo_actual += 1
    return estaciones


def generar_tramos(estaciones, num_tramos, rng):
    """Genera tramos (origen, destino, minutos) entre estaciones existentes.

    Se garantiza primero que cada estacion tenga al menos un tramo (para que
    la red sea razonable), y despues se completan tramos aleatorios extra
    hasta llegar a num_tramos.
    """
    codigos = [e["codigo"] for e in estaciones]
    tramos = []
    vistos = set()

    def agregar_tramo(origen, destino):
        if origen == destino:
            return False
        clave = (origen, destino)
        if clave in vistos:
            return False
        minutos = rng.randint(1, 20)
        tramos.append({"origen": origen, "destino": destino, "minutos": minutos})
        vistos.add(clave)
        return True

    # Conecta cada estacion con la siguiente de su lista (cadena simple)
    for i in range(len(codigos) - 1):
        agregar_tramo(codigos[i], codigos[i + 1])

    # Completa con tramos aleatorios hasta llegar al minimo pedido
    intentos = 0
    while len(tramos) < num_tramos and intentos < num_tramos * 20:
        origen, destino = rng.sample(codigos, 2)
        agregar_tramo(origen, destino)
        intentos += 1

    return tramos


def _secuencia_valida(rng):
    """Construye una secuencia de eventos que cumple el patron esperado de un
    viaje: entrar, (transbordar)*, salir, con recargas sueltas permitidas.
    """
    eventos = ["entrar"]
    for _ in range(rng.randint(0, 2)):
        eventos.append("transbordar")
    if rng.random() < 0.3:
        eventos.append("recargar")
    eventos.append("salir")
    return eventos


def _secuencia_invalida(rng):
    """Construye una secuencia que rompe a proposito el patron de un viaje
    valido, para servir de caso de prueba de secuencia invalida (Fase 3).
    """
    tipo = rng.choice(["sin_entrar", "doble_entrar", "sin_salir", "evento_repetido_mal"])
    if tipo == "sin_entrar":
        return ["transbordar", "salir"]
    if tipo == "doble_entrar":
        return ["entrar", "entrar", "salir"]
    if tipo == "sin_salir":
        return ["entrar", "transbordar"]
    return ["entrar", "salir", "salir"]


def generar_secuencias(num_secuencias, num_invalidas, rng):
    """Genera secuencias de eventos de tarjeta, marcando cuales son invalidas
    a proposito (para los datos de prueba de la Fase 3, que se validan mas
    adelante en el proyecto).
    """
    secuencias = []
    num_validas = num_secuencias - num_invalidas
    for i in range(num_validas):
        secuencias.append({"id": f"S{i + 1:02d}", "eventos": _secuencia_valida(rng)})
    for i in range(num_invalidas):
        idx = num_validas + i
        secuencias.append({"id": f"S{idx + 1:02d}", "eventos": _secuencia_invalida(rng)})
    rng.shuffle(secuencias)
    return secuencias


def escribir_zonas(zonas, ruta):
    """Escribe zonas.txt con formato codigo,nombre (una por linea)."""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("codigo,nombre\n")
        for z in zonas:
            f.write(f"{z['codigo']},{z['nombre']}\n")


def escribir_estaciones(estaciones, ruta):
    """Escribe estaciones.txt con formato codigo,nombre,zona (una por linea)."""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("codigo,nombre,zona\n")
        for e in estaciones:
            f.write(f"{e['codigo']},{e['nombre']},{e['zona']}\n")


def escribir_tramos(tramos, ruta):
    """Escribe tramos.txt con formato origen,destino,minutos (una por linea)."""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("origen,destino,minutos\n")
        for t in tramos:
            f.write(f"{t['origen']},{t['destino']},{t['minutos']}\n")


def escribir_secuencias(secuencias, ruta):
    """Escribe secuencias.txt con formato id,evento1,evento2,... (una por linea)."""
    with open(ruta, "w", encoding="utf-8") as f:
        for s in secuencias:
            f.write(f"{s['id']}," + ",".join(s["eventos"]) + "\n")


def main():
    """Genera y escribe los cuatro archivos de datos de prueba en esta carpeta."""
    rng = random.Random(SEMILLA)

    zonas = generar_zonas(NUM_ZONAS)
    estaciones = generar_estaciones(zonas, ESTACIONES_POR_ZONA)
    tramos = generar_tramos(estaciones, NUM_TRAMOS, rng)
    secuencias = generar_secuencias(NUM_SECUENCIAS, NUM_SECUENCIAS_INVALIDAS, rng)

    escribir_zonas(zonas, "zonas.txt")
    escribir_estaciones(estaciones, "estaciones.txt")
    escribir_tramos(tramos, "tramos.txt")
    escribir_secuencias(secuencias, "secuencias.txt")

    print(f"Zonas generadas: {len(zonas)} (minimo 3)")
    print(f"Estaciones generadas: {len(estaciones)} (minimo 40)")
    print(f"Tramos generados: {len(tramos)} (minimo 60)")
    print(f"Secuencias generadas: {len(secuencias)} (minimo 20, {NUM_SECUENCIAS_INVALIDAS} invalidas, minimo 5)")
    print("Archivos escritos: zonas.txt, estaciones.txt, tramos.txt, secuencias.txt")


if __name__ == "__main__":
    main()
