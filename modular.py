import sys
import math

################################ funciones #####################################
def es_primo(n):
    # Cualquier número negativo no es primo
    # El 1 y el 0 no son números primos, el cero es divisible por cualquier número
    if n <= 1: 
        return False
    # Vemos si es par para que en el bucle se salte los pares
    if n%2 == 0: 
        return False
    # De entre los impares, va diviendo hasta la raíz cuadrada
    for i in range (3,int(math.sqrt(n)+1),2):
        if n%i == 0: 
            return False
    # Si no ha sido divisible por ninguna de las anteriores, es primo
    return True

def lista_primos(a,b):
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

def factorizar(n):
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

def mcd(a,b): ######################################## DEMASIADOS ARGS
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

def bezout(a,b,l1,l2,mcd,a0,b0): ######################################## DEMASIADOS ARGS
    if  a != mcd and b != mcd: #################### num negativoo (con la otra función)
        c = max(a,b) // min(a,b)
        if a > b:
            l1[0] -= l2[0] *c
            l1[1] -= l2[1] *c
            a = a%b
        elif b > a:
            l2[0] -= l1[0] *c
            l2[1] -= l1[1] *c
            b = b%a
        return bezout(a,b,l1,l2,mcd,a0,b0)
    if mcd == l1[0]*a0 + l1[1]*b0:
        return(mcd, l1[0], l1[1])
    else:
        return(mcd, l2[0], l2[1])

def coprimos(a,b):
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

def potencia_mod_p(base, exp, p):
    # Pequeño teorema de Fermat
    if p == 0:
        return
    if exp < 0: ################################################ CAMBIAR
        exp %= p
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

def inversa_mod_p(n,p):
    # Solo si son coprimos hay sol
    if coprimos(n,p):
        if n<0:
            n += p
            m, x, y = bezout(n,p,[1,1],[0,1], mcd(n,p),n,p)
        else: 
            m, x, y = bezout(n,p,[1,0],[0,1], mcd(n,p),n,p)
        return x%p

def euler(n):
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
