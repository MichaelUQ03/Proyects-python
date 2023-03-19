#CALCULADORA APRUEBA DE MOKYES

class CAM: #Crear una clase para una calculadora

    def get_number(self): #Definir una funcion que guardara varios numeros
        try: #no permitir que el usuario ingrese letras
            #Se podran ingresar varios numeros y se guardaran en una lista
            self.numbers = input("Ingrese los numeros que desea operar separados por coma: ").split(",")
            for i in range(len(self.numbers)): #Recorrer la lista
                self.numbers[i] = int(self.numbers[i]) #Convertir los numeros de la lista a enteros

        except ValueError: #Si el usuario ingresa letras
            print("Solo se permiten numeros") #Mostrar un mensaje de error
            self.get_number() #Volver a pedir los numeros
        except:
            print("Error desconocido")
            self.get_number()

    def get_operation(self): #Definir una funcion que guardara la operacion
        try: #no permitir que el usuario ingrese letras
            self.operation = input("Seleccione la operacion que desea realizar:\n1. Suma\n2. Resta \n3. Multiplicacion \n4. Division\nRespuesta: ") #Pedir la operacion
            if self.operation == "1": #Si la operacion es 1
                self.operation = "suma" #Guardar la operacion como suma
            elif self.operation == "2": #Si la operacion es 2
                self.operation = "resta" #Guardar la operacion como resta
            elif self.operation == "3": #Si la operacion es 3
                self.operation = "multiplicacion" #Guardar la operacion como multiplicacion
            elif self.operation == "4": #Si la operacion es 4
                self.operation = "division" #Guardar la operacion como division
            else: #Si la operacion no es ninguna de las anteriores
                print("Solo se permiten numeros del 1 al 4") #Mostrar un mensaje de error
                self.get_operation() #Volver a pedir la operacion
        except ValueError: #Si el usuario ingresa letras
            print("Solo se permiten numeros") #Mostrar un mensaje de error
            self.get_operation() #Volver a pedir la operacion
        except:
            print("Error desconocido")
            self.get_operation()

    def calculate(self): #Definir una funcion que calculara la operacion
        try: #no permitir que el usuario ingrese letras
            if self.operation == "suma": #Si la operacion es suma
                self.result = 0 #Guardar el resultado como 0
                for i in self.numbers: #Recorrer la lista de numeros
                    self.result += i #Sumar el numero a la variable result
            elif self.operation == "resta": #Si la operacion es resta
                self.result = self.numbers[0] #Guardar el resultado como el primer numero de la lista
                for i in range(1, len(self.numbers)): #Recorrer la lista de numeros
                    self.result -= self.numbers[i] #Restar el numero a la variable result
            elif self.operation == "multiplicacion": #Si la operacion es multiplicacion
                self.result = 1 #Guardar el resultado como 1
                for i in self.numbers: #Recorrer la lista de numeros
                    self.result *= i #Multiplicar el numero a la variable result
            elif self.operation == "division": #Si la operacion es division
                self.result = self.numbers[0] #Guardar el resultado como el primer numero de la lista
                for i in range(1, len(self.numbers)): #Recorrer la lista de numeros
                    self.result /= self.numbers[i] #Dividir el numero a la variable result
            else: #Si la operacion no es ninguna de las anteriores
                print("Solo se permiten numeros del 1 al 4") #Mostrar un mensaje de error
                self.get_operation() #Volver a pedir la operacion
        except ValueError: #Si el usuario ingresa letras
            print("Solo se permiten numeros") #Mostrar un mensaje de error
            self.get_operation() #Volver a pedir la operacion
        except:
            print("Error desconocido")
            self.get_operation()

    def show_result(self): #Definir una funcion que mostrara el resultado
        print("El resultado es: " + str(self.result)) #Mostrar el resultado

    def run(self): #Definir una funcion que ejecutara el programa
        self.get_number() #Pedir los numeros
        self.get_operation() #Pedir la operacion
        self.calculate() #Calcular la operacion
        self.show_result() #Mostrar el resultado

CAM().run() #se ejecuta la clase