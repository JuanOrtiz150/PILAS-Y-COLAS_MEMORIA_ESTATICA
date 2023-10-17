# Realizar una cola con listas enlazadas
# Autor: Juan Carlos Ortiz Salas
# Fecha: 13/10/23

class Nodo:
    def __init__(self, x):
        self.x = x
        self.sig = None


class Pila:
    def __init__(self):
        self.head = None

    def push(self, x):
        if self.head == None:
            self.head = Nodo(x)
            return
        nuevo_nodo = Nodo(x)
        nuevo_nodo.sig = self.head
        self.head = nuevo_nodo

    def pop(self):
        if self.head == None:
            print("\n [INGRESE UN DATO] \n ***LA PILA ESTA VACIA*** \n")
            return

        self.head = self.head.sig

    def vaciar_pila(self):
        self.head = None
        print("[LA PILA YA ESTA VACIA]")

    def imprimir(self):
        nodo_temporal = self.head
        print("\n PILA: \n")
        while nodo_temporal != None:
            print("[", nodo_temporal.x, "]")
            nodo_temporal = nodo_temporal.sig
        print("\n*******")


pila = Pila()

i = 0

while True:

    print(
        "***** \n PUSH[1] \n POP [2] \n VACIAR PILA[3] \n FINALIZAR [4] \n \n***** \n")
    resp = input("->")

    if resp == "1":
        if i == 12:
            while resp == "1":
                print("**PILA LLENA **")
                resp = input("->")
        else:
            print("Ingresa el dato que desees ingresar:")
            dato = input("=")

            pila.push(dato)
            pila.imprimir()
            i = i+1

    elif resp == "2":
        if i == 0:
            while resp == "2":
                print("**PILA VACIA**")
                resp = input("->")
        else:
            pila.pop()
            pila.imprimir()
            i = i-1

    elif resp == "3":
        pila.vaciar_pila()
        i = 0

    elif resp == "4":
        pila.vaciar_pila
        pila.imprimir()

        break

    else:
        while resp != "1" and resp != "2" and resp != "3" and resp != "4":
            resp = input("->")
