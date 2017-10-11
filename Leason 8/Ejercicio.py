class Workers(object):
    monto_para_aumento = 1.04
    numero_de_empleados = 0
    def __init__(self,name,surname,salary):
        self.name = name
        self.surname = surname
        self.email = name + "." + surname + "@company.com"
        self.salary = salary

        Workers.numero_de_empleados += 1

    #
    # def fullname(self):
    #     return'{} {}'.format(self.name,self.surname)
    #
    # def get_salary(self):
    #     return self.salary
    #
    # def get_name(self):
    #     return self.name
    #
    #
    # def aplicar_aumento(self):
    #     self.salary = int(self.salary * self. monto_para_aumento)

# print Workers.numero_de_empleados

worker_1 = Workers("Hugo","Mecalco",80000)
worker_2 = Workers("User","login",90000)
worker_5 = Workers("Juan","Neo",82000)
# print worker_1
# print worker_2
print worker_1.name
# # print worker_1.email
# print worker_1.get_salary()
# print worker_2.email
#
# print worker_1.get_name()
# print Workers.get_name(worker_1)
# print Workers.numero_de_empleados
# print worker_1.get_position()
# print Workers.get_salary(worker_2)
#
# print worker_2.__dict__

#
# class Tvs:
#     cuantas_tvs = 0
#     def __init__(self, marca, pais_fabricante , tipo, precio, mercado):
#         self.marca = marca
#         self.pais_fabricante = pais_fabricante
#         self.tipo = tipo
#         self.precio = precio
#         self.mercado = mercado
#         Tvs.cuantas_tvs += 1
#
#     def get_marca(self):
#         return self.marca
#     def get_pais_fabricante(self):
#         return self.pais_fabricante
#     def get_tipo(self):
#         return self.tipo
#     def get_precio(self):
#         return int(self.precio* 1.16) #Se define IVA
#     def get_mercado(self):
#         return self.mercado
#
#
# tv1 = Tvs("Samsung", "Corea del Sur","LED",11500, "Familia")
# tv2 = Tvs("TotalScren", "China","LCD",2000,"Empresarial")
# tv3 = Tvs("Asus","China","LED",15000,"Gamer")
#
# # print  Tvs.get_precio(tv1)
# # print tv1.precio()
# #
# print tv1.marca
# # print tv2.get_precio()
# print Tvs.cuantas_tvs

class Developer(Workers):
    monto_para_aumento = 1.10
    def __init__(self,name,surname,salary,prog_lang):
        super(Developer, self).__init__(name,surname,salary)
        self.prog_lang = prog_lang

# dev_1 = Developer("Julio","Angel",9000,"C")
dev_2 = Developer("Angel","PEres",3123,"Python")