colorList = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

def createColorGenerator():
    i = 0
    while True:
        yield colorList[i]
        i += 1
        i %= len(colorList)