# -*- coding: utf-8 -*_
#def Certificado(I9000,I22000="NA"):
#    print("aplicar{} o {}").format(I9000,I22000)

#Certificado("29sep")

def play(intento=1):
    respuesta = raw_input("¿De qué color es una naraja?")
    if respuesta != "naranja":
        if intento < 3:
            print "\nFallaste! Inténtalo de nuevo"
            intento +=1
           play(intento) # llamada recursiva
         else:
            print "\nYOU LOSE!"
else:
print "\nYou win!"


def printing():
    a,b,c = "string", 15,True
    mi_tupla =('hola mundo',2014)
    texto,anio = mi_tupla

    print str (a)
    print str (b)
    print str (c)
    print str (texto)
    print str (anio)

printing()