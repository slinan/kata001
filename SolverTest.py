from unittest import TestCase

from Solver import Solver

class SolverTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Solver().calcular(""),[0,'nan','nan'],"Cadena vacía")

    def test_calcular_1_elementos(self):
        self.assertEqual(Solver().calcular("5"), [1,5,5], "1 elemento")

    def test_calcular_2_elementos(self):
       self.assertEqual(Solver().calcular("4,2"), [2,2], "2 elementos")

    def test_calcular_n_elementos(self):
        self.assertEqual(Solver().calcular("4,2,4,5,4,5,4,5,4"), [9,2], "9 elementos")
        self.assertEqual(Solver().calcular("4,2,4,55,44,55,4,5,964"), [9,2], "9 elementos")
        self.assertEqual(Solver().calcular("4,2,4,55,44,55,4,5,964,1,1,1,1,1,1,1,1"), [17,1], "17 elementos")