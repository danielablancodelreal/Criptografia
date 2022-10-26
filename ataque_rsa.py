import rsa
import math
import modular
import time

ini = time.time()
n = 41822862350053
e = 34175116403509

cif = '15345944278248 19103703418576 29140591527782 5504951372629 42651683427 13065609939906 19103703418576 42651683427 41570693672736 29495746220673 42651683427 15851586779796 13065609939906 29495746220673 19103703418576 21314414282007 31854921190548 13065609939906 42651683427 21279656858353 28952064507959 19813200902259 15714144372027 21314414282007 20735851352733 5504951372629'
cList = cif.split(" ")
for i in range(len(cList)):
    cList[i] = int(cList[i])

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

print(rsa.descifrar_cadena_rsa(cList,n,d,0))

fin = time.time()

print(f'Ha tardado {fin-ini}s')