# Realizar una cola con arrays maximo de 12 datos
# Autor: Juan Carlos Ortiz Salas
# Fecha: 09/10/23


def col():
    i = 0
    cola = [0]*13

    while True:

        print(
            "***** \n QUEUE[1] \n ENQUEUE [2] \n VACIAR COLA[3] \n FINALIZAR [4] \n \n***** \n")
        resp = input("->")

        if resp == "1":
            if i == 12:
                while resp == "1":
                    print("***COLA LLENA***")
                    resp = input("->")
            else:
                cola[i] = input("=")
                i = i+1
                print("\n ***COLA*** \n")
                print(cola)

        elif resp == "2":

            if i == 0:
                while resp == "2":
                    print("***COLA VACIA***")
                    resp = input("->")
            else:
                for j in range(i):
                    cola[j] = cola[j+1]
                print("\n ***COLA*** \n")
                print(cola)
                i = i-1

        elif resp == "3":
            if i == 0:
                while resp == "2":
                    print("***COLA VACIA***")
                    resp = input("->")
            else:
                try:
                    for j in range(i):
                        cola[j] = 0
                    i = 0
                except Exception:
                    return

        elif resp == "4":
            break

        else:
            while resp != "1" and resp != "2" and resp != "3" and resp != "4":
                resp = input("->")


col()
