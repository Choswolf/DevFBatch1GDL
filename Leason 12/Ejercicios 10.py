

class Zona_Metropolitana(object):
    def __init__(self,area_idustrial,area_comercial,area_residencial,areas_mixtas):
        self.area_industrial = area_idustrial
        self.area_comercial = area_comercial
        self.area_residencial = area_residencial
        self.area_mixtas = areas_mixtas
    def construir_industria(self):
        print "Voy a construir en {}".format(self.area_industrial)
    def crear_negocio(self):
        print "Voy a crearlo en {}".format(self.area_comercial)
    def demoler(self):
        print "Voy a demoler"

class Ciudad(Zona_Metropolitana):
    def __init__(self,area_idustrial,area_comercial,area_residencial,areas_mixtas,colonia,lugar_eventos):
        super(Ciudad,self).__init__(area_idustrial,area_comercial,area_residencial,areas_mixtas)
        self.colonia = colonia
        self.lugar_eventos = lugar_eventos

    def construir_casa(self):
        print "construir casa en la zona {} y la colonia {}".format(self.area_comercial,self.colonia)

    # def planear_evento(self):
    #     print ''



guadalajara = Zona_Metropolitana('Corredor industrial el Salto',['Andares','Galerias'],'La Calma','lazaro cardenas')
cdmx = Zona_Metropolitana('Tlahuac','Polanco','La roma','Santa fe')


guadalajara.crear_negocio()
cdmx.crear_negocio()

elsalto = Ciudad('Corredor industrial el Salto','Plaza','casas x','zona x','eme','record')

elsalto.construir_casa()