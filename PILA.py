# Realizar una pila con arrays maximo de 12 datos
# Autor: Juan Carlos Ortiz Salas
# Fecha: 09/10/23

def pil():
    i = 0
    pila = [0]*13

    while True:

        print("POSICION [", i, "]")

        print(
            "***** \n PUSH[1] \n POP[2] \n VACIAR PILA[3] \n FINALIZAR [4] \n \n***** \n")
        resp = input("->")

        if resp == "1":
            if i == 12:
                while resp == "1":
                    print("****PILA LLENA****")
                    print(pila)
                    resp = input("->")
            else:
                print("\n Ingresa el valor que desees ingresar en la pila")
                pila[i] = input("=")

                print("\n ***PILA*** \n")
                print(pila)
                i = i+1

        elif resp == "2":
            if i == 0:
                pila[i] = 0
                while resp == "2":
                    print("****LA PILA ESTA VACIA****")
                    print(pila)
                    resp = input("->")
            else:
                try:
                    pila[i-1] = 0
                    i = i-1
                    print("\n ***PILA*** \n")
                    print(pila)
                except Exception:
                    return

        elif resp == "3":
            if i == 0:
                while resp == "3":
                    print("****LA PILA ESTA VACIA****")
                    resp = input("->")
            else:
                for j in range(i):
                    pila[j] = 0

                i = 0

        elif resp == "4":
            break

        else:
            while resp != "1" and resp != "2" and resp != "3" and resp != "4":
                resp = input("->")


pil()
