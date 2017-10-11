import os
def cambiofotos():

    lista_de_nombres = os.listdir("C:\Users\julve\Downloads\images\prank")
    # print lista_de_nombres
    os.chdir("C:\Users\julve\Downloads\images\prank" )
    # print "Current working dir : %s" % os.getcwd()
    # print lista_de_nombres[2][3]
    tama = lista_de_nombres.__len__()
    len(lista_de_nombres)
    # print lista_de_nombres
    for file_name in lista_de_nombres:
        os.rename(file_name,file_name.translate(None,"1234567890"))

# cambiofotos()


def colas():
    from collections import deque
    queue = deque(["Eric","John","Michel"])

    # queue = ["Eric", "John", "Michel"]
    print (queue)
    queue.append("Terry")
    queue.append("Graham")
    # queue.pop() #ultimas entradas primeras salidas
    queue.popleft() #primeras entradas primeras salidas
    queue.popleft()
    print (queue)

colas()