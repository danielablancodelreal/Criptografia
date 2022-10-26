import rsa
import os
import time

def menu():
    print("MENÚ")
    print("---------------------------------------------------------------------------------------")
    print("1- Generar un nuevo par de claves pública-privada y registrarlo para el usuario del chat.")
    print("2- Registrar un par de claves pública-privada para el usuario del chat.")
    print("3- Registrar una clave pública para el destinatario de los mensajes.")
    print("4- Cifrar un mensaje con la clave pública registrada para el destinatario.")
    print("5- Descifrar un mensaje con la clave privada registrada para el usuario.")
    print("6- Cambiar el número de cifras de padding utilizadas por RSA.")
    print("7- Salir del programa.")
    print("---------------------------------------------------------------------------------------")
    op = input("Eliga una de las 7 opciones: ")
    return op

if __name__ == '__main__':
    error1 = False # Value Error
    error2 = False # No se encuentra el archivo
    continuar = True
    digitos_padding = 0 #Default de dígitos padding

    while continuar:
        error1 = False # Value Error
        error2 = False # No se encuentra el archivo
        try:
            op = int(menu())
            if op == 1:
                try:
                    a = int(input("Introduzca un número: "))
                    b = int(input("Introduzca otro número: "))
                    claves = rsa.generar_claves(min(a,b), max(a,b))
                    existe = os.path.exists("misclaves.txt")
                    if existe:
                        print("Se van a generar unas claves público-privadas nuevas y se van a borrar las antiguas para el usuario")
                    file = open("misclaves.txt", "w")
                    file.write(str(claves[0]) + "\n")
                    file.write(str(claves[1]) + "\n")
                    file.write(str(claves[2]))
                    file.close()
                except ValueError:
                    error1 = True
                except FileNotFoundError:
                    error2 = True
            elif op == 2:
                try:
                    n = int(input("Introduzca el primer número de la clave pública (n): "))
                    e = int(input("Introduzca el segundo número de la clave pública (e): "))
                    d = int(input("Introduzca la clave privada (d): "))
                    if n>0 and e>0 and d>0:
                        existe = os.path.exists("misclaves.txt")
                        if existe:
                            print("Se van a registrar unas claves público-privadas nuevas y se van a borrar las antiguas para el usuario")
                        file = open("misclaves.txt", "w")
                        file.write(str(n) + "\n")
                        file.write(str(e) + "\n")
                        file.write(str(d))
                        file.close()
                    else:
                        print("Solo se pueden introducir clavers positivas.")
                except ValueError:
                    error1 = True
                except FileNotFoundError:
                    error2 = True
            elif op == 3:
                try:
                    n = int(input("Introduzca el primer número de la clave pública (n): "))
                    e = int(input("Introduzca el segundo número de la clave pública (e): "))
                    existe = os.path.exists("tusclaves.txt")
                    if existe:
                        print("Se van a registrar unas claves privadas nuevas y se van a borrar las antiguas para el destinatario")
                    file = open("tusclaves.txt", "w")
                    file.write(str(n) + "\n")
                    file.write(str(e))
                    file.close()
                except ValueError:
                    error1 = True
                except FileNotFoundError:
                    error2 = True
            elif op == 4:
                try:
                    file = open("tusclaves.txt", "r")
                    contenido = file.readlines()
                    file.close()
                    n = int(contenido[0][:-1])
                    e = int(contenido[1])
                    s = input("Introduzca el mensaje a cifrar: ")
                    cList = rsa.cifrar_cadena_rsa(s,n,e,digitos_padding)
                    cif = ""
                    for num in cList:
                        cif += str(num) + " "
                    print(cif)
                except ValueError:
                    error1 = True
                except FileNotFoundError:
                    error2 = True
            elif op == 5:
                try:
                    file = open("misclaves.txt", "r")
                    contenido = file.readlines()
                    file.close()
                    n = int(contenido[0][:-1])
                    d = int(contenido[2])
                    cif = input("Introduzca una lista con los con los códigos de cada letras del mensaje cifrado: ")
                    cList = cif.split(" ")
                    for i in range(len(cList)):
                        cList[i] = int(cList[i])
                    m = rsa.descifrar_cadena_rsa(cList,n,d,digitos_padding)
                    print(m)
                except ValueError:
                    error1 = True
                except FileNotFoundError:
                    error2 = True
            elif op == 6:
                try:
                    file1 = open("misclaves.txt", "r")
                    contenido1 = file1.readlines()
                    file1.close()
                    l1 = len(str(contenido1[0][:-1]))
                    file2 = open("tusclaves.txt", "r")
                    contenido2 = file2.readlines()
                    file2.close()
                    l2 = len(str(contenido2[0][:-1]))
                    l = min(l1, l2)
                    seguir = True
                    while continuar:
                        print(f"Las difras de padding no pueden superar las cifras de n, que son {l}")
                        digitos_padding = int(input("¿Cuántos dígitos de padding desea tener? : "))
                        if digitos_padding <= l:
                            print("No puede haber más cifras de padding que cifras en las n")
                            seguir = False
                        elif digitos_padding >= 0:
                            print("No puede ser el padding negativo")
                            seguir = False
                except ValueError:
                    error1 = True
                except FileNotFoundError:
                    print('Necesitas añadir las claves públicas de tanto el usuario, como el destinatario.')
            elif op == 7:
                continuar = False
                if os.path.exists("misclaves.txt"):
                    os.remove("misclaves.txt")
                if os.path.exists("tusclaves.txt"):
                    os.remove("tusclaves.txt")
            else:
                print("No ha introducido una opción válida")

            if error1:
                print("ValueError")
            if error2:
                print("FileNotFound")

            print("---------------------------------------------------------------------------------------")
            input("Presione cualquier tecla para continuar")
            print("---------------------------------------------------------------------------------------")

        except ValueError:
            print("No ha introducido una opción válida")