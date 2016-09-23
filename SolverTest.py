from unittest import TestCase

from Solver import Solver

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

class SolverTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Solver().calcular(""),[0,'nan','nan','nan'],"Cadena vacía")

    def test_calcular_1_elementos(self):
        self.assertEqual(Solver().calcular("5"), [1,5,5,mean([5])], "1 elemento")

    def test_calcular_2_elementos(self):
       self.assertEqual(Solver().calcular("4,2"), [2,2,4,mean([4,2])], "2 elementos")

    def test_calcular_n_elementos(self):
        self.assertEqual(Solver().calcular("4,2,4,5,4,5,4,5,4"), [9,2,5,mean([4,2,4,5,4,5,4,5,4])], "9 elementos")
        self.assertEqual(Solver().calcular("4,2,4,55,44,55,4,5,964"), [9,2,964, mean([4,2,4,55,44,55,4,5,964])], "9 elementos")
        self.assertEqual(Solver().calcular("4,2,4,55,44,55,4,5,964,1,1,1,1,1,1,1,1"), [17,1,964, mean([4,2,4,55,44,55,4,5,964,1,1,1,1,1,1,1,1])], "17 elementos")