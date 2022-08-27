from functools import reduce
from time import sleep
import util.View as view
import util.permutations as permutations
from model.Piece import Piece

class Sheet:
    def __init__(self, pieces: list[Piece] = []):
        self.pieces = [Piece(0, 0, 0)]
        self.lastPiecePos = 0
        for p in pieces:
            self.append(p)

    def __str__(self) -> str:
        return "empty" if len(self) <=1 else str(reduce(lambda a, b: str(a) + ' | ' + str(b), self.pieces[1:]))

    def __len__(self) -> int:
        return len(self.pieces)

    def append(self, piece: Piece) -> float:
        self.lastPiecePos += self.pieces[-1].getMinDistance(piece)
        self.pieces.append(piece)
        return self

    def draw(self, windowName, delay=100, xMult=1):
        view.reset((self.lastPiecePos + self.pieces[-1].getRightPoint()) * xMult)
        pos = 0
        totalWaste = 0

        for (idx, piece) in enumerate(self.pieces):
            if idx == 0:
                continue
            
            pos += self.pieces[idx-1].getMinDistance(piece)
            totalWaste += self.pieces[idx-1].calculateWaste(piece)
            
            view.addPoly(piece.getDrawArr(pos, xMult))
        
        # usado para calcular a perda no final
        totalWaste += self.pieces[-1].calculateWaste(self.pieces[0])

        view.show(windowName, delay)
        return totalWaste

    def calculateWaste(self):
        totalWaste = 0

        for (idx, piece) in enumerate(self.pieces):
            if idx == 0:
                continue
            
            totalWaste += self.pieces[idx-1].calculateWaste(piece)
        
        # usado para calcular a perda no final
        totalWaste += self.pieces[-1].calculateWaste(self.pieces[0])

        return totalWaste
    
    def findBestArrangement(self, delay=500, displayTest=True, testWinName="testing_views"):
        minComb = []
        minInt = None
        
        for arrangement in permutations.permutations(self.pieces[1:]):
            sheet_test = Sheet(arrangement)
            waste = Sheet(arrangement).calculateWaste()
            if (minInt == None or waste <= minInt):
                minComb = arrangement
                minInt = waste
            if displayTest:
                sheet_test.draw(testWinName, delay, 10)
        if displayTest:
            view.destroyWindow(testWinName)
        return minComb