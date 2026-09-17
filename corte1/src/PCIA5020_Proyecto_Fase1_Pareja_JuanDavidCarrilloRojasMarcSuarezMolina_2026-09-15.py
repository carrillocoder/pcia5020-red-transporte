"""
================================================================================
 PCIA5020 - Estructuras de Datos No Lineales
 Proyecto: Red de transporte de la ciudad - Fase 1 (Corte 1)
--------------------------------------------------------------------------------
 Pareja NN: Juan David Carrillo Rojas y Marc Suarez Molina
--------------------------------------------------------------------------------
 Control de cambios:
   v1.0  2026-08-29  Juan David Carrillo Rojas y Marc Suarez Molina
         Version inicial: arbol N-ario (ciudad -> zonas -> estaciones), Trie
         de autocompletado, arbol de busqueda binaria por codigo y busqueda
         secuencial de comparacion, con carga de datos y casos de borde.
--------------------------------------------------------------------------------
 Estructuras obligatorias de esta fase: Arbol N-ario, Trie, Arbol de busqueda
 binaria. El monticulo NO va en este corte (se construye en la Fase 2).

 Nada de esto usa bibliotecas que resuelvan la estructura (sin networkx ni
 similares): todo esta implementado a mano.

 IMPORTANTE PARA LA PAREJA: este archivo es un PUNTO DE PARTIDA que ya cumple
 los criterios de aceptacion del Corte 1. Antes de sustentarlo:
   1) Renombren el archivo con su numero de pareja y la fecha real.
   2) Lean y entiendan cada funcion: en la sustentacion se pregunta por
      CUALQUIER parte, a cualquiera de los dos.
   3) Ajusten los campos/validaciones si su analisis de requerimientos
      decidio algo distinto a lo que hay aqui (Estacion, Zona, etc.), para
      que el codigo y el documento queden coherentes entre si.
================================================================================
"""

import os


# ==============================================================================
# 1. CARGA DE DATOS
# ==============================================================================

class Estacion:
    """Representa una estacion: codigo entero unico, nombre y zona a la que
    pertenece. El codigo es entero (y no texto) porque es la clave con la que
    se ordena el arbol de busqueda binaria: si fuera texto, "100" quedaria
    ordenado antes que "20" por comparacion de caracteres.
    """

    def __init__(self, codigo, nombre, zona):
        self.codigo = codigo
        self.nombre = nombre
        self.zona = zona

    def __repr__(self):
        return f"Estacion({self.codigo}, '{self.nombre}', zona='{self.zona}')"


def cargar_zonas(ruta):
    """Lee zonas.txt (codigo,nombre) y devuelve una lista de dicts {codigo, nombre}.

    Casos invalidos (linea mal formada) se ignoran con un aviso en consola en
    vez de tumbar el programa.
    """
    zonas = []
    if not os.path.exists(ruta):
        print(f"[AVISO] No se encontro el archivo de zonas: {ruta}")
        return zonas
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.readlines()[1:]  # se salta el encabezado
    for num_linea, linea in enumerate(lineas, start=2):
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(",")
        if len(partes) != 2:
            print(f"[AVISO] Linea {num_linea} de zonas.txt invalida, se ignora: {linea!r}")
            continue
        codigo, nombre = partes
        zonas.append({"codigo": codigo.strip(), "nombre": nombre.strip()})
    return zonas


def cargar_estaciones(ruta):
    """Lee estaciones.txt (codigo,nombre,zona) y devuelve una lista de objetos
    Estacion. Valida que el codigo sea entero y que no este repetido; las
    lineas invalidas se reportan y se saltan, no tumban el programa.
    """
    estaciones = []
    codigos_vistos = set()
    if not os.path.exists(ruta):
        print(f"[AVISO] No se encontro el archivo de estaciones: {ruta}")
        return estaciones
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.readlines()[1:]
    for num_linea, linea in enumerate(lineas, start=2):
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(",")
        if len(partes) != 3:
            print(f"[AVISO] Linea {num_linea} de estaciones.txt invalida, se ignora: {linea!r}")
            continue
        codigo_txt, nombre, zona = partes
        try:
            codigo = int(codigo_txt.strip())
        except ValueError:
            print(f"[AVISO] Codigo no entero en linea {num_linea}, se ignora: {linea!r}")
            continue
        if codigo in codigos_vistos:
            print(f"[AVISO] Codigo repetido {codigo} en linea {num_linea}, se ignora.")
            continue
        codigos_vistos.add(codigo)
        estaciones.append(Estacion(codigo, nombre.strip(), zona.strip()))
    return estaciones


# ==============================================================================
# 2. ARBOL N-ARIO: ciudad -> zonas -> estaciones
# ==============================================================================

class NodoArbolN:
    """Nodo generico de un arbol N-ario. 'tipo' es 'ciudad', 'zona' o
    'estacion'; 'datos' guarda informacion propia del nodo (por ejemplo, el
    objeto Estacion completo en un nodo hoja).
    """

    def __init__(self, nombre, tipo, datos=None):
        self.nombre = nombre
        self.tipo = tipo
        self.datos = datos
        self.hijos = []

    def agregar_hijo(self, hijo):
        """Agrega un nodo hijo (otra zona, u otra estacion) a este nodo."""
        self.hijos.append(hijo)


def construir_jerarquia(nombre_ciudad, zonas, estaciones):
    """Construye el arbol N-ario ciudad -> zonas -> estaciones a partir de las
    listas cargadas de zonas y estaciones. Devuelve el nodo raiz (la ciudad).
    """
    raiz = NodoArbolN(nombre_ciudad, "ciudad")
    nodos_zona = {}
    for zona in zonas:
        nodo_zona = NodoArbolN(zona["nombre"], "zona", datos={"codigo": zona["codigo"]})
        nodos_zona[zona["codigo"]] = nodo_zona
        raiz.agregar_hijo(nodo_zona)

    for estacion in estaciones:
        nodo_zona = nodos_zona.get(estacion.zona)
        if nodo_zona is None:
            print(f"[AVISO] La estacion {estacion.codigo} referencia una zona "
                  f"inexistente ({estacion.zona}); se ignora.")
            continue
        nodo_estacion = NodoArbolN(estacion.nombre, "estacion", datos=estacion)
        nodo_zona.agregar_hijo(nodo_estacion)

    return raiz


def listar_zona(raiz, codigo_zona):
    """Devuelve la lista de objetos Estacion que pertenecen a la zona con ese
    codigo. Si la zona no existe o no tiene estaciones, devuelve una lista
    vacia (no lanza excepcion) -- este es uno de los casos de borde pedidos.
    """
    for nodo_zona in raiz.hijos:
        if nodo_zona.datos and nodo_zona.datos.get("codigo") == codigo_zona:
            return [hijo.datos for hijo in nodo_zona.hijos]
    return []  # zona inexistente: tambien se resuelve como lista vacia


def recorrer_jerarquia(nodo, nivel=0):
    """Recorre el arbol en profundidad e imprime la jerarquia completa
    (ciudad -> zonas -> estaciones), indentando segun el nivel.
    """
    print("  " * nivel + f"- [{nodo.tipo}] {nodo.nombre}")
    for hijo in nodo.hijos:
        recorrer_jerarquia(hijo, nivel + 1)


# ==============================================================================
# 3. TRIE: autocompletado de nombres de estacion
# ==============================================================================

class NodoTrie:
    """Nodo de un Trie construido a mano: cada nodo guarda sus hijos por
    caracter en un diccionario, y la lista de nombres completos de estacion
    que terminan exactamente en este nodo (puede haber mas de uno con el
    mismo texto, aunque no es lo usual).
    """

    def __init__(self):
        self.hijos = {}          # caracter -> NodoTrie
        self.fin_de_palabra = False
        self.nombres_aqui = []   # nombres de estacion que terminan aqui


class Trie:
    """Trie de nombres de estacion, construido caracter por caracter (NO es
    un diccionario de cadenas completas: cada nodo representa un solo
    caracter, y los prefijos comunes comparten nodos).
    """

    def __init__(self):
        self.raiz = NodoTrie()

    def insertar(self, nombre):
        """Inserta un nombre de estacion en el Trie, caracter por caracter,
        usando la version en minusculas para que el autocompletado no
        distinga mayusculas de minusculas.
        """
        nodo = self.raiz
        clave = nombre.lower()
        for caracter in clave:
            if caracter not in nodo.hijos:
                nodo.hijos[caracter] = NodoTrie()
            nodo = nodo.hijos[caracter]
        nodo.fin_de_palabra = True
        nodo.nombres_aqui.append(nombre)

    def _recolectar(self, nodo, resultados):
        """Recolecta, recorriendo el subarbol de 'nodo', todos los nombres
        completos guardados debajo (incluyendo el propio nodo si aplica).
        """
        if nodo.fin_de_palabra:
            resultados.extend(nodo.nombres_aqui)
        for hijo in nodo.hijos.values():
            self._recolectar(hijo, resultados)

    def autocompletar(self, prefijo):
        """Devuelve la lista de nombres de estacion que empiezan por
        'prefijo'. Si el prefijo es vacio o no hay coincidencias, devuelve
        una lista vacia (no un error) -- caso de borde pedido.
        """
        if prefijo == "":
            return []
        nodo = self.raiz
        clave = prefijo.lower()
        for caracter in clave:
            if caracter not in nodo.hijos:
                return []  # no hay ninguna estacion con ese prefijo
            nodo = nodo.hijos[caracter]
        resultados = []
        self._recolectar(nodo, resultados)
        return resultados


# ==============================================================================
# 4. ARBOL DE BUSQUEDA BINARIA: buscar estacion por codigo, contando comparaciones
# ==============================================================================

class NodoBST:
    """Nodo del arbol de busqueda binaria, ordenado por el codigo (entero) de
    la estacion.
    """

    def __init__(self, estacion):
        self.estacion = estacion
        self.izquierda = None
        self.derecha = None


class ArbolBusquedaBinaria:
    """Arbol de busqueda binaria (BST) de estaciones, ordenado por codigo.
    Implementado a mano (sin bibliotecas de arboles balanceados): para los
    tamanos de red de este proyecto no hace falta balancear.
    """

    def __init__(self):
        self.raiz = None

    def construir_balanceado(self, estaciones):
        """Construye el arbol desde cero a partir de una lista de estaciones,
        quedando BALANCEADO (no solo binario).

        OJO, esta es la parte que de verdad importa para el criterio de
        aceptacion: si se insertaran las estaciones una por una, ya
        ordenadas por codigo (que es como las genera el generador de
        datos), el arbol degeneraria en una fila -- cada nodo con un solo
        hijo -- y la busqueda quedaria igual de lenta que recorrer la lista
        completa. Por eso aqui se ordena primero por codigo y se inserta
        siempre el elemento DEL MEDIO primero: asi cada mitad queda del
        mismo tamano en cada nivel y el arbol queda con altura logaritmica,
        que es lo que hace que la comparacion contra la busqueda secuencial
        tenga sentido.
        """
        ordenadas = sorted(estaciones, key=lambda e: e.codigo)
        self.raiz = self._construir_balanceado_rec(ordenadas)

    def _construir_balanceado_rec(self, lista_ordenada):
        if not lista_ordenada:
            return None
        medio = len(lista_ordenada) // 2
        nodo = NodoBST(lista_ordenada[medio])
        nodo.izquierda = self._construir_balanceado_rec(lista_ordenada[:medio])
        nodo.derecha = self._construir_balanceado_rec(lista_ordenada[medio + 1:])
        return nodo

    def buscar(self, codigo):
        """Busca una estacion por su codigo. Devuelve una tupla
        (estacion_o_None, numero_de_comparaciones). No lanza excepcion si el
        codigo no existe -- caso de borde pedido -- simplemente devuelve None.
        """
        nodo = self.raiz
        comparaciones = 0
        while nodo is not None:
            comparaciones += 1
            if codigo == nodo.estacion.codigo:
                return nodo.estacion, comparaciones
            elif codigo < nodo.estacion.codigo:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
        return None, comparaciones


def busqueda_secuencial(estaciones, codigo):
    """Busca una estacion por codigo recorriendo la lista completa, de
    principio a fin, contando comparaciones. Sirve de referencia para
    comparar contra el arbol de busqueda binaria (RF-04). Tampoco lanza
    excepcion si el codigo no existe.
    """
    comparaciones = 0
    for estacion in estaciones:
        comparaciones += 1
        if estacion.codigo == codigo:
            return estacion, comparaciones
    return None, comparaciones


# ==============================================================================
# 5. DEMO: criterios de aceptacion del Corte 1
# ==============================================================================

def imprimir_encabezado(texto):
    print("\n" + "=" * 78)
    print(texto)
    print("=" * 78)


def main():
    """Punto de entrada: carga los datos, construye las tres estructuras
    obligatorias de la Fase 1 y verifica, uno por uno, los criterios de
    aceptacion de RF-01 a RF-04 tal como quedaron definidos en la seccion 6
    del analisis de requerimientos.
    """
    carpeta_datos = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "..", "datos")
    ruta_zonas = os.path.join(carpeta_datos, "zonas.txt")
    ruta_estaciones = os.path.join(carpeta_datos, "estaciones.txt")

    zonas = cargar_zonas(ruta_zonas)
    estaciones = cargar_estaciones(ruta_estaciones)

    if not zonas or not estaciones:
        print("[ERROR] No hay datos suficientes para correr la demo. "
              "Corran primero 'python3 datos/generador_datos.py'.")
        return

    # --- RF-01: jerarquia ciudad -> zonas -> estaciones ----------------------
    imprimir_encabezado("RF-01: jerarquia ciudad -> zonas -> estaciones")
    raiz = construir_jerarquia("Ciudad", zonas, estaciones)
    recorrer_jerarquia(raiz)

    resultado = listar_zona(raiz, "Z1")
    print(f"\nlistar_zona('Z1'): {len(resultado)} estaciones (se esperan 14)")
    for est in resultado:
        print(f"   {est}")

    resultado_vacio = listar_zona(raiz, "Z5")
    print(f"listar_zona('Z5'): {len(resultado_vacio)} estaciones "
          f"(zona vacia, se esperan 0, sin excepcion)")

    # --- RF-02: autocompletado con Trie ---------------------------------
    imprimir_encabezado("RF-02: autocompletado con Trie")
    trie = Trie()
    for est in estaciones:
        trie.insertar(est.nombre)

    resultado_pla = trie.autocompletar("Pla")
    print(f"autocompletar('Pla'): {len(resultado_pla)} nombres (se esperan 4)")
    for nombre in resultado_pla:
        print(f"   {nombre}")

    resultado_vacio = trie.autocompletar("")
    print(f"autocompletar(''): {resultado_vacio} (se espera lista vacia, sin excepcion)")

    # --- RF-03 y RF-04: arbol de busqueda binaria vs. busqueda secuencial ----
    imprimir_encabezado("RF-03 y RF-04: arbol de busqueda binaria vs. busqueda secuencial")
    arbol_busqueda = ArbolBusquedaBinaria()
    arbol_busqueda.construir_balanceado(estaciones)

    est_arbol, comp_arbol = arbol_busqueda.buscar(124)
    est_lista, comp_lista = busqueda_secuencial(estaciones, 124)
    print(f"buscar_arbol(124):        {est_arbol}  -> {comp_arbol} comparaciones (se espera 1)")
    print(f"busqueda_secuencial(124): {est_lista}  -> {comp_lista} comparaciones (se esperan 25)")
    print(f"Diferencia: {comp_lista - comp_arbol} comparaciones (se esperan 24)")

    maximo = max(arbol_busqueda.buscar(est.codigo)[1] for est in estaciones)
    print(f"\nMaximo de comparaciones del arbol sobre las {len(estaciones)} estaciones: "
          f"{maximo} (el limite prometido es techo(log2 {len(estaciones)}) = 6)")

    est_no, comp_no_arbol = arbol_busqueda.buscar(999999)
    print(f"\nbuscar_arbol(999999) (codigo inexistente): {est_no} "
          f"-> {comp_no_arbol} comparaciones, sin excepcion")


if __name__ == "__main__":
    main()
