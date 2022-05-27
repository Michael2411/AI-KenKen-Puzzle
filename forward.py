import operator
from itertools import product, permutations
from functools import reduce
import numpy as np
from Generate import generate


class kenken_forward:
    def __init__(self): 
        self.operator_dict = {"+": operator.add,
                 "-": operator.sub,
                 "*": operator.mul,
                 "/": operator.truediv}
                 
    def calculate(self,numbers, target, op):
        operation = self.operator_dict[op]
        total = reduce(operation, numbers)
        return total == target

    # check the domain of valid numbers for each cell before inserting a number in it
    def valid_number(self,row, column, grid, size):
        valid_numbers = set(range(1, size+1))
        for i in range(0, size):
            valid_numbers.discard(grid[row, i])
            valid_numbers.discard(grid[i, column])
        yield from valid_numbers


    def cage_calc(self,grid, cages, cage_number):
        cage = list(cages.items())[cage_number]
        target = cage[1][0]
        operation = cage[1][1]
        if operation == '=':
            return True
        cells = cage[1][2]
        list_numbers = []
        for r, c in cells:
            list_numbers.append(grid[r, c])
        if(operation == '-' or operation == '/'):
            list_numbers.sort(reverse=True)
        if self.calculate(list_numbers, target, operation):
            return True          # the beak skips over the else
        else:
            return False           # this is done if the loop finishes normal


    def grid_full(self,grid, size):
        for row in range(size):
            for column in range(size):
                if grid[row, column] == 0:
                    return False
        return True


    def cage_full(self,grid, cages, cage_number):
        cage = list(cages.items())[cage_number]
        cells = cage[1][2]
        list_numbers = []
        for r, c in cells:
            if grid[r, c] == 0:
                return False
        return True


    def cage_check(self,grid, cages, number_cages):
        for k in range(number_cages):
            if self.cage_full(grid, cages, k):
                if self.cage_calc(grid, cages, k):
                    continue
                return False
        return True


    def solve_kenken(self,grid, cage_constraints, size, number_cages, cages):
        if self.grid_full(grid, size):
            # if is_valid_sum(grid, cages):
            return True, grid
        # return False, grid
        for i, j in product([row for row in range(size)],
                            [column for column in range(size)]):  # Product is from itertools library
            if grid[i, j] != 0:
                continue
            for number in self.valid_number(i, j, grid, size):
                grid[i, j] = number
                if(not self.cage_check(grid, cages, number_cages)):
                    grid[i, j] = 0
                    continue
                is_solved, grid = self.solve_kenken(
                    grid, cage_constraints, size, number_cages, cages)
                if is_solved:
                    return True, grid
                grid[i, j] = 0
            return False, grid
        return False, grid


    def fill_most_constrained(self,grid, cage_constraints, size):
        for row in range(size):
            for column in range(size):
                if cage_constraints[row][column][2] == '=':
                    grid[row, column] = cage_constraints[row][column][1]
        return grid


    def make_cages(self,cage_constraints,size):
        cages = {}
        for r in range(0, size):
            for c in range(0, size):
                cage_number, target, op = cage_constraints[r][c]
                if op:
                    if cage_number not in cages:
                        cages[cage_number] = [target, op, []]
                    cages[cage_number][2].append((r, c))
        return cages

    def forward_checking(self,grid):
        cage_constraints = grid
        size = len(cage_constraints[0])

        number_cages = 0
        for row in range(size):
            for column in range(size):
                if(cage_constraints[row][column][0] > number_cages):
                    number_cages = cage_constraints[row][column][0]

        cages = self.make_cages(cage_constraints,size)
        grid = np.zeros(size * size).reshape(size, size)
        grid = self.fill_most_constrained(grid, cage_constraints, size)
        is_solved, solved = self.solve_kenken(
            grid, cage_constraints, size, number_cages, cages)
        if is_solved:
            solved=solved.astype(int)
            return(solved)
        else:
            solved = []
            return solved

game = kenken_forward()
grid, notGrid=generate(8)
result=game.forward_checking(grid)
print(result)
# grid= generate(7)
# solved=forward_checking(grid)
# print(solved)
'''
    cage_constraints = [
    [[1, 2, '/'], [1, 2, '/'], [2, 5, '-'], [3, 3, '='], [4, 5, '='], [5, 6, '='], [6, 4, '-'], [7, 18, '+'], [7, 18, '+']],
    [[8, 270, '*'], [8, 270, '*'], [2, 5, '-'], [9, 23, '+'], [9, 23, '+'], [10, 4, '-'], [6, 4, '-'], [11, 19, '+'], [7, 18, '+']], 
    [[8, 270, '*'], [8, 270, '*'], [12, 21, '+'], [13, 11, '+'], [9, 23, '+'], [10, 4, '-'], [14, 378, '*'], [11, 19, '+'], [15, 6, '=']], 
    [[16, 9, '='], [12, 21, '+'], [12, 21, '+'], [13, 11, '+'], [9, 23, '+'], [17, 4, '='], [14, 378, '*'], [11, 19, '+'], [18, 12, '+']], 
    [[19, 17, '+'], [19, 17, '+'], [20, 12, '+'], [13, 11, '+'], [21, 1, '-'], [21, 1, '-'], [14, 378, '*'], [22, 5, '='], [18, 12, '+']], 
    [[23, 18, '+'], [19, 17, '+'], [20, 12, '+'], [20, 12, '+'], [24, 720, '*'], [25, 1134, '*'], [14, 378, '*'], [18, 12, '+'], [18, 12, '+']], 
    [[23, 18, '+'], [26, 7, '='], [24, 720, '*'], [24, 720, '*'], [24, 720, '*'], [25, 1134, '*'], [27, 11, '+'], [27, 11, '+'], [27, 11, '+']], 
    [[23, 18, '+'], [23, 18, '+'], [28, 315, '*'], [29, 4, '='], [25, 1134, '*'], [25, 1134, '*'], [30, 14, '+'], [30, 14, '+'], [30, 14, '+']], 
    [[31, 1, '-'], [31, 1, '-'], [28, 315, '*'], [28, 315, '*'], [28, 315, '*'], [32, 8, '='], [33, 108, '*'], [33, 108, '*'], [33, 108, '*']]]

    cage_constraints =[
    [[1, 6, '*'], [2, 3, '='], [3, 6, '*']], 
    [[1, 6, '*'], [1, 6, '*'], [3, 6, '*']], 
    [[4, 2, '='], [1, 6, '*'], [3, 6, '*']]
    ]
'''
    
