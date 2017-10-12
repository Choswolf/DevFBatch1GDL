#Ejercicio 1
def max(a,b):
    if (a > b):
        c = a
    elif(a == b):
        c = "Son iguales"
    else:
        c = b

    return c




#Ejercicio 2
def max3(a,b,c):
    if (a > b and a > c) :
        res = a
    elif (b > a and b > c):
        res = b
    elif (c > b and c > a):
        res = c
    elif ((a == b and a > c)or(a == c and a > b)or(b == c and b > a) ):
        res = "Los numeros mayores son iguales"
    return res





class Comparacion(object):

    def __init__(self,listap):
        self.listap = listap


    # Ejercicio 3
    def tamlista(self):
        contador = 0
        for i in self.listap:
            contador = contador +1
        return contador



    def printposiciones(self,pos): #Para pruebas
        return self.listap[pos]



    # Ejercicio 4
    def compare_vocal(self,pos):

        validador = ()
        vocales = ("aeiou")

        for i in vocales:
            if self.listap[pos] == i:
                    validador = True


        if validador != True:
            validador = False

        return validador



    # Ejercicio 5.A
    def sum(self):

        acomulado = 0

        for i in self.listap:
            acomulado = acomulado + i

        return acomulado



    # Ejercicio 5.B
    def mult(self):

        acomulado = 0

        for i in self.listap:
            if acomulado == 0:
                acomulado = acomulado + i
            else:
                acomulado = acomulado * i

        return acomulado



    # Ejercicio 6
    def get_histograma(self):
        for i in self.listap :
            lsp = []
            a = 0

            while i > a:
                lsp.append("*")
                a += 1
            print "".join(lsp)

        return "HISTOGRAMA DE LA LISTA \n \t{}".format(self.listap)






listas=[3,1,5,7,'abc',3,131]
list2 = 'Hola'
listan =[14,2,3,4,5,47]
listahis = [4,9 ,7]


print max(524,524)                              #Ejercicio 1
print max3(1582,865,865)                        #Ejercicio 2
print Comparacion(list2).tamlista()             #Ejercicio 3
print Comparacion(list2).compare_vocal(3)       #Ejercicio 4
print list2[3]
print Comparacion(listan).sum()                 #Ejercicio 5.A
print Comparacion(listan).mult()                #Ejercicio 5.B
print "\n"
print Comparacion(listahis).get_histograma()    #Ejercicio 6





# #ejercicio 6 definir un histograma procedimiento() que tome una lista de numeros enteros e imprima un histogramaen
#     la pantalla. Ejemplo: procedimiento([4,9 ,7]) deberia imprimir lo siguiente
#     ****
#     *********
#     *******
#