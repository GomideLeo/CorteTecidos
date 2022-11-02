from model.Sheet import Sheet

class HeuristicSolver:
    def __init__(self, sheet: Sheet) -> None:
        self.sheet = sheet
        self.bestFit = float('inf')
        self.bestArrangement = []
        self.totalEvaluations = 0
    
    def greedyHeuristicSolve(self) -> None:
        wasteMtx = self.sheet.calculateWasteMtx()
        usedPieces = []
        currentPiece = 0
        result = Sheet()

        while len(result) < len(self.sheet):
            usedPieces.append(currentPiece)
            minWaste = None

            for idx, waste in enumerate(wasteMtx[currentPiece]):
                self.totalEvaluations += 1
                if idx not in usedPieces:
                    minWaste = (waste, idx) if (
                        minWaste is None or waste < minWaste[0]) else minWaste

            currentPiece = minWaste[1]
            result.append(self.sheet.pieces[currentPiece])
        self.bestArrangement = result.pieces

    
    def findSolution(self) -> list:
        self.greedyHeuristicSolve()
        return self.bestArrangement