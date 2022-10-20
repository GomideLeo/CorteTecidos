from model.Piece import Piece
from model.Sheet import Sheet

filename = './examples/ex01.txt'
sheet = []

with open(filename, 'r') as f:
    nPieces = int(f.readline())

    for line in f:
        if nPieces == 0:
            break

        piece = line.split()
        sheet.append(Piece(float(piece[0]), float(piece[1]), float(piece[2])))

        nPieces -= 1

sheetObj = Sheet(sheet)
print(sheetObj.calculateWasteMtx())
newComb = (sheetObj.findBestArrangement(displayTest=False))
Sheet(newComb).draw("window", 0, 10)
greedySolve = sheetObj.greedyHeuristicSolve()
greedySolve.draw("window", 0, 10)
# print(Sheet(sheet).draw("window", 0, 10))
