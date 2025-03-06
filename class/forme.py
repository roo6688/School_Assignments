class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    def deplacementX(self, dep):
        self.__x += dep
    
    def deplacementY(self, dep):
        self.__y += dep
    def __str__(self):
        return (f"({self.__x}, {self.__y})")
    
class Droite(Point):
    def __init__(self, pointA, pointB):
        self.__pointA = pointA
        self.__pointB = pointB
    @property
    def pointA(self):
        return self.__pointA
    
    @property
    def pointB(self):
        return self.__pointB

    def deplacementX(self, dep):
        self.__pointA.deplacementX(dep)
        self.__pointB.deplacementX(dep)

    def deplacementY(self, dep):
        self.__pointA.deplacementY(dep)
        self.__pointB.deplacementY(dep)

    def __str__(self):
        return (f"({self.__pointA}, {self.__pointB})")
    
    def pente(self):

        if self.pointB.x == self.pointA.x:
            return None
        elif self.pointB.y == self.pointA.y:
            return 0
        else: 
            m = (self.pointB.y - self.pointA.y) / (self.pointB.x - self.pointA.x)
            return m
        
    def perpendiculaire(self, autre):
        
        if (self.pente() is None and autre.pente() == 0) or (self.pente() == 0 and autre.pente() is None):
            return True
        
        elif (self.pente() is not None) and (autre.pente() is not None) and (self.pente() * autre.pente() == -1):
            return True

        else:
            return False
class Quad(Droite):
    def __init__(self, droite1, droite2, droite3, droite4):
        self.__droite1 = droite1
        self.__droite2 = droite2
        self.__droite3 = droite3
        self.__droite4 = droite4
    
    @property
    def droite1(self):
        return self.__droite1
    
    @property
    def droite2(self):
        return self.__droite2
    
    @property
    def droite3(self):
        return self.__droite3
    
    @property
    def droite4(self):
        return self.__droite4

    def deplacementX(self, dep):
        self.__droite1.deplacementX(dep)
        #self.__droite2.deplacementX(dep)
        self.__droite3.deplacementX(dep)
        #self.__droite4.deplacementX(dep)

    def deplacementY(self, dep):
        self.__droite1.deplacementY(dep)
        #self.__droite2.deplacementY(dep)
        self.__droite3.deplacementY(dep)
        #self.__droite4.deplacementY(dep)

    def __str__(self):
        return (f"({self.__droite1} / {self.__droite2} / {self.__droite3} / {self.__droite4})")
    
    
        

    def estUnCarre(self):
        if droite1.perpendiculaire(droite2) and droite2.perpendiculaire(droite3) and droite3.perpendiculaire(droite4) and droite4.perpendiculaire(droite1):
            return True
        else:
            return False



if __name__ == "__main__":
    point1 = Point(5,5)
    point2 = Point(8,5)
    point3 = Point(8,2)
    point4 = Point(5,2)
    droite1 = Droite(point1, point2)
    droite2 = Droite(point2, point3)
    droite3 = Droite(point3, point4)
    droite4 = Droite(point4, point1)
    quad1 = Quad(droite1, droite2, droite3, droite4)
    quad1.deplacementY(1000)
    print(quad1)

    



