import math

class Solver:
    def calcular(self,cadena):
        if cadena == "":
            return [0,0]
        else:
            if ',' not in cadena:
                return [1,int(cadena)]
            return [len(cadena.split(','))]