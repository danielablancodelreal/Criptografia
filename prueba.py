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

###############################################################

def bezout_recursivo(a,b,l1,l2,mcd,a0,b0):
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

def bezout(a,b):
    m = mcd(a,b)
    return bezout_recursivo(a,b,[1,0],[0,1], m,a,b)

def inversa_mod_p(n,p):
    # Solo si son coprimos hay sol
    if coprimos(n,p):
        m, x, y = bezout(n,p)
        return x%p
        
print(inversa_mod_p(9,22))