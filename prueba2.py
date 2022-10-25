import math 

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

###################################################################

def potencia_mod_p(base, exp, p):
    if p == 0:
        return
    if exp < 0: 
        phip = euler(p)
        exp //= -phip
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


print(potencia_mod_p(9,-8,11))