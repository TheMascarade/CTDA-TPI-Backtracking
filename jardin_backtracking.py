B = [[9, 0, 12, 5], [0, 20, 0, 0], [4, 0, 1, 9]]
patrones_prohibidos = [[[1, 0, 1], [0, 0, 0], [1, 0, 1]]]


class Nodo:
    def __init__(self, jardin_estado, sum_belleza: int):
        self.jardin_estado = jardin_estado
        self.sum_belleza = sum_belleza
        self.hijos: list["Nodo"] = []

    def nuevo_hijo(self, nodo):
        self.hijos.append(nodo)


def belleza(jardin, patrones_prohib) -> int:
    filas = len(jardin)
    cols = len(jardin[0])
    raiz = Nodo(
        jardin_estado=[[0] for _ in range(cols) for _ in range(filas)],
        sum_belleza=0,
    )
    celdas_prohibidas: set[tuple[int, int]] = set()
    generar_soluciones(raiz, celdas_prohibidas, jardin)


def generar_soluciones(padre: "Nodo", cel_prohibidas, bellezas, fila=0, col=0):
    if col >= len(bellezas[0]) - 1:
        if fila >= len(bellezas) - 1:
            return
        col = 0
        fila += 1
    for fila in range(fila, len(bellezas)):
        for col in range(col, len(bellezas[0])):
            if es_celda_prohibida(fila, col, cel_prohibidas):
                continue
            nuevas_prohibidas = cel_prohibidas.update(
                [
                    (fila + 1, col + 1),
                    (fila, col + 1),
                    (fila + 1, col),
                    (fila - 1, col - 1),
                    (fila, col - 1),
                    (fila - 1, col),
                ]
            )
            nuevo_estado_jardin = padre.jardin_estado
            nuevo_estado_jardin[fila, col] = bellezas[fila, col]
            nuevo_nodo = Nodo(
                jardin_estado=nuevo_estado_jardin,
                sum_belleza=padre.sum_belleza + bellezas[fila, col],
            )
            padre.nuevo_hijo(nuevo_nodo)
            generar_soluciones(nuevo_nodo, nuevas_prohibidas, bellezas, fila, col + 1)
        col = 0


def es_celda_prohibida(fila, col, cel_prohibidas) -> bool:
    return (fila, col) in cel_prohibidas
