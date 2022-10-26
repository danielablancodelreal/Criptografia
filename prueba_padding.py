import modular
import random

def aplicar_padding(m,digitos_padding):
    m = str(m)
    for i in range(0,digitos_padding):
        m += str(random.randint(0,9))
    m = int(m)
    return m

def eliminar_padding(m,digitos_padding):
    m = str(m)
    m = m[:-digitos_padding]
    m = int(m)
    return m



if __name__ == "__main__":

    m = aplicar_padding(45342,3)
    print(m)
    print(eliminar_padding(m,3))

