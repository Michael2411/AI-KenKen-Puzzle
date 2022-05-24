import operator
from itertools import product
import numpy as np
from Generate import generate

def calculate(numbers, target, op):
    operator_dict = {"+": operator.add,
                     "-": operator.sub,
                     "*": operator.mul,
                     "/": operator.truediv}

    running_total = numbers[0]
    for number in numbers[1:]:
        running_total = operator_dict[op](running_total, number)

    if running_total == target:
        return True
    return False


def cage_calc(grid,groups,cage_number):
        group = list(groups.items())[cage_number]
        target =group[1][0]
        operation = group[1][1]
        if operation=='=':
            return True
        cells = group[1][2]
        list_numbers=[]
        for r,c in cells:
            list_numbers.append(grid[r,c])
        if(operation=='-' or operation=='/'):
            list_numbers.sort(reverse=True)
        if calculate(list_numbers, target, operation):
            return True          # the beak skips over the else
        else:
            return False           # this is done if the loop finishes normal

def grid_full(grid, size):
    for row in range(size):
        for column in range(size):
            if grid[row, column] == 0:
                return False
    return True

def check_number(grid,i,j):
    for k in range(0, size ):
        if ((grid[i,j]== grid[k,j])&(k !=i)) :
            return 1
        if ((grid[i,j]== grid[i,k])&(k!=j)):
            return 1
        #return True

def cage_full(grid,groups,cage_number):
        group = list(groups.items())[cage_number]
        cells = group[1][2]
        list_numbers=[]
        for r,c in cells:
            if grid[r,c]==0:
                return False
        return True

def cage_check(grid,groups,number_groups):
    for k in range(number_groups):
        if cage_full(grid, groups,k):
            if cage_calc(grid, groups,k):
                continue
            return False
    return True

def solve_kenken(grid, instruction_array, size, number_groups, domain):
    if grid_full(grid, size):     
            return True, grid
    for i, j in product([row for row in range(size)],
                        [column for column in range(size)]):  # Product is from itertools library
        if grid[i, j] != 0:
            continue
        for number in  domain:
            grid[i, j] = number
            ################
            number_not_valid = check_number(grid, i, j)
            if(number_not_valid):
                grid[i,j]=0
                continue
            ################
            if(not cage_check(grid, groups, number_groups)):
                grid[i,j]=0
                continue
            is_solved, grid = solve_kenken(grid, instruction_array, size, number_groups, domain)
            if is_solved:
                return True, grid
            grid[i, j] = 0
        return False, grid
    return False, grid


def fill_most_constrained(grid, instruction_array, size):
    # Fill fixed numbers
    for row in range(size):
        for column in range(size):
            if instruction_array[row][column][2] == '=':
                grid[row, column] = instruction_array[row][column][1]
    return grid

def make_groups(instruction_array):
    groups = {}
    for r in range(0, size):
        for c in range(0, size):
            group_number,target,op = instruction_array[r][c]
            if op:
                if group_number not in groups:
                    groups[group_number] = [target, op, []]
                groups[group_number][2].append((r,c))
    return groups

if __name__ == "__main__":
    '''
    instruction_array =[
        [[1, 6, '*'], [2, 3, '='], [3, 6, '*']], 
        [[1, 6, '*'], [1, 6, '*'], [3, 6, '*']], 
        [[4, 2, '='], [1, 6, '*'], [3, 6, '*']]
        ]
    
    instruction_array =[
    [[1, 1, '-'], [2, 18, '*'], [2, 18, '*']], 
    [[1, 1, '-'], [2, 18, '*'], [3, 2, '/']], 
    [[4, 3, '/'], [4, 3, '/'], [3, 2, '/']]
    ]
    '''
    cages, instruction_array = generate(3)
    size = len(instruction_array[0])
    number_groups=0
    for row in range(size):
        for column in range(size):
            if(instruction_array[row][column][0]> number_groups):
                number_groups=instruction_array[row][column][0]

    #store cages 
    groups = make_groups(instruction_array)
    #get the domain of numbers for the grid [1....n]
    domain=[]
    for i in range(1,size+1):
         domain.append(i)
    #initiate grid
    grid = np.zeros(size * size).reshape(size, size)
    #most constrained variable heuristic 
    grid = fill_most_constrained(grid, instruction_array, size)
    is_solved, solved = solve_kenken(grid, instruction_array, size, number_groups, domain)
    if is_solved:
        print(solved)
    else:
        print("Cannot solve")