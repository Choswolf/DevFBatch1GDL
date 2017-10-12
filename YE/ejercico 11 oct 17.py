def max(a,b):
    if (a >= b):
        c = a
    else:
        c = b
    return c


# print max(25,35)


def max3(a,b,c):
    if (a > b and a > c) :
        res = a
    if (b > a and b > c):
        res = b
    if (c > b and c > a):
        res = c
    return res

# print max3(8,6,7)



class Comparacion(object):
    def __init__(self,listap):
        self.listap = listap

    def distlista(self):
        contador = 0
        for i in self.listap:
            contador = contador +1
        return contador


    def printposiciones(self,pos):
        return self.listap[pos]
    def compare_vocal(self,pos):
        validador = ()

        vocales = ("aeiou")
        for prueba in self.listap:
            if prueba == vocales[p]:
                    validador = True
            # print vocales[p]
            # print self.listap[pos]
            # print p
        if validador != True:
            validador = False
        return validador
    def sum(self):
        acomulado = 0
        for i in self.listap:
            acomulado = acomulado + i
        return acomulado
    def mult(self):
        acomulado = 0
        for i in self.listap:
            if acomulado == 0:
                acomulado = acomulado + i
            else:
                acomulado = acomulado * i
        return acomulado
    # #ejercicio 6 definir un histograma procedimiento() que tome una lista de numeros enteros e imprima un histogramaen
    #     la pantalla. Ejemplo: procedimiento([4,9 ,7]) deberia imprimir lo siguiente
    #     ****
    #     *********
    #     *******
    #

listas=[3,1,5,7,'abc',3,131]
list2 = 'Hola'
listan =[14,2,3,4,5,47]

# print Comparacion(list2).compare_vocal(3)
print Comparacion(listan).mult()
print Comparacion(listan).distlista()

# dasdd
# dasd
# asd