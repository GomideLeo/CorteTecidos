from model.BranchBoundSolver import BranchBoundSolver
from model.BruteForceSolver import BruteForceSolver
from model.HeuristicSolver import HeuristicSolver
from model.Piece import Piece
from model.Sheet import Sheet

filename = './examples/ex03.txt'
pieces = []

with open(filename, 'r') as f:
    nPieces = int(f.readline())

    for line in f:
        if nPieces == 0:
            break

        piece = line.split()
        pieces.append(Piece(float(piece[0]), float(piece[1]), float(piece[2])))

        nPieces -= 1

sheet_non_treated = Sheet(pieces)

bf = BruteForceSolver(sheet_non_treated)
sheet_bf = Sheet(bf.findSolution())
sheet_bf.draw("window", 0, 10)
print("bf_waste = ", sheet_bf.calculateWaste(), ", totalEval = ", bf.totalEvaluations)

bb = BranchBoundSolver(sheet_non_treated)
sheet_bb = Sheet(bb.findSolution())
sheet_bb.draw("window", 0, 10)
print("bb_waste = ", sheet_bb.calculateWaste(), ", totalEval = ", bb.totalEvaluations)

hs = HeuristicSolver(sheet_non_treated)
sheet_hs = Sheet(hs.findSolution())
sheet_hs.draw("window", 0, 10)
print("hs_waste = ", sheet_hs.calculateWaste(), ", totalEval = ", hs.totalEvaluations)
