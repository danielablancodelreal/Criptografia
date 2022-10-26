import rsa
import time

ini = time.time()
try:
    a = int(input("Introduzca un número: "))
    b = int(input("Introduzca otro número: "))
    claves = rsa.generar_claves(min(a,b), max(a,b))
    print("n: ", claves[0])
    print("e: ", claves[1])
except ValueError:
    error1 = True

fin = time.time()
print(f'Ha tardado {fin-ini}s')