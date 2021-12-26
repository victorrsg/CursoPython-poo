# Creación de la clase
class Galleta():
    # Creación de atributos
    chocolate = False
    
    # Constructor __init__
    def __init__(self, sabor=None, forma=None): # self para indicar que es un método interno de la clase --- sabor y forma son atributos a crear
        self.sabor = sabor # self.sobar == sabor de nuestra clase y se refiere al atributo sabor de nuestro constructor(__init__)
        self.forma = forma
        if sabor is not None and forma is not None:
            print("Se acaba de crear una galleta {} y {}".format(sabor,forma))
    
    def chocolatear(self): # Nuevo método
        self.chocolate = True
        
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")


g = Galleta("salada","cuadrada") # Instanciación de objetos