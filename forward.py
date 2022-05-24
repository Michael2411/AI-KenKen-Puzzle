import operator
from itertools import product, permutations
from functools import reduce
import numpy as np

operator_dict = {"+": operator.add,
                     "-": operator.sub,
                     "*": operator.mul,
                     "/": operator.truediv}
def calculate(numbers, target, op):
    
    operation = operator_dict[op]

    total = reduce(operation, numbers)

    return total == target

#check the domain of valid numbers for each cell before inserting a number in it
def valid_number(row, column, board, size):
    valid_numbers = set(range(1,size+1))
    for i in range(0, size):
        valid_numbers.discard(board[row, i])
        valid_numbers.discard(board[i, column])
    yield from valid_numbers

# def is_valid_sum(board, groups):
#     for group in groups.items():
#         target =group[1][0]
#         operation = group[1][1]
#         if operation=='=':
#             continue
#         cells = group[1][2]
#         list_numbers=[]
#         for r,c in cells:
#             list_numbers.append(board[r,c])

#         combination_numbers = permutations(list_numbers, len(list_numbers))
#         for combination in combination_numbers:
#             if calculate(combination, target, operation):
#                 flag =1
#                 break            # the beak skips over the else
#         else:
#             return False           # this is done if the loop finishes normally

#     return True


def cage_calc(board,groups,cage_number):
        group = list(groups.items())[cage_number]
        target =group[1][0]
        operation = group[1][1]
        if operation=='=':
            return True
        cells = group[1][2]
        list_numbers=[]
        for r,c in cells:
            list_numbers.append(board[r,c])
        if(operation=='-' or operation=='/'):
            list_numbers.sort(reverse=True)
        if calculate(list_numbers, target, operation):
            return True          # the beak skips over the else
        else:
            return False           # this is done if the loop finishes normal

def is_full(board, size):
    for row in range(size):
        for column in range(size):
            if board[row, column] == 0:
                return False
    return True

def cage_full(board,groups,cage_number):
        group = list(groups.items())[cage_number]
        cells = group[1][2]
        list_numbers=[]
        for r,c in cells:
            if board[r,c]==0:
                return False
        return True

def cage_check(board,groups,number_groups):
    for k in range(number_groups):
        if cage_full(board, groups,k):
            if cage_calc(board, groups,k):
                continue
            return False
    return True
                
def solve_board(board, instruction_array, size, number_groups,groups):
    if is_full(board, size):
        #if is_valid_sum(board, groups):
        return True, board
       #return False, board
    for i, j in product([row for row in range(size)],
                        [column for column in range(size)]):  # Product is from itertools library
        if board[i, j] != 0:
            continue
        for number in valid_number(i, j, board, size):
            board[i, j] = number
            if(not cage_check(board, groups, number_groups)):
                board[i,j]=0
                continue
            is_solved, board = solve_board(board, instruction_array, size, number_groups,groups)
            if is_solved:
                return True, board
            board[i, j] = 0
        return False, board
    return False, board


def fill_obvious(board, instruction_array, size):
    for row in range(size):
        for column in range(size):
            if instruction_array[row][column][2] == '=':
                board[row, column] = instruction_array[row][column][1]
    return board


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
    instruction_array = [
    [[1, 2, '/'], [1, 2, '/'], [2, 5, '-'], [3, 3, '='], [4, 5, '='], [5, 6, '='], [6, 4, '-'], [7, 18, '+'], [7, 18, '+']],
    [[8, 270, '*'], [8, 270, '*'], [2, 5, '-'], [9, 23, '+'], [9, 23, '+'], [10, 4, '-'], [6, 4, '-'], [11, 19, '+'], [7, 18, '+']], 
    [[8, 270, '*'], [8, 270, '*'], [12, 21, '+'], [13, 11, '+'], [9, 23, '+'], [10, 4, '-'], [14, 378, '*'], [11, 19, '+'], [15, 6, '=']], 
    [[16, 9, '='], [12, 21, '+'], [12, 21, '+'], [13, 11, '+'], [9, 23, '+'], [17, 4, '='], [14, 378, '*'], [11, 19, '+'], [18, 12, '+']], 
    [[19, 17, '+'], [19, 17, '+'], [20, 12, '+'], [13, 11, '+'], [21, 1, '-'], [21, 1, '-'], [14, 378, '*'], [22, 5, '='], [18, 12, '+']], 
    [[23, 18, '+'], [19, 17, '+'], [20, 12, '+'], [20, 12, '+'], [24, 720, '*'], [25, 1134, '*'], [14, 378, '*'], [18, 12, '+'], [18, 12, '+']], 
    [[23, 18, '+'], [26, 7, '='], [24, 720, '*'], [24, 720, '*'], [24, 720, '*'], [25, 1134, '*'], [27, 11, '+'], [27, 11, '+'], [27, 11, '+']], 
    [[23, 18, '+'], [23, 18, '+'], [28, 315, '*'], [29, 4, '='], [25, 1134, '*'], [25, 1134, '*'], [30, 14, '+'], [30, 14, '+'], [30, 14, '+']], 
    [[31, 1, '-'], [31, 1, '-'], [28, 315, '*'], [28, 315, '*'], [28, 315, '*'], [32, 8, '='], [33, 108, '*'], [33, 108, '*'], [33, 108, '*']]]
        
    size = len(instruction_array[0])

    number_groups=0
    for row in range(size):
        for column in range(size):
            if(instruction_array[row][column][0]> number_groups):
                number_groups=instruction_array[row][column][0]
            
    groups = make_groups(instruction_array)
    board = np.zeros(size * size).reshape(size, size)
    board = fill_obvious(board, instruction_array, size)
    is_solved, solved = solve_board(board, instruction_array, size, number_groups,groups)
    if is_solved:
        print(solved)
    else:
        print("Cannot solve")