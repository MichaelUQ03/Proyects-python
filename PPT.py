#Piedra papel o tiijera
import random

class Juego:
    def menu(self):
        print("Bienvenido a piedra papel o tijera\n1. Jugar\n2. Salir")
        try:
            self.operation = input("Seleccione la opcion que desea realizar: ")
            if self.operation == "1":
                self.operation = "jugar"
            elif self.operation == "2":
                self.operation = "salir"
            else:
                print("Solo se permiten numeros del 1 al 2")
                self.menu()
        except ValueError:
            print("Solo se permiten numeros")
            self.menu()

    def piedra(self):
        print("Piedra")
        self.jugada = "piedra"
        self.computadora()

    def papel(self):
        print("Papel")
        self.jugada = "papel"
        self.computadora()

    def tijera(self):
        print("Tijera")
        self.jugada = "tijera"
        self.computadora()

    def computadora(self):
        self.jugada_computadora = random.choice(["piedra", "papel", "tijera"])
        print("Computadora: " + self.jugada_computadora)
        self.resultado()

    def resultado(self):
        if self.jugada == self.jugada_computadora:
            print("Empate")
        elif self.jugada == "piedra":
            if self.jugada_computadora == "papel":
                print("Perdiste")
            elif self.jugada_computadora == "tijera":
                print("Ganaste")
        elif self.jugada == "papel":
            if self.jugada_computadora == "tijera":
                print("Perdiste")
            elif self.jugada_computadora == "piedra":
                print("Ganaste")
        elif self.jugada == "tijera":
            if self.jugada_computadora == "piedra":
                print("Perdiste")
            elif self.jugada_computadora == "papel":
                print("Ganaste")
        self.menu()

    def jugar(self):
        print("Jugar\nSeleccione una opcion:\n1. Piedra\n2. Papel\n3. Tijera")
        try:
            self.jugada = input("Seleccione la opcion que desea realizar: ")
            if self.jugada == "1":
                self.piedra()
            elif self.jugada == "2":
                self.papel()
            elif self.jugada == "3":
                self.tijera()
            else:
                print("Solo se permiten numeros del 1 al 3")
                self.jugar()
        except ValueError:
            print("Solo se permiten numeros")
            self.jugar()

    def salir(self):
        print("Salir")
        exit()

    def __init__(self):
        while True:
            self.menu()
            if self.operation == "jugar":
                self.jugar()
            elif self.operation == "salir":
                self.salir()
            else:
                print("Opcion invalida")
                self.menu()

juego = Juego()
#a





