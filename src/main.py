import os
from model.BranchBoundSolver import BranchBoundSolver
from model.BruteForceSolver import BruteForceSolver
from model.HeuristicSolver import HeuristicSolver
from model.Piece import Piece
from model.Sheet import Sheet
import time


dirname = './examples/generated'

for filename in os.listdir(dirname):
    pieces = []
    # print(filename)
    with open(os.path.join(dirname, filename), 'r') as f:
        nPieces = int(f.readline())

        for line in f:
            if nPieces == 0:
                break

            piece = line.split()
            pieces.append(
                Piece(float(piece[0]), float(piece[1]), float(piece[2])))

            nPieces -= 1

    print("Arquivo:", os.path.join(dirname, filename))
    sheet_non_treated = Sheet(pieces)

    t0 = time.time()
    bf = BruteForceSolver(sheet_non_treated)
    sheet_bf = Sheet(bf.findSolution())
    t1 = time.time()
    sheet_bf.draw("window", 1000, 10)
    print("bf_waste = ", sheet_bf.calculateWaste(), ", totalEval = ",
          bf.totalEvaluations, ", total time of execution = ", t1 - t0)

    t0 = time.time()
    bb = BranchBoundSolver(sheet_non_treated)
    sheet_bb = Sheet(bb.findSolution())
    t1 = time.time()
    sheet_bb.draw("window", 1000, 10)
    print("bb_waste = ", sheet_bb.calculateWaste(), ", totalEval = ",
          bb.totalEvaluations, ", total time of execution = ", t1 - t0)

    t0 = time.time()
    hs = HeuristicSolver(sheet_non_treated)
    sheet_hs = Sheet(hs.findSolution())
    t1 = time.time()
    sheet_hs.draw("window", 1000, 10)
    print("hs_waste = ", sheet_hs.calculateWaste(), ", totalEval = ",
          hs.totalEvaluations, ", total time of execution = ", t1 - t0)

    print("==================================================")
