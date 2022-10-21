import modular
import random

def generar_claves(min_primo, max_primo):
    lista_primos = modular.lista_primos(min_primo,max_primo)
    p1 = lista_primos.pop(random.randint(0,len(lista_primos)-1))
    p2 = lista_primos.pop(random.randint(0,len(lista_primos)-1))
    n = p1*p2
    phin = (p1-1)*(p2-1)
    continuar = True
    while continuar:
        d = random.randint(1,phin)
        if modular.coprimos(d,phin):
            continuar = False
    e = modular.inversa_mod_p(d,phin)
    claves = (n,e,d)
    return claves


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

def cifrar_rsa(m,n,e,digitos_padding):
    m = aplicar_padding(m,digitos_padding)
    c = modular.potencia_mod_p(m,e,n)

    return c

def descifrar_rsa(c,n,d,digitos_padding):
    m = modular.potencia_mod_p(c,d,n)
    m = eliminar_padding(m,digitos_padding)
    return m

def cifrar_cadena_rsa(s,n,e,digitos_padding):
    cList = []
    for i in range(len(s)):
        u = ord(str(s[i]))
        u = aplicar_padding(u,digitos_padding)
        cList.append(modular.potencia_mod_p(u,e,n))
    return cList

def descifrar_cadena_rsa(cList,n,d,digitos_padding):
    m = ""
    for i in range(len(cList)):
        t = modular.potencia_mod_p(int(cList[i]),d,n)
        t = eliminar_padding(t, digitos_padding)
        u = chr(t)
        m += u
    return m

def romper_clave(n,e):
    phin = modular.euler(n)
    d = modular.inversa_mod_p(e,phin)
    return d

def ataque_texto_plano(cList,n,e):
    d = romper_clave(n,e)
    print(d)
    mensaje = descifrar_cadena_rsa(cList,n,d,0)
    return mensaje


