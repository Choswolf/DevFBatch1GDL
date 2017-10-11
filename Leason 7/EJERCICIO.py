def ejercicio9(): #diccionario
    n=input("Cuantas palabras quieres escribir?")
    lista9=[]
    for x in range(n) :
        lista9.append(raw_input('Palabra {}'.format(x+1)))

    print lista9

# ejercicio9()

def ejercicio9B(): #Tupla
    n=input("Cuantas palabras quieres escribir?")
    lista9={}
    for x in range(n) :
        lista9[x] =(raw_input('Palabra {}'.format(x+1)))

    print lista9[input("Que numero quieres imprimir")-1]
    print lista9
# ejercicio9B()


def ejercicio9C(): #Lista
    n=input("Cuantas palabras quieres escribir?")
    lista9=[]
    for x in range(n) :
        lista9.append(raw_input('Palabra {}'.format(x+1)))

    print lista9

# ejercicio9C()


def ejercicio10():
    n = input("Cuantas palabras quieres escribir?")
    lista9 = []
    for x in range(n):
        lista9.append(raw_input('Palabra {}'.format(x + 1)))
    m= 'hola'
    # m = raw_input("Que palabra buscas?")
    contador =0
    for y in range(n):
        if m == lista9[y]:
            contador = contador+1
    print '{} se repite {} veces'.format(m,contador)
# ejercicio10()

def ejercicio10B():
    n = input("Cuantas palabras quieres escribir?")
    lista9 = []
    for x in range(n):
        lista9.append(raw_input('Palabra {}'.format(x + 1)))

    print len(filter(lambda x:x == 'hola',lista9))


ejercicio10B()

def ejercicio10B():
    n = input("Cuantas palabras quieres escribir?")
    lista9 = []
    c = 0
    for x in range(n):
        lista9.append(raw_input('Palabra {}'.format(x + 1)))




# x in cosa