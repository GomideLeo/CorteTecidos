import numpy as np


class Piece:
    def __init__(self, x1: float, x2: float, x3: float):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def __str__(self) -> str:
        return str(self.x1) + " " + str(self.x2) + " " + str(self.x3)

    """ 
    calcula a distância entre o ponto esquerdo superior de `self` e o de `other`
    """
    def appendRignt(self, other) -> float:
        return max(self.x1, self.x2 - other.x3)

    def draw(self, topLeftPos):
        topLeftPos = topLeftPos * 10
        topRightPos = topLeftPos + self.x1 * 10
        botRightPos = topLeftPos + self.x2 * 10
        botLeftPos = topLeftPos + self.x3 * 10

        pts = np.array([[topLeftPos, 0], [topRightPos, 0],
            [botRightPos, 100], [botLeftPos, 100]],
            np.int32)

        return [pts.reshape((-1, 1, 2))]

