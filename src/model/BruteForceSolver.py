import time
from model.Sheet import Sheet
import util.permutations as permutations
import cv2
import util.View as view


class BruteForceSolver:
    TIMEOUT = 60 * 5  # 5 mins

    def __init__(self, sheet: Sheet) -> None:
        self.sheet = sheet
        self.bestFit = float('inf')
        self.bestArrangement = []
        self.totalEvaluations = 0

    def bruteForce(self, delay=100, displayTest=True, testWinName="testing_views") -> None:
        for arrangement in permutations.permutations(self.sheet.pieces[1:]):
            self.totalEvaluations += 1
            sheetTest = Sheet(arrangement)
            waste = Sheet(arrangement).calculateWaste()
            if waste <= self.bestFit:
                self.bestArrangement = arrangement
                self.bestFit = waste
            if displayTest:
                sheetTest.draw(testWinName, delay, 10)
                cv2.waitKey()

            if (time.time() - self.startTime > BruteForceSolver.TIMEOUT):
                break
        if displayTest:
            view.destroyWindow(testWinName)

    def findSolution(self) -> list:
        self.startTime = time.time()
        self.bruteForce(displayTest=False)
        return self.bestArrangement
