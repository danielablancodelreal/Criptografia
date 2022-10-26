import math
from typing import List, Tuple, Dict

################################ funciones #####################################
def es_primo(n: int) -> bool: 
    # Cualquier número negativo no es primo
    # El 1 y el 0 no son números primos, el cero es divisible por cualquier número
    if n <= 1: 
        return False
    # Si es 2 es primo
    if n == 2:
        return True
        # Vemos si es par para que en el bucle se salte los pares
    if n%2 == 0: 
        return False
    # De entre los impares, va diviendo hasta la raíz cuadrada
    for i in range (3,int(math.sqrt(n)+1),2):
        if n%i == 0: 
            return False
    # Si no ha sido divisible por ninguna de las anteriores, es primo
    return True

def lista_primos(a: int,b: int) -> List[int]:
    lista = []
    # Añadimos el 2 a la lista en caso de que el primer número sea menor o igual que este
    # aparte, incializamos la busqueda en 3, para saltarnos todos los primos.
    # Si b mayor que a, no hay solución
    if a <= 1:
        a = 2
    if a > b:
        return
    if a <= 2: 
        lista.append(2)
        a = 3 
    # Si el primer número es par, le sumamos 1
    if a%2 == 0: 
        a += 1
    # El bucle empieza en un número impar para ir de dos en dos hasta b
    for i in range(a,b+1,2):
        if es_primo(i): 
            lista.append(i)
    return lista

def factorizar(n: int) -> Dict[int, int]:
    n = abs(n)
    diccionario = {}
    i = 2
    a = n
    contador= 0
    while i*i <= a:
        if n%i == 0:
            contador += 1
            n = n//i
        else:
            if contador != 0: 
                diccionario[i] = contador
                contador = 0
            i += 1
            a = n
    if n > 1:
        diccionario[n] = 1
    return diccionario

def mcd(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return max(a,b)
    if a < 0 or b <0: 
        return 1
    elif a%b == 0 or b%a == 0: 
        return min(a,b)
    elif a == 0 or b == 0: 
        return max(a,b)
    else: 
        return mcd(min(a,b), max(a,b) % min(a,b))

def bezout_recursivo(a: int, b: int, l1: List[int], l2: List[int], mcd: int, a0: int, b0: int) -> Tuple[int,int,int]:
    if  a != mcd and b != mcd:
        if a > b and b < 0 and a > 0:
            l2[0] += l1[0]
            l2[1] += l1[1]
            b += a
        elif b > a and a < 0 and b > 0:
            l1[0] += l2[0]
            l1[1] += l2[1]
            a += b
        elif a > b:
            l1[0] -= l2[0]
            l1[1] -= l2[1]
            a -= b
        elif b > a:
            l2[0] -= l1[0]
            l2[1] -= l1[1]
            b -= a 
        return bezout_recursivo(a,b,l1,l2,mcd,a0,b0)
    if mcd == l1[0]*a0 + l1[1]*b0:
        return(mcd, l1[0], l1[1])
    else:
        return(mcd, l2[0], l2[1])

def bezout(a: int, b: int) -> Tuple[int,int,int]:
    m = mcd(a,b)
    return bezout_recursivo(a,b,[1,0],[0,1], m,a,b)

def coprimos(a: int, b: int) -> bool:
    # Si son negativos, se transforman a su valor absoluto
    if a < 0 or b < 0: 
        a = abs(a)
        b = abs(b)
    # Si uno de los dos es uno, son coprimos
    if a == 1 or b == 1: 
        return True
    # Si uno es divisible entre otro, no son coprimos
    elif a%b == 0 or b%a == 0: 
        return False
    # Si uno de los dos es cero, no son coprimos
    elif a == 0 or b == 0: 
        return False
    # Sino, simplificamos
    else: 
        return coprimos(min(a,b), max(a,b) % min(a,b))

def potencia_mod_p(base: int, exp: int, p: int) -> int:
    if p == 0:
        return
    if exp < 0: ################################################ CAMBIAR
        phip = euler(p)
        exp %= phip
    # Pequeño teorema de Fermat
    if exp == p and es_primo(p):
        return (base % p)
    # Si la base es 1, da igual el exponente
    elif base == 1:
        return base%p
    # Si el exponente es 0, el resulado es 1 módulo p
    elif exp == 0:
        return 1%p
    # Exponenciación binaria
    else:
        x = 1
        while exp > 0:
            if exp%2 == 1:
                x = (x*base)%p
            base = base*base%p
            exp = exp//2
        return x%p

def inversa_mod_p(n: int, p: int) -> int:
    # Solo si son coprimos hay sol
    if coprimos(n,p):
        m, x, y = bezout(n,p)
        return x%p

def euler(n: int) -> int:
    #Comprobamos que n es primo para poder aplicar una propiedad
    if es_primo(n):
        return n-1
    dic = factorizar(n)
    #Factorizamos ya que si mcd(a,b) = 1, euler(a*b) == euler(a)*euler(b)
    lista = list(dic.keys())
    contador = 1
    # euler(p**k) == (p-1)*p**(k-1)
    for i in range(len(lista)):
        contador *= (lista[i]-1)*(lista[i]**(dic[lista[i]]-1))
    return contador

def legendre(n: int, p: int) -> int: ################################################# MAL (no nos ha dado tiempo a cambiarla)
    #comprobamos que p es primo
    if not es_primo(p):
        return
    #calculamos el símbolo de Legendre según su definición
    elif n%p == 0: 
        return 0
    elif math.sqrt(n%p) == int(math.sqrt(n%p)): 
        return 1
    else: 
        return -1

def resolver_sistema_congruencias(a: List[int], b: List[int], p: List[int]) -> Tuple[int, int]: ################################################# FALTAN SIMPLIFICACIONES + VALORES NEGATIVOS
    if coprimos_n(p) == True:
        a_ec = []
        M = 1
        for i in range(len(a)):
            a_ec.append(inversa_mod_p(a[i],p[i])*b[i])
            M *= p[i]
            
        lista = []
        for j in range(len(a_ec)):
            lista.append(inversa_mod_p((M/p[j]), p[j]))
        
        x = 0
        for k in range(len(a_ec)):
            x += a_ec[k]*lista[k]*(M/p[k])
        
        return (int(x%M), M)

def mcd_n_recursivo(lista: List[int], a: int, n: int) -> int:
    m = mcd(a,lista[n])
    if n+1 == len(lista):
        return m
    return mcd_n(lista, m, n+1)

def mcd_n(lista: List[int]) -> int:
    return mcd_n_recursivo(lista,lista[0],1)

def coprimos_n(p: List[int]) -> bool:
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            divisor = mcd(p[i],p[j])
            if divisor > 1:
                return False
    return True

def raiz_mod_p(n: int,p: int) -> int:
    if es_primo(p) and p != 2:
        n %= p
        if n == 0:
            return n
        elif n == 1:
            return n, p-1
        elif legendre(n, p) == 0:
            return 0
        elif legendre(n**(p-1), p) == 1:
            for a in range(0,p):
                w = (((a**2-n)%p)**((p-1)/2))%p
                if int(w) == p-1:break
            exponente = ctb((p+1)/2,2)
            x1 = [a,1]
            x2 = mult(x1,x1,a**2-n,p)
            for i in range(1, len(exponente)):
                if exponente[i] == 0:
                    x2 = mult(x2,x1,a**2-n,p)
                    x1 = mult(x1,x1,a**2-n,p)
                else:
                    x1 = mult(x1,x2,a**2-n,p)
                    x2 = mult(x2,x2,a**2-n,p)
            return (x1[0], -x1[0]%p)
        else:
            return False

def mult(l1,l2,o,p):
    return [(l1[0]*l2[0]+l1[1]*l2[1]*o)%p,(l1[0]*l2[1]+l1[1]*l2[0]*o)%p]

def ctb(n,b):
    if n<2:
        return [n]
    t = n
    r = []
    while t!=0:
        r = [t%b] + r
        t /= b
    return r