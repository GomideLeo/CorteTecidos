import numpy as np
import util.colorGenerator
import math
import cv2

view = np.zeros((100, 0, 3), dtype = "uint8")
colorgen = util.colorGenerator.createColorGenerator()

def destroyAll():
    cv2.destroyAllWindows()

def reset(width = 500, height = 100):
    global view
    global colorgen

    view = np.zeros((height, math.ceil(width), 3), dtype = "uint8")
    colorgen = util.colorGenerator.createColorGenerator()

def addPoly(poly):
    cv2.fillPoly(view, poly, next(colorgen))

def show(windowName, delay = 100):
    cv2.imshow(windowName, view)
    cv2.waitKey(delay)

def destroyWindow(winname):
    cv2.destroyWindow(winname)