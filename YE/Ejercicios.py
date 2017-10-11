import requests

consulta = "red hot chili peppers, pulp fiction"
parametro = {'k': "287043-Dulce-43XT5NJE", 'q': consulta}

url = 'https://tastedive.com/api/similar?'
respuesta = requests.get(url, params=parametro)

#print(respuesta.url)
json_object_respuesta = respuesta.json()

#print(json_object_respuesta)


class Similar(object):
    def __init__(self, data):
        self.data = data
        self.info = data ['Info']
        self.results = data ['Results']
    def get_resultados (self):
        return Resultados(self.results)
    def get_busqueda(self):
        return self.info


class Resultados(object):
    def __init__(self,results):
        self.results = results

    def get_posicion(self,pos):
        return RR(self.results[pos])

class RR(object):
    def __init__(self,rr):
        self.rr = rr
        self.name = rr['Name']
        self.type = rr['Type']

    def get_RR(self):
        return self.rr

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type



prueba = Similar(json_object_respuesta['Similar'])
#resultado = prueba.get_busqueda()
#resultado2 = prueba.get_resultados().results[3]
#resultado3 = prueba.results
#print(resultado)
#print(resultado2)
#print(resultado3)
for i in range(len(prueba.get_resultados().results)):
    print ("{} , {}".format(prueba.get_resultados().get_nombre(i).get_name(), prueba.get_resultados().get_nombre(i).get_type()))

print prueba.get_resultados().get_nombre(3).get_name()
#class Busqueda()
    #def __init__(self, results):
        #self.results = results

   #def get_busqueda(self,posicion)
        #return Similar(self,posicion[0])