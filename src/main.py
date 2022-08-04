from model.Piece import Piece
import util.colorGenerator
import numpy as np
import cv2

my_img = np.zeros((100, 600, 3), dtype = "uint8")

filename = './examples/ex01.txt'
colorgen = util.colorGenerator.createColorGenerator()

with open(filename, 'r') as f: 
    nPieces = int(f.readline())
    topLeft = 0
    prev = None
    curr = None

    for line in f:
        if nPieces == 0: break

        piece = line.split()
        curr = Piece(float(piece[0]), float(piece[1]), float(piece[2]))

        if prev is not None:
            topLeft += prev.appendRignt(curr)
        else: 
            topLeft = max(0, -curr.x3)

        cv2.fillPoly(my_img, curr.draw(topLeft), next(colorgen))
        prev = curr

        nPieces -= 1

# a = Piece(10, 5, -2)
# cv2.fillPoly(my_img, a.draw(2), next(colorgen))

cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
