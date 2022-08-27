from model.Piece import Piece
from model.Sheet import Sheet

filename = './examples/ex02.txt'
sheet = []

with open(filename, 'r') as f: 
    nPieces =  int(f.readline())

    for line in f:
        if nPieces == 0: break

        piece = line.split()
        sheet.append(Piece(float(piece[0]), float(piece[1]), float(piece[2])))

        nPieces -= 1

newComb = (Sheet(sheet).findBestArrangement())
Sheet(newComb).draw("window", 0, 10)
# print(Sheet(sheet).draw("window", 0, 10))
