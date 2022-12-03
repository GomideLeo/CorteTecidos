import time
from model.Sheet import Sheet


class BranchBoundSolver:
    TIMEOUT = 60 * 5  # 5 mins

    def __init__(self, sheet: Sheet) -> None:
        self.sheet = sheet
        self.bestFit = float('inf')
        self.bestArrangement = []
        self.totalEvaluations = 0

    def permute(self, toPermute, permuted=[]) -> None:
        if (time.time() - self.startTime > BranchBoundSolver.TIMEOUT):
            return

        if (len(toPermute) == 0):
            self.totalEvaluations += 1
            leafWaste = Sheet(permuted).calculateWaste()
            if leafWaste < self.bestFit:
                self.bestFit = leafWaste
                self.bestArrangement = permuted
            return

        for i in range(len(toPermute)):
            choice = permuted + [toPermute[i]]
            rest = toPermute[0:i] + toPermute[i + 1:]
            if Sheet(choice).calculateWaste() < self.bestFit:
                self.totalEvaluations += 1
                self.permute(rest, choice)

    def findSolution(self) -> list:
        self.startTime = time.time()
        self.permute(self.sheet.pieces[1:])
        return self.bestArrangement
