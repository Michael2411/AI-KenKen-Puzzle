from random import seed, random, shuffle, randint, choice
from functools import reduce


class kenken_generate:
    def __init__(self):
        self.cages = []  # CAGES GENERATED
        self.board = []  # BOARD GENERATED

    def operation(self, operator):
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

    def adjacent(self, xy1, xy2):
        """
        Checks wheither two positions represented in 2D coordinates are adjacent
        """
        x1, y1 = xy1
        x2, y2 = xy2

        dx, dy = x1 - x2, y1 - y2

        return (dx == 0 and abs(dy) == 1) or (dy == 0 and abs(dx) == 1)

    def generate(self, size):
        self.board = [[((i + j) % size) + 1 for i in range(size)]
                      for j in range(size)]
        # Fill the board with number 1 to size
        for _ in range(size):
            shuffle(self.board)
            # shuffle the board to randomize

        for c1 in range(size):
            for c2 in range(size):
                if random() > 0.5:
                    for r in range(size):
                        self.board[r][c1], self.board[r][c2] = self.board[r][c2], self.board[r][c1]
        # random the board cells with each other

        self.board = {(j + 1, i + 1): self.board[i][j] for i in range(size)
                      for j in range(size)}  # LOCATION WITH VALUES
        # Save in board loaction and vakue

        # print(board)

        uncaged = sorted(self.board.keys())  # LOCATIONS
        # print(uncaged)

        #cages = []
        while uncaged:
            self.cages.append([])
            csize = randint(1, 4)  # cages size kol cage kam cell
            cell = uncaged[0]  # root
            uncaged.remove(cell)
            # 9 locations [8 uncaged 1 caged ] each time
            self.cages[-1].append(cell)
            #print("uncaged", uncaged)
            #print("cages", cages)
            #print("csize", csize)
            #adjs = []
            # This for loop to get cage cells and remove it from uncaged
            for _ in range(csize - 1):
                # for other in uncaged:
                #    if adjacent(cell, other):
                #        adjs.append([other])

                adjs = [
                    other for other in uncaged if self.adjacent(cell, other)]
                # get the adjcent cells for detected cell now
                #print("adj", adjs)
                # print(adjs)
                cell = choice(adjs) if adjs else None  # choose one of adj
                if not cell:
                    break
                #print("chosen cell", cell)
                uncaged.remove(cell)  # remove it from uncaged
                self.cages[-1].append(cell)  # and add it in to cages

            # get operation
            csize = len(self.cages[-1])
            if csize == 1:
                cell = self.cages[-1][0]
                self.cages[-1] = [[cell], '=', self.board[cell]]
                #print("call size 1", cell)
                #print("last element in cages", cages[-1])
                continue

            elif csize == 2:
                fst, snd = self.cages[-1][0], self.cages[-1][1]
                if self.board[fst] / self.board[snd] > 0 and not self.board[fst] % self.board[snd]:
                    operator = "/"  # choice("+-*/")
                else:
                    operator = "-"  # choice("+-*")
            else:
                operator = choice("+*")

            #print("operation output", operation(operator))
            # reduce take function and apply to all list [sec argument] Make The operation in to all elements in the cage
            target = reduce(self.operation(operator), [
                            self.board[cell] for cell in self.cages[-1]])
            # save locations of cells AND OP AND TARGET
            self.cages[-1] = [(self.cages[-1]), operator, int(abs(target))]
#print("Mizo cages", cages)

        return_cages = []
        for i in range(1, size+1):
            cages_row = []
            for j in range(1, size+1):
                cell = (i, j)
                for k in range(0, len(self.cages)):
                    for l in range(0, len(self.cages[k][0])):
                        if(self.cages[k][0][l] == cell):
                            #print("box", k+1)
                            # save number of cage , target , op
                            cell_type = [k+1, self.cages[k]
                                         [2], self.cages[k][1]]
                            cages_row.append(cell_type)
                            break
            return_cages.append(cages_row)

        return return_cages, self.cages


# kenkengenerate = kenken_generate()  # instance
#cages, ziko, board = kenkengenerate.generate(3)
#print("cages", ziko)
#print("board", board)
# if __name__ == "__main__":
#    cages, ziko = generate(3)
#    print("cages", cages)
#    print("ziko", ziko)
# print(cell)

# return size, cages
