from random import seed, random, shuffle, randint, choice
from functools import reduce


def operation(operator):
    """
    A utility function used in order to determine the operation corresponding
    to the operator that is given in string format
    """
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '-':
        return lambda a, b: a - b
    elif operator == '*':
        return lambda a, b: a * b
    elif operator == '/':
        return lambda a, b: a / b
    else:
        return None


def adjacent(xy1, xy2):
    """
    Checks wheither two positions represented in 2D coordinates are adjacent
    """
    x1, y1 = xy1
    x2, y2 = xy2

    dx, dy = x1 - x2, y1 - y2

    return (dx == 0 and abs(dy) == 1) or (dy == 0 and abs(dx) == 1)


def generate(size):
    board = [[((i + j) % size) + 1 for i in range(size)] for j in range(size)]
    # Fill the board with number 1 to size
    for _ in range(size):
        shuffle(board)
        # shuffle the board to randomize

    for c1 in range(size):
        for c2 in range(size):
            if random() > 0.5:
                for r in range(size):
                    board[r][c1], board[r][c2] = board[r][c2], board[r][c1]
    # random the board cells with each other

    board = {(j + 1, i + 1): board[i][j] for i in range(size)
             for j in range(size)}  # LOCATION WITH VALUES
    # Save in board loaction and vakue

    # print(board)

    uncaged = sorted(board.keys())  # LOCATIONS
    # print(uncaged)

    cages = []
    while uncaged:
        cages.append([])
        csize = randint(1, 4)  # cages size kol cage kam cell
        cell = uncaged[0]  # root
        uncaged.remove(cell)
        cages[-1].append(cell)  # 9 locations [8 uncaged 1 caged ] each time
        #print("uncaged", uncaged)
        #print("cages", cages)
        #print("csize", csize)
        #adjs = []
        # This for loop to get cage cells and remove it from uncaged
        for _ in range(csize - 1):
            # for other in uncaged:
            #    if adjacent(cell, other):
            #        adjs.append([other])

            adjs = [other for other in uncaged if adjacent(cell, other)]
            # get the adjcent cells for detected cell now
            #print("adj", adjs)
            # print(adjs)
            cell = choice(adjs) if adjs else None  # choose one of adj
            if not cell:
                break
            #print("chosen cell", cell)
            uncaged.remove(cell)  # remove it from uncaged
            cages[-1].append(cell)  # and add it in to cages

        # get operation
        csize = len(cages[-1])
        if csize == 1:
            cell = cages[-1][0]
            cages[-1] = [[cell], '=', board[cell]]
            #print("call size 1", cell)
            #print("last element in cages", cages[-1])
            continue

        elif csize == 2:
            fst, snd = cages[-1][0], cages[-1][1]
            if board[fst] / board[snd] > 0 and not board[fst] % board[snd]:
                operator = "/"  # choice("+-*/")
            else:
                operator = "-"  # choice("+-*")
        else:
            operator = choice("+*")

        #print("operation output", operation(operator))
        # reduce take function and apply to all list [sec argument] Make The operation in to all elements in the cage
        target = reduce(operation(operator), [
                        board[cell] for cell in cages[-1]])
        # save locations of cells AND OP AND TARGET
        cages[-1] = [(cages[-1]), operator, int(abs(target))]
#print("Mizo cages", cages)

    koko_cages = []
    for i in range(1, size+1):
        cages_row = []
        for j in range(1, size+1):
            cell = (i, j)
            for k in range(0, len(cages)):
                for l in range(0, len(cages[k][0])):
                    if(cages[k][0][l] == cell):
                        #print("box", k+1)
                        # save number of cage , target , op
                        cell_type = [k+1, cages[k][2], cages[k][1]]
                        cages_row.append(cell_type)
                        break
        koko_cages.append(cages_row)

    return koko_cages


#cages, koko = generate(3)
#print("cages", cages)
#print("koko cages", koko)
# print(cell)

# return size, cages
