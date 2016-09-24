import math

class Solver:

    def calcular(self,cadena):
        if cadena == "":
            return [0,'nan','nan','nan']
        elif "," not in cadena:
                return [1,int(cadena),int(cadena),int(cadena)]
        cadenaSplit = cadena.split(',')
        minimo = int(cadenaSplit[0])
        maximo = int(cadenaSplit[0])
        suma = 0
        for x in range (0, len(cadenaSplit)):
            suma = suma + int(cadenaSplit[x])
            if(int(cadenaSplit[x]) < minimo):
                minimo = int(cadenaSplit[x])
            if(int(cadenaSplit[x])> maximo):
                maximo = int(cadenaSplit[x])
        suma = float(suma)
        avg = suma/len(cadenaSplit)
        return [len(cadena.split(',')),minimo, maximo, avg]