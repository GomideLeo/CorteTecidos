import numpy as np
import model.Piece as Piece
import util.View as view

class Piece:
    def __init__(self, x1: float, x2: float, x3: float):
        if x1 < 0 or x2 < x3: raise Exception("Peça inválida")

        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def __str__(self) -> str:
        return str(self.x1) + " " + str(self.x2) + " " + str(self.x3)

    def getMinDistance(self, other: Piece) -> float:
        """ 
        calcula a distância entre o ponto esquerdo superior de `self` e o de `other`
        """ 
        return max(self.x1, self.x2 - other.x3)

    def calculateWaste(self, other: Piece, xMult = 1, height = 100) -> float:
        """ 
        calcula a quantidade de área que vai ser perdida entre `self` e `other`
        """
        otherAnchor = self.getMinDistance(other)

        if self.x1 > self.x2 - other.x3:
            # se a ponta do triangulo for na parte de cima
            return (otherAnchor + other.x3 - self.x2) * xMult * height / 2
        else:
            # se a ponta do triangulo for na parte de baixo
            return (otherAnchor - self.x1) * xMult * height / 2

    def getRightPoint(self) -> float:
        return max(self.x1, self.x2)

    def getLeftPoint(self) -> float:
        return min(0, self.x3)

    def getDrawArr(self, topLeftPos = 0, xMult = 1, height = 100):
        """ 
        Obtem o vetor para ser usado para desenhar a peça

        @param topLeftPos: posição onde a peça vai estar na view
        @param height: altura da view
        @param xMult: fator para multiplicar o eixo x (estético)
        """
        topLeftPos = topLeftPos * xMult
        topRightPos = topLeftPos + self.x1 * xMult
        botRightPos = topLeftPos + self.x2 * xMult
        botLeftPos = topLeftPos + self.x3 * xMult

        pts = np.array([[topLeftPos, 0], [topRightPos, 0],
            [botRightPos, height], [botLeftPos, height]],
            np.int32)

        return [pts.reshape((-1, 1, 2))]

    def draw(self, windowName, xMult = 1, height = 100):
        view.reset((self.getRightPoint() - self.getLeftPoint()) * xMult, height)
        view.addPoly(self.getDrawArr(-self.getLeftPoint(), xMult, height))
        view.show(windowName,0)

