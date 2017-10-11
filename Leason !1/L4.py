def get_messege():
    return "{}, \n{} y {}!!!"

def get_palabra(x,y,z):
    messege = get_messege().format(x, y, z)
    print(messege)
    return get_messege().format(x,y,z)

def frase():
    return(get_palabra("Lok'tar Ogar","Honor","Gloria"))

frase()

