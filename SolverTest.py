from unittest import TestCase

from Solver import Solver

class SolverTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Solver().calcular(""),[0],"Cadena vacía")

    def test_calcular_1_elementos(self):
        self.assertEqual(Solver().calcular("4"), [1], "1 elemento")

    def test_calcular_2_elementos(self):
        self.assertEqual(Solver().calcular("4,2"), [2], "2 elementos")

    def test_calcular_n_elementos(self):
        self.fail()