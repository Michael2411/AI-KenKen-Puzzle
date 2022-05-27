import operator
from itertools import product
import numpy as np
from functools import reduce
from Generate import generate

class kenken_backtracking:
    def __init__(self): 
        self.operator_dict = {"+": operator.add,
                 "-": operator.sub,
                 "*": operator.mul,
                 "/": operator.truediv}

    def calculate(self,numbers, target, op):
        running_total = numbers[0]
        for number in numbers[1:]:
            running_total = self.operator_dict[op](running_total, number)
        if running_total == target:
            return True
        return False


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


    def check_number(self,grid, i, j,size):
        for k in range(0, size):
            if ((grid[i, j] == grid[k, j]) & (k != i)):
                return 1
            if ((grid[i, j] == grid[i, k]) & (k != j)):
                return 1
            # return True


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


    def solve_kenken(self,grid, cage_constraints, size, number_cages, domain,cages):
        if self.grid_full(grid, size):
            return True, grid
        for i, j in product([row for row in range(size)],
                            [column for column in range(size)]):  # Product is from itertools library
            if grid[i, j] != 0:
                continue
            for number in domain:
                grid[i, j] = number
                ################
                number_not_valid = self.check_number(grid, i, j,size)
                if(number_not_valid):
                    grid[i, j] = 0
                    continue
                ################
                if(not self.cage_check(grid, cages, number_cages)):
                    grid[i, j] = 0
                    continue
                is_solved, grid = self.solve_kenken(
                    grid, cage_constraints, size, number_cages, domain,cages)
                if is_solved:
                    return True, grid
                grid[i, j] = 0
            return False, grid
        return False, grid


    def fill_most_constrained(self,grid, cage_constraints, size):
        # Fill fixed numbers
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

    def backtracking(self,grid):
        cage_constraints = grid
        size = len(cage_constraints[0])
        number_cages = 0
        for row in range(size):
            for column in range(size):
                if(cage_constraints[row][column][0] > number_cages):
                    number_cages = cage_constraints[row][column][0]

        # store cages
        cages = self.make_cages(cage_constraints,size)
        # get the domain of numbers for the grid [1....n]
        domain = []
        for i in range(1, size+1):
            domain.append(i)
        # initiate grid
        grid = np.zeros(size * size).reshape(size, size)
        # most constrained variable heuristic
        grid = self.fill_most_constrained(grid, cage_constraints, size)
        is_solved, solved = self.solve_kenken(
            grid, cage_constraints, size, number_cages, domain,cages)
        if is_solved:
            solved=solved.astype(int)
            return solved
        else:
            solved = []
            return solved

game = kenken_backtracking()
grid, notGrid=generate(6)
result=game.backtracking(grid)
print(result)
# grid= generate(6)
# solved=backtracking(grid)
# print(solved)
'''
    cage_constraints =[
        [[1, 6, '*'], [2, 3, '='], [3, 6, '*']], 
        [[1, 6, '*'], [1, 6, '*'], [3, 6, '*']], 
        [[4, 2, '='], [1, 6, '*'], [3, 6, '*']]
        ]

    cage_constraints =[
    [[1, 1, '-'], [2, 18, '*'], [2, 18, '*']], 
    [[1, 1, '-'], [2, 18, '*'], [3, 2, '/']], 
    [[4, 3, '/'], [4, 3, '/'], [3, 2, '/']]
    ]
'''
    
