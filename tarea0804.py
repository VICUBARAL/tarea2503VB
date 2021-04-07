#Ejercicio 1
class FigurasGeometricasSuperficies:
    pass  # Para implementar luego. 

#Ejercicio2
class Rectangulo:
    def _init_(self,base,altura):
        self.base = base
        self.altura = altura

    def SuperficieRectangulo(self):
        area = self.base * self.altura

        return area

#Ejercicio3
class TrianguloRectangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def SuperficieTrianguloRectangulo(self):
        area = (self.base * self.altura)/2

        return area

#Ejercicio 4
class Coordenada:
    def _init_(self, x,y):
        self.x = x
        self.y = y

    @classmethod
    def new(self, x):
        return x

    @classmethod
    def new(self,y):
        return y   
    
#Ejercicio5
class RectanguloCoordenada:
    



       