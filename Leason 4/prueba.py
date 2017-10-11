# a=input(" Dame vector 1 dame los puntos X y Y separados por ',' ")
#
# b=input(" Dame vector 2 dame los puntos X y Y separados por ',' ")

# a=(0, 0)
# b=(1, 1)
# Cuantos vectores np

def vectorescuadrados():
    A=input(" Dame punto 1 valor X,Y,..., separados por ',' \n")
    B=input(" Dame punto 2 valor X y Y separados por ',' \n")
    print A, B
    if len(A)== 2 and len(B)==2:
        distancia = (((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2)) ** .5
        print distancia
    else:
        print 'No es un vector de cuadrado'
#
# vectorescuadrados()



def vectoresnp():
    np=input("cuantas dimensiones?")
    A=input(" Dame punto 1 valor X,Y,...,n separados por ',' \n")
    B=input(" Dame punto 2 valor X,Y,...,n separados por ',' \n")
    print A, B
    if len(A)== np and len(B)==np:
        contador=0
        for x in range(np):
            contador = (contador +((A[x] - B[x]) ** 2))
        contador = (contador ** .5)
        print contador
    else:
        print 'No funciona asi'



vectoresnp()


