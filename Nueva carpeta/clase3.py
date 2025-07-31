class numero:
    def __init__(self, numero):
        self.numero = numero
        
    def evaluar_numero(self):
        if self.numero & 1:
            print("impar")
        elif self.numero == 7:
            print("\nEl numero ingresado es un comodín")
        else:
            print("par")
            if self.numero == 10:
                print("\nEl numero ingresado es 10")
            
    def sumar(self, numeroasumar):
        return self.numero + numeroasumar
    
if __name__ == "__main__":
    
    numeroaevaluar = numero(int(input("Ingrese un numero: ")))
    numeroaevaluar.evaluar_numero()
    sumarealizada = numeroaevaluar.sumar(2)
    print("\nLa suma realizada es: ",sumarealizada)
    

