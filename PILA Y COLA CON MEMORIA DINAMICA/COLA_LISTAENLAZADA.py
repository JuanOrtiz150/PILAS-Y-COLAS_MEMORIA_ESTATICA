class Nodo:
    def __init__(self, x):
        self.x = x
        self.sig = None


class Cola():
    def __init__(self):
        self.head = None

    def Enqueue(self, x):

        if self.head == None:
            self.head = Nodo(x)
            return

        temp = self.head
        while temp.sig != None:
            temp = temp.sig

        temp.sig = Nodo(x)

    def Dequeue(self) -> str:
        if self.head == None:
            return
        temp = self.head
        self.head = self.head.sig
        return temp.x

    def vaciar_pila(self):
        self.head = None
        self.tail = None
        print("[LA PILA YA ESTA VACIA]")

    def imprimir(self):
        nodo_temporal = self.head
        print("\n PILA: \n")
        while nodo_temporal != None:
            print("[", nodo_temporal.x, "]")
            nodo_temporal = nodo_temporal.sig
        print("\n*******")


pila = Cola()

i = 0

while True:

    print(
        "***** \n ENQUEUE[1] \n DEQUEUE [2] \n VACIAR COLA[3] \n FINALIZAR [4] \n \n***** \n")
    resp = input("->")

    if resp == "1":
        if i == 12:
            while resp == "1":
                print("[COLA LLENA]")
                resp = input("->")
        else:

            print("Ingresa el dato que desees ingresar:")
            dato = input("=")
            pila.Enqueue(dato)
            pila.imprimir()
            i = i+1

    elif resp == "2":
        if i == 0:
            while resp == "2":
                print("[COLA VACIA]")
                resp = input("->")
        else:
            pila.Dequeue()
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
