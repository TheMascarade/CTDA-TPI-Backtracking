import unittest
import jardin_backtracking as src


class TestExistePatron(unittest.TestCase):
    def test_patron_igual_jardin(self):
        self.assertTrue(src.existe_patron(j1, patrones_prohibidos[0]))

    def test_patron_en_submatriz(self):
        self.assertTrue(src.existe_patron(j1, patrones_prohibidos[1]))

    def test_patron_no_existe(self):
        self.assertFalse(src.existe_patron(j3, patrones_prohibidos[0]))

    def test_patron_no_existe_submatriz(self):
        self.assertFalse(src.existe_patron(j3, patrones_prohibidos[1]))

    def test_existen_todos_patrones(self):
        self.assertFalse(src.es_jardin_valido(j1, patrones_prohibidos))

    def test_existe_algun_patron(self):
        self.assertFalse(src.es_jardin_valido(j2, patrones_prohibidos))

    def test_existe_ningun_patron(self):
        self.assertTrue(src.es_jardin_valido(j3, patrones_prohibidos))


j1 = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
]
j2 = [
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 1],
]
j3 = [
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
]

patrones_prohibidos = [
    [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ],
    [
        [1, 0],
        [0, 0],
    ],
]

unittest.main()
