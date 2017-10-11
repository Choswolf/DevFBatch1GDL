# my_set={1,3}

# def add_element_to_set():
#     my_set.add(2)
#     print('element',my_set)
#     my_set.update([2,3,4])
#
#     print('Elementos:',my_set)
#
#     my_set.update([4,5],{1,6,8})
#
#     print('Elem:',my_set)
#
#     my_set2={1,3,4,5,6}
#     print('set2',my_set2)
#
#     my_set2.discard(4)
#     print('set2', my_set2)
#
#     my_set3=set('HelloWorld')
#     #desordena la lista
#     print(my_set3)
#
#     #Pop random elementos
#     my_set3.pop()
#     print(my_set3)
#
#     my_set3.clear()
#
#
#     print(my_set3)
# add_element_to_set()


# Hacer union e interseccion con los siguientes sets:
#   A=set([1,2,3,4,5])
#   B=set([4,5,6,7,8])
def ejercio6():
    A={1,2,3,4,5}
    B=set([4,5,6,7,8])
    C= A & B
    D= A | B
    print C , 'Interseccion'
    print D ,  'Union'
    inter = A.intersection(B)
    print inter,"inter"
    inter = A.union(B)
    print inter, "Union"

def tupla1():
    my_tuple = ('mouse',[8,4,6],(1,2,3))
    a,b,c = my_tuple
    print my_tuple[2][0]
    print a
    print b[2]
    print c
# tupla1()

# Diccionario coleccion de elementos no ordenados

def crear_diccionario():
    # empty dictIONARY
    mydict = {}
    mydict= {1: 'apple',2: 'ball',3:'empirico','address': "ninos heroes 2560"}
    print mydict["address"]
    print mydict.get("das")
# crear_diccionario()

def cambiar_agregar_elementos():
    my_dict = {'name': 'julio', 'age': 24}
    my_dict ["domicilio"] = "rio autlan 1936"
    print(my_dict)
# cambiar_agregar_elementos()
# API REST
# JSON
# XML
# SOAP
# GRAP.QL

def ejerciciohugo():
    # squares = {x:x*x for x in range()6 }
    # print(squares)
    # equivalente
    squares = {}
    for x in range(6):
        squares[x]= x * x
        print squares
# ejerciciohugo()

#diccionario con datos de tu familia

def familia():
    tupla = {}
    x = input("Cuantos miembros son en tu familia?")
    for y in range (x):
        tupla[y] = raw_input("name")
        print tupla


# familia()


def ejercicioextra():
    numeros= {}
    print "Te imprimo numeros divisibles entre 7 pero no multiplos de 6 entre 2 numeros"
    x = input("Entre que numero 1r numero ")
    y = input("2do numero")
    for z in range(x,y+1):
        if(z%7 == 0) and (z%5 == 0):
            print z

ejercicioextra()