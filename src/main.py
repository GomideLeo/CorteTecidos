from model.Piece import Piece
from model.Sheet import Sheet

filename = './examples/ex01.txt'
sheet = Sheet()

with open(filename, 'r') as f: 
    nPieces =  int(f.readline())

    for line in f:
        if nPieces == 0: break

        piece = line.split()
        sheet.append(Piece(float(piece[0]), float(piece[1]), float(piece[2])))

        nPieces -= 1

print(sheet.draw("window", 1000, 10))
