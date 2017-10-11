def p1():
    f= open("guru9e9.txt","w+")
    for i in range (0,10):
     f.write("This is line %d\r" % (i+1))
    f.close()

# p1()

def prueba():
    for x in [20,39,12,43]:print x,
# prueba()

mylist = [1,2,3,4,5,6]
def prueba2():
    print mylist[2]
    print mylist[2:5]
    print mylist[5:]
    print mylist[:4]
    print mylist[:]
# prueba2()

def prueba3 (lista):
    m = 0
    for i in range(len(lista)):
        if m < mylist[i] :
            m = mylist[i]
            print i, m



#prueba3(mylist)

# for elemento in mylist:
#     print elemento
#
# mylist.append(10)
# print mylist
#
# mylist.insert(4,"destiny")
# print mylist
#
# mylist.remove('destiny')
# print mylist
#
# mylist.pop()
# print (mylist)

def borrartodo(lista1):
    x = len(lista1)
    for y in range (x):
        print lista1
        lista1.pop()
    print lista1
    print "Prueba"
# borrartodo(mylist)


# lista2=[]
# for x in range(input('cuantas palabras?')):
#     lista2.append(raw_input("Escribe la palabra"))
# print lista2
#
# borrartodo(lista2)

# ip= [002.131.412.412]
# print ip
def IP ():
    ip = raw_input('escribe ip')
    print ip
    if len(ip) == 15:
    print("ok")
    for i in ip:
        if ((i == '1')or (i=='2')or(i=='3')or(i=='4')or(i=='5')or(i=='6')or(i=='7')or((i=='8')or(i=='9')or(i=='0')or(i=='.')):
            print i ,'ok'
        else:
            print 'error'
            break
    else:
    print 'error'
# IP()
# no funciona asi el OR
