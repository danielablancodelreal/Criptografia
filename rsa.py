import modular
import random
import math
from typing import List, Tuple

def generar_claves(min_primo: int, max_primo: int) -> Tuple[int, int, int]: 
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


def aplicar_padding(m: int, digitos_padding: int) -> int:
    m = str(m)
    for i in range(0,digitos_padding):
        m += str(random.randint(0,9))
    m = int(m)
    return m

def eliminar_padding(m: int, digitos_padding: int) -> int:
    m = str(m)
    m = m[:-digitos_padding]
    m = int(m)
    return m

def cifrar_rsa(m: int, n: int, e: int, digitos_padding: int) -> int:
    if digitos_padding > 0:
        m = aplicar_padding(m,digitos_padding)
    c = modular.potencia_mod_p(m,e,n)
    return c

def descifrar_rsa(c: int, n: int, d: int, digitos_padding: int) -> int:
    m = modular.potencia_mod_p(c,d,n)
    if digitos_padding > 0:
        m = eliminar_padding(m,digitos_padding)
    return m

def cifrar_cadena_rsa(s: str, n: int, e: int, digitos_padding: int) -> List[int]:
    cList = []
    for i in range(len(s)):
        u = ord(str(s[i]))
        cList.append(cifrar_rsa(u,n,e,digitos_padding))
    return cList

def descifrar_cadena_rsa(cList: List[int], n: int, d: int, digitos_padding: int) -> str:
    m = ""
    for i in range(len(cList)):
        t = descifrar_rsa(cList[i],n,d,digitos_padding)
        u = chr(t)
        m += u
    return m

def romper_clave(n: int, e: int) -> int:
    phin = modular.euler(n)
    d = modular.inversa_mod_p(e,phin)
    return d

def ataque_texto_plano(cList: List[int], n: int, e: int) -> str:
    d = romper_clave(n,e)
    mensaje = descifrar_cadena_rsa(cList,n,d,0)
    return mensaje

def ataque_rsa(cList: List[int], n: int, e: int) -> str:
    x = math.ceil(2*math.sqrt(n))
    continuar = True
    while continuar:
        s = x**2 - 4*n
        if math.sqrt(s) != int(math.sqrt(s)):
            x += 1
        else:
            y = math.sqrt(s)
            continuar = False
    p = int((1/2)*(x-y))
    q = int((1/2)*(x+y))

    phin = (p-1)*(q-1)
    d = modular.inversa_mod_p(e,phin)

    return descifrar_cadena_rsa(cList,n,d,0)
