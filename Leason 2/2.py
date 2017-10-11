# -*- coding: utf-8 -*_
def the_for():
    mi_lista = ['juan','antonio','juan']
    for nombre in mi_lista:
        print nombre
#the_for()

#Mazapan$2.5 Chocolate$1.4 Chicle$1.2 Tamarindo$4

# pregunta cuanto pones> Pregunta que quieres> calcula cuanto fue y cuanto devuelve

d1 , dP1 = 'a) Mazapan',2.5
d2 , dP2 = 'b) Chocolate',1.4
d3 , dP3 = 'c) Chicle', 1.2
d4 , dP4 = 'd) Tamarindo', 4

def lista():
    #nombres
    print "DULCES \n"
    print d1, " $" , dP1
    print d2, " $" , dP2
    print d1, " $", dP3
    print d2, " $", dP4

def wish():
    dulce = raw_input("¿Que dulce quieres?(letra)")
    if dulce in ("a","b","c","d"):
        insertar(dulce)
    else:
        print "No aplica"
        wish()



#wish()
def insertar():
    moneda = input("De cuanto es tu moneda\n") #valor moneda
    if(moneda > 5):
        print ("Cambio ${}\n".format(moneda))



def saldo():
    if (dulce == "a"):
        # precio = dP1
    if (dulce == "b"):
        # precio = dP2
    if (dulce == "c"):
        precio = dP3
    if (dulce == "d"):
        precio = dP4
    if (moneda => precio)



 #   eleccion= raw_input("que dulce quieres \n Mazapan ($2.50)\nChocolate  ($1.4) \nChicle ($1.2)\n Tamarindo ($4)") #elegir dulce

  #  print('{}'.format(moneda))
   # print('{}'.format(dulce))

def mut():
    for tabla in range(1,11):
        print "\nTabla del", tabla, "\n\n"
        for mult in range(1,11):
            res = tabla * mult
            print tabla, "*", mult,"=" ,res
# mut()




