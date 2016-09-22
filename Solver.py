import math

class Solver:
    def calcular(self,cadena):
        if cadena == "":
            return [0,'nan']
        else:
            if ',' not in cadena:
                return [1,int(cadena)]
            elif len(cadena.split(','))==2:
                cadSplit = cadena.split(',')
                num1 = int(cadSplit[0])
                num2 = int(cadSplit[1])
                if(num1 > num2):
                    return [2, num2]
                else:
                    return [2, num1]
        return [len(cadena.split(','))]