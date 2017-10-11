#circulo trangulo y cuadrado Crear 3 objetos

class Figura(object):
    def calcular_area(self,area):
        return area

class Circulo(Figura):

    def __init__(self,radio):
        self.area = 0
        self.radio = radio

    def calcular_area(self):
        area = ((self.radio ** 2)* 3.1416)
        return area

circulo = Circulo(2)
print (circulo.calcular_area())



#json

# import json
#
# json_file = open('marvel.json').read()
# json_data = json.load(json_file)
# print json_data['data']