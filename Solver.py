import math

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

class Solver:

    def calcular(self,cadena):
        if cadena == "":
            return [0,'nan','nan','nan']
        else:
            if "," not in cadena:
                return [1,int(cadena),int(cadena),mean([int(cadena)])]
            elif len(cadena.split(","))==2:
                cadenaSplit = cadena.split(",")
                if int(cadenaSplit[0])>int(cadenaSplit[1]):
                    return [2,int(cadenaSplit[1]),int(cadenaSplit[0]),mean([4,2])]
                else:
                    return [2,int(cadenaSplit[0]),int(cadenaSplit[1]),mean([4,2])]
            cadenaSplit = cadena.split(',')
            minimo = int(cadenaSplit[0]);
            maximo = int(cadenaSplit[0]);
            for x in range (1, len(cadenaSplit)):
                if(int(cadenaSplit[x]) < minimo):
                    minimo = int(cadenaSplit[x])
                if(int(cadenaSplit[x])> maximo):
                    maximo = int(cadenaSplit[x])
            return [len(cadena.split(',')),minimo, maximo]