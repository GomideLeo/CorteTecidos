import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--folder", default='./examples/generated',
                    type=str, help="Folder path to save generated files.")
parser.add_argument("-n", "--number", default=1,
                    type=int, help="Number of generated files.")
parser.add_argument("-s", "--size", default=4,
                    type=int, help="Size of files.")

args = parser.parse_args()

for i in range(args.number):
    f = open(args.folder + "/size_" + str(args.size) +
             "_" + str(i) + ".txt", "w")
    f.write(str(args.size))

    for j in range(args.size):
        x1 = random.randint(0, 25)
        x2 = random.randint(-25, 25)
        x3 = random.randint(-25, x2)

        f.write("\n"+str(x1) + " " + str(x2) + " " + str(x3))

    f.close()
