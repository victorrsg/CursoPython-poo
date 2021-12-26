# Ejercicio Avanzado
# 1. Crea una clase llamada Punto con sus dos coordenadas X e Y.
# 2. Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
# 3. Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
# 4.Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, o si es el origen.
# 5. Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
# (Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

import math

class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self)) # self para llamar al objeto
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
            
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y) )
        
    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))
        


class Rectangulo():
    def __init__(self,inicial=0,final=0):
        self.inicial = inicial
        self.final = final
    def base(self):
        self.base=abs(self.final.x-self.inicial.x)
        print("La base del rectángulo es {}".format(self.base))

    def altura(self):
        self.altura=abs(self.final.y-self.inicial.y)
        print("La altura del rectángulo es {}".format(self.altura))

    def area(self):
        self.base=abs(self.final.x-self.inicial.x)
        self.altura=abs(self.final.y-self.inicial.y)
        self.area=(self.base*self.altura)
        print("El área del rectángulo es {}".format(self.area))
    


# 1. Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
# 2. Consulta a que cuadrante pertenecen el punto A, C y D.
# 3. Consulta los vectores AB y BA.
# 4. (Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
# 5. (Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
# 6. Crea un rectángulo utilizando los puntos A y B.
# 7. Consulta la base, altura y área del rectángulo. 

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)