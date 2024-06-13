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


def existe_patron(jardin, patron):
    # Si la matriz del patron es de mayor tamaño que la del jardin
    # el patron no puede existir
    if len(patron) > len(jardin) or len(patron[0]) > len(jardin[0]):
        return False

    # Caso en que la matriz del patron y el jardin sean de igual tamaño
    # comprobamos si los 1 coinciden en ambas matrices
    if len(patron) == len(jardin) and len(patron[0]) == len(jardin[0]):
        for fila in range(len(jardin)):
            for col in range(len(jardin[0])):
                if patron[fila][col] == 1 and jardin[fila][col] != 1:
                    return False
        return True

    # Caso en que la matriz de jardin sea de mayores dimensiones que el patron
    dy = len(jardin) - len(patron)
    dx = len(jardin[0]) - len(patron[0])


def es_jardin_valido(jardin, patrones_prohib):
    for patron in patrones_prohib:
        if existe_patron(jardin, patron):
            return False
    return True


class Nodo:
    def __init__(self, cords, jardin_estado, sum_belleza: int, belleza, celdas_prohib):
        self.jardin_estado: list[list[int]] = jardin_estado
        self.cords = cords
        self.sum_belleza = sum_belleza
        self.belleza = belleza
        self.celdas_prohibidas: set[tuple[int, int]] = celdas_prohib
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


def belleza(jardin, patrones_prohib):
    filas = len(jardin)
    cols = len(jardin[0])
    raiz = Nodo(
        cords=None,
        jardin_estado=[[0 for _ in range(cols)] for _ in range(filas)],
        sum_belleza=0,
        belleza=0,
        celdas_prohib=set(),
    )
    generar_soluciones(
        padre=raiz,
        bellezas=jardin,
    )
    print(raiz)


def generar_soluciones(padre: "Nodo", bellezas, fila=0, col=0):
    for fila in range(fila, len(bellezas)):
        for col in range(col, len(bellezas[0]) - 1):
            # print("padre", padre.cords)
            # print("fila", fila)
            # print("columna", col)
            # print("prohibidas", padre.celdas_prohibidas)
            # print("----------------")
            if (fila, col) in padre.celdas_prohibidas:
                continue
            nuevo_nodo = Nodo(
                cords=(fila, col),
                jardin_estado=padre.jardin_estado,
                sum_belleza=padre.sum_belleza + bellezas[fila][col],
                belleza=bellezas[fila][col],
                celdas_prohib=padre.celdas_prohibidas.copy(),
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
    return


belleza(B, None)
