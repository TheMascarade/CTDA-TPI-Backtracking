import copy

B = [
    [9, 0, 12, 5],
    [0, 20, 0, 0],
    [4, 0, 1, 9],
]
# B = [
#     [8, 1],
#     [1, 5],
# ]
patrones_prohibidos = [
    [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ],
]


class Nodo:
    def __init__(
        self,
        cords=(),
        jardin_estado=[[]],
        sum_belleza: int = 0,
        belleza=0,
        celdas_prohib=set(),
    ):
        self.jardin_estado: list[list[int]] = copy.deepcopy(jardin_estado)
        self.cords = cords
        self.sum_belleza = sum_belleza
        self.belleza = belleza
        self.celdas_prohibidas: set[tuple[int, int]] = celdas_prohib.copy()
        self.hijos: list["Nodo"] = []

    def __str__(self, nivel=0) -> str:
        nodo_str = (
            repr(self.cords)
            + "Belleza de celda: "
            + repr(self.belleza)
            + " Sumatoria de bellezas: "
            + repr(self.sum_belleza)
        )
        rep = "\t" * nivel + nodo_str + "\n"
        for hijo in self.hijos:
            rep += hijo.__str__(nivel + 1)
        return rep

    def nuevo_hijo(self, nodo):
        self.hijos.append(nodo)


def existe_patron(jardin, patron) -> bool:
    # Si la matriz del patron es de mayor tamaño que la del jardin
    # el patron no puede existir
    if len(patron) > len(jardin) or len(patron[0]) > len(jardin[0]):
        return False

    # Caso en que la matriz del patron y el jardin sean de igual tamaño
    # comprobamos si los 1 coinciden en ambas matrices

    # Caso en que la matriz de jardin sea de mayores dimensiones que el patron
    def patron_en_submatriz(subm, patron):
        for fila in range(len(subm)):
            for col in range(len(subm[0])):
                if patron[fila][col] == 1 and subm[fila][col] != 1:
                    return False
        return True

    if len(patron) == len(jardin) and len(patron[0]) == len(jardin[0]):
        return patron_en_submatriz(jardin, patron)

    filas_patron = len(patron)
    cols_patron = len(patron[0])
    filas_jardin = len(jardin)
    cols_jardin = len(jardin[0])
    for i in range(filas_jardin - filas_patron + 1):
        for j in range(cols_jardin - cols_patron + 1):
            submatriz = [
                fila[j : j + cols_patron] for fila in jardin[i : i + filas_patron]
            ]
            if patron_en_submatriz(submatriz, patron):
                return True
    return False


def es_jardin_valido(jardin, patrones_prohib):
    for patron in patrones_prohib:
        if existe_patron(jardin, patron):
            return False
    return True


def belleza_maxima(jardin, patrones_prohib):
    nodo_max: "Nodo"
    belleza_max = 0

    def eval_hojas(nodo: "Nodo"):
        nonlocal belleza_max
        nonlocal nodo_max
        if len(nodo.hijos) == 0:
            valido = es_jardin_valido(nodo.jardin_estado, patrones_prohib)
            if nodo.sum_belleza >= belleza_max and valido:
                imp_matriz(nodo.jardin_estado)
                print("-------------")
                belleza_max = nodo.sum_belleza
                nodo_max = nodo

        else:
            for hijo in nodo.hijos:
                eval_hojas(hijo)

    filas = len(jardin)
    cols = len(jardin[0])
    raiz = Nodo(
        jardin_estado=[[0 for _ in range(cols)] for _ in range(filas)],
    )
    generar_soluciones(
        padre=raiz,
        bellezas=jardin,
    )
    print("Arbol combinatorio")
    print("------------------")
    print(raiz)
    print("------------------")
    print("Jardines optimos:")
    print("******************")
    eval_hojas(raiz)
    print("Belleza maxima:", belleza_max)


def generar_soluciones(padre: "Nodo", bellezas, fila=0, col=0):
    for fila in range(fila, len(bellezas)):
        for col in range(col, len(bellezas[0])):
            if (fila, col) in padre.celdas_prohibidas:
                continue
            nuevo_nodo = Nodo(
                cords=(fila, col),
                jardin_estado=padre.jardin_estado,
                sum_belleza=padre.sum_belleza + bellezas[fila][col],
                belleza=bellezas[fila][col],
                celdas_prohib=padre.celdas_prohibidas,
            )
            nuevo_nodo.celdas_prohibidas.update(
                [
                    (fila, col - 1),
                    (fila, col + 1),
                    (fila + 1, col),
                    (fila - 1, col),
                    (fila - 1, col - 1),
                    (fila - 1, col + 1),
                    (fila + 1, col - 1),
                    (fila + 1, col + 1),
                ]
            )

            nuevo_nodo.jardin_estado[fila][col] = 1
            padre.nuevo_hijo(nuevo_nodo)
            generar_soluciones(
                nuevo_nodo,
                bellezas,
                fila,
                col + 1,
            )
        col = 0


def imp_matriz(matriz: list[list]):
    for fila in matriz:
        print(fila)


belleza_maxima(B, patrones_prohibidos)
