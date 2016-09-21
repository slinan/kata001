from unittest import TestCase

from Solver import Solver

class SolverTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Solver().calcular(""),0,"Cadena vacía")
