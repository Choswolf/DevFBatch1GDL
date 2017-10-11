def if_else_control():
    numero1 = 2
    numero2 = 4
    if numero1 > numero2:
        print "{} es mayor".format(numero1)
    elif numero1 >= numero2:
        print "{} es igual a {}".format(numero1,numero2)
    else:
        print("error")
if_else_control()