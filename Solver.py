import math

class Solver:
    def calcular(self,cadena):
        if cadena == "":
            return [0,'nan','nan']
        else:
            cadenaSplit = cadena.split(',')
            minimo = int(cadenaSplit[0]);
            for x in range (1, len(cadenaSplit)):
                if(int(cadenaSplit[x]) < minimo):
                    minimo = int(cadenaSplit[x])
            return [len(cadena.split(',')),minimo]