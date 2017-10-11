def get_messege():
    return ("{}, {} y {}")

def palabra(x,y):
    sum = x + y
    messege = get_messege().format(x,y,sum)
    print(messege)

def frase():
    palabra(1,6)


frase()

