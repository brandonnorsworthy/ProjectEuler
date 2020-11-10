#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

#you can only go down or right
gridsize = 2
choices = 0

def main():
    global choices
    showLocaiton(0,0)
    pathFinderX(0,0)
    print('# of choices:', choices)

def showLocaiton(locationX, locationY):
    for gridy in range(gridsize + 1):
        gridstr = ''
        for gridx in range(gridsize + 1):
            if locationX == gridx and locationY == gridy:
                gridstr += 'x'
            else:
                gridstr += ' '
            if gridx < gridsize:
                gridstr += '-'
        print(gridstr)
        if gridy < gridsize:
            gridstr = ''
            for printgridy in range(gridsize + 1):
                gridstr += '|'
                gridstr += ' '
            print(gridstr)
    print('choices so far:', choices, '\n')
            

def pathFinderX(locationX, locationY):
    global choices
    if atTheEdge(locationX):
        choices += 1
        print('edge hit right: x', locationX, 'y', locationY)
        showLocaiton(locationX, locationY)
        pathFinderY(locationX, locationY)
        return
    else:
        locationX += 1
        print('going right: x', locationX, 'y', locationY)
        showLocaiton(locationX, locationY)
        pathFinderX(locationX, locationY)
        

def pathFinderY(locationX, locationY):
    global choices
    if atTheEdge(locationY):
        choices += 1
        print('edge hit down: x', locationX, 'y', locationY)
        showLocaiton(locationX, locationY)
        return
    else:
        locationY += 1
        print('going down: x', locationX, 'y', locationY)
        showLocaiton(locationX, locationY)
        pathFinderX(locationX, locationY)
        pathFinderY(locationX, locationY)

def atTheEdge(location):
    global gridsize
    if location == gridsize:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
