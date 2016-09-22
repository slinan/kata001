import math

class Solver:
    def calcular(self,cadena):
        if cadena == "":
            return [0]
        else:
            return [len(cadena.split(','))]