from functools import reduce
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
        return str(reduce(lambda a, b: str(a) + ' | ' + str(b), self.pieces[1:])) if len(self) > 1 else 'empty'

    def __len__(self) -> int:
        return len(self.pieces)

    def append(self, piece: Piece) -> float:
        self.lastPiecePos += self.pieces[-1].getMinDistance(piece)
        self.pieces.append(piece)
        return self

    def calculateWasteMtx(self):
        """
        retorna uma matriz com a perda ao se inserir uma peça ao lado de outra
        mtx[x][y] -> perda ao inserir y à direita de x
        obs.: buscando em relação ao indice 0, obtem a perda no inicio ou ao fim
        """
        mtx = []
        for piece in self.pieces:
            wasteArr = []
            for piece2 in self.pieces:
                if piece != piece2:
                    wasteArr.append(piece.calculateWaste(piece2))
                else:
                    wasteArr.append(None)
            mtx.append(wasteArr)

        return mtx

    def draw(self, windowName, delay=100, xMult=1):
        view.reset(
            (self.lastPiecePos + self.pieces[-1].getRightPoint()) * xMult)
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

    def calculateWaste(self, ignotreFinalWaste=False):
        totalWaste = 0

        for (idx, piece) in enumerate(self.pieces):
            if idx == 0:
                continue

            totalWaste += self.pieces[idx-1].calculateWaste(piece)

        # usado para calcular a perda no final
        if not ignotreFinalWaste:
            totalWaste += self.pieces[-1].calculateWaste(self.pieces[0])

        return totalWaste
    # TODO: adapt code to class heuristic Solver

    def greedyHeuristicSolve(self):
        wasteMtx = self.calculateWasteMtx()
        usedPieces = []
        currentPiece = 0
        result = Sheet()

        while len(result) < len(self):
            usedPieces.append(currentPiece)
            minWaste = None

            for idx, waste in enumerate(wasteMtx[currentPiece]):
                if idx not in usedPieces:
                    minWaste = (waste, idx) if (
                        minWaste is None or waste < minWaste[0]) else minWaste

            currentPiece = minWaste[1]
            result.append(self.pieces[currentPiece])

        return result
