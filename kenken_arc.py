import re
import sys

import trail2
import operator
from itertools import product, permutations
from functools import reduce
import numpy as np
#from Generate import generate




class KenKen():

    def __init__(self, size, mylist):

        self.variables = list()
        self.neighbors = dict()
        self.blockVar = list()
        self.blockOp = list()
        self.blockValue = list()
        self.blockVariables = list()

        """Create variables list"""
        for i in range(1, size+1):
            for j in range(1, size+1):
                self.variables.append('K' + str(i) + str(j))

        """Create domains dictionary"""
        dictDomainsValues = list(range(1, size+1))
        self.domains = dict((v, dictDomainsValues) for v in self.variables)

        """Create neighbors dictionary"""
        for v in self.variables:
            dictNeighborValue = []
            coordinateX = int(list(v)[1])
            coordinateY = int(list(v)[2])

            for i in range(1, size+1):
                if i != coordinateY:
                    string = 'K' + str(coordinateX) + str(i)
                    dictNeighborValue.append(string)
                if i != coordinateX:
                    string = 'K' + str(i) + str(coordinateY)
                    dictNeighborValue.append(string)

            self.neighbors[v] = dictNeighborValue

        """Create constraint data lists"""
        for l in mylist:
            # var, op, val = l.split()

            # self.blockVar.append(re.findall('\d+', var))
            # self.blockOp.append(op)
            # self.blockValue.append(int(val))

            # var, op, val = l.split()
            var = l[0]
            op = l[1]
            val = l[2]

            self.blockVar.append(var)
            self.blockOp.append(op)
            self.blockValue.append(int(val))

        # print(self.blockOp)
        # print(self.blockValue)
        # print(self.blockVar)
        for i in range(len(self.blockVar)):
            blockList = []
            for j in range(0, len(self.blockVar[i])):
                mystring = str(self.blockVar[i][j])
                myvar = len(mystring)
                mystring = mystring[1:myvar-1]
                newstring = mystring.replace(', ', '')
                string = 'K' + newstring
                # print(string)
                blockList.append(string)

            self.blockVariables.append(blockList)
            # print(self.blockVariables)

    def kenken_constraint(self, A, a, B, b):
        if B in self.neighbors[A] and a == b:
            return False

        for n in self.neighbors[A]:
            if n in game_kenken.infer_assignment() and game_kenken.infer_assignment()[n] == a:
                return False

        for n in self.neighbors[B]:
            if n in game_kenken.infer_assignment() and game_kenken.infer_assignment()[n] == b:
                return False

        blockA = blockB = 0

        for i in range(len(self.blockVariables)):
            if A in self.blockVariables[i]:
                blockA = i
            if B in self.blockVariables[i]:
                blockB = i

        if blockA == blockB:
            blockNum = blockA
            if self.blockOp[blockNum] == "=":
                if A != B:
                    return False
                elif a != b:
                    return False
                elif a != self.blockValue[blockNum]:
                    return False

                return True

            elif self.blockOp[blockNum] == '+':
                sum = assigned = 0

                for v in self.blockVariables[blockNum]:
                    if v == A:
                        sum += a
                        assigned += 1
                    elif v == B:
                        sum += b
                        assigned += 1
                    elif v in game_kenken.infer_assignment():
                        sum += game_kenken.infer_assignment()[v]
                        assigned += 1

                if sum == self.blockValue[blockNum] and assigned == len(self.blockVariables[blockNum]):
                    return True
                elif sum < self.blockValue[blockNum] and assigned < len(self.blockVariables[blockNum]):
                    return True
                else:
                    return False

            elif self.blockOp[blockNum] == '*':
                sum = 1
                assigned = 0

                for v in self.blockVariables[blockNum]:
                    if v == A:
                        sum *= a
                        assigned += 1
                    elif v == B:
                        sum *= b
                        assigned += 1
                    elif v in game_kenken.infer_assignment():
                        sum *= game_kenken.infer_assignment()[v]
                        assigned += 1

                if sum == self.blockValue[blockNum] and assigned == len(self.blockVariables[blockNum]):
                    return True
                elif sum <= self.blockValue[blockNum] and assigned < len(self.blockVariables[blockNum]):
                    return True
                else:
                    return False

            elif self.blockOp[blockNum] == '/':
                return max(a, b) / min(a, b) == self.blockValue[blockNum]

            elif self.blockOp[blockNum] == '-':
                return max(a, b) - min(a, b) == self.blockValue[blockNum]

        else:
            constraintA = self.kenken_constraint_op(A, a, blockA)
            constraintB = self.kenken_constraint_op(B, b, blockB)

            return constraintA and constraintB

    def kenken_constraint_op(self, var, val, blockNum):
        if self.blockOp[blockNum] == "=":
            return val == self.blockValue[blockNum]

        elif self.blockOp[blockNum] == '+':
            sum2 = 0
            assigned2 = 0

            for v in self.blockVariables[blockNum]:
                if v == var:
                    sum2 += val
                    assigned2 += 1
                elif v in game_kenken.infer_assignment():
                    sum2 += game_kenken.infer_assignment()[v]
                    assigned2 += 1

            if sum2 == self.blockValue[blockNum] and assigned2 == len(self.blockVariables[blockNum]):
                return True
            elif sum2 < self.blockValue[blockNum] and assigned2 < len(self.blockVariables[blockNum]):
                return True
            else:
                return False

        elif self.blockOp[blockNum] == '*':
            sum2 = 1
            assigned2 = 0

            for v in self.blockVariables[blockNum]:
                if v == var:
                    sum2 *= val
                    assigned2 += 1
                elif v in game_kenken.infer_assignment():
                    sum2 *= game_kenken.infer_assignment()[v]
                    assigned2 += 1

            if sum2 == self.blockValue[blockNum] and assigned2 == len(self.blockVariables[blockNum]):
                return True
            elif sum2 <= self.blockValue[blockNum] and assigned2 < len(self.blockVariables[blockNum]):
                return True
            else:
                return False

        elif self.blockOp[blockNum] == '/':
            for v in self.blockVariables[blockNum]:
                if v != var:
                    constraintVar2 = v

            if constraintVar2 in game_kenken.infer_assignment():
                constraintVal2 = game_kenken.infer_assignment()[constraintVar2]
                return max(constraintVal2, val) / min(constraintVal2, val) == self.blockValue[blockNum]
            else:
                for d in game_kenken.choices(constraintVar2):
                    if max(d, val) / min(d, val) == self.blockValue[blockNum]:
                        return True

                return False

        elif self.blockOp[blockNum] == '-':
            for v in self.blockVariables[blockNum]:
                if v != var:
                    constraintVar2 = v

            if constraintVar2 in game_kenken.infer_assignment():
                constraintVal2 = game_kenken.infer_assignment()[constraintVar2]
                return max(constraintVal2, val) - min(constraintVal2, val) == self.blockValue[blockNum]
            else:
                for d in game_kenken.choices(constraintVar2):
                    if max(d, val) - min(d, val) == self.blockValue[blockNum]:
                        return True

                return False

    # def display(self, dic, size):
    #     for i in range(size):
    #         for j in range(size):
    #             string = 'K' + str(i) + str(j)
    #             sys.stdout.write(str(dic[string]) + " ")
    #         print()



# if __name__ == '__main__':
class InitializeArc():

   

    def getCorrectValues(self,size,grid,arc):
        global kenken
        kenken = KenKen(size, arc)
        global game_kenken
        game_kenken =trail2.CSP(
            kenken.variables, kenken.domains, kenken.neighbors, kenken.kenken_constraint)
        x = trail2.ArcConsistency.AC3(game_kenken)
        global arc_array
        mydomain = []
        myListDomain = []
        if(x):
            for i in range(1, size+1):
                mydomain = []
                for j in range(1, size+1):
                    mydomain.append(game_kenken.curr_domains['K'+str(i)+str(j)])
                myListDomain.append(mydomain)
        arc_array = myListDomain

        # print(grid)
        # print("arc_array:",arc_array)
        # print(arc_array[0][1])
        solved_arc = self.forward_checking(grid)
        return solved_arc
        
        # print(solved_arc)
        # kenken.display(trail2.CSP.backtracking_search(game_kenken, inference=trail2.CSP.mac), size)



    def calculate(self,numbers, target, op):
        operation =self.operator_dict[op]
        total = reduce(operation, numbers)
        return total == target

    # check the domain of valid numbers for each cell before inserting a number in it


    # def valid_number(row, column, grid, size):
    #     valid_numbers = set(range(1, size+1))
    #     for i in range(0, size):
    #         valid_numbers.discard(grid[row, i])
    #         valid_numbers.discard(grid[i, column])
    #     yield from valid_numbers

    def valid_number(n, m):
        valid_numbers = arc_array[n][m]
        return valid_numbers


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


    def grid_full(grid, size):
        for row in range(size):
            for column in range(size):
                if grid[row, column] == 0:
                    return False
        return True


    def cage_full(grid, cages, cage_number):
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


    def check_number(grid, i, j, size):
        for k in range(0, size):
            if ((grid[i, j] == grid[k, j]) & (k != i)):
                return 1
            if ((grid[i, j] == grid[i, k]) & (k != j)):
                return 1
            # return True


    def solve_kenken(self,grid, cage_constraints, size, number_cages, cages):
        if self.grid_full(grid, size):
            # if is_valid_sum(grid, cages):
            return True, grid
        # return False, grid
        for i, j in product([row for row in range(size)],
                            [column for column in range(size)]):  # Product is from itertools library
            if grid[i, j] != 0:
                continue
            for number in self.valid_number(i, j):
                grid[i, j] = number
                ################
                number_not_valid = self.check_number(grid, i, j, size)
                if(number_not_valid):
                    grid[i, j] = 0
                    continue
                ################
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


    def fill_most_constrained(grid, cage_constraints, size):
        for row in range(size):
            for column in range(size):
                if cage_constraints[row][column][2] == '=':
                    grid[row, column] = cage_constraints[row][column][1]
        return grid


    def make_cages(cage_constraints, size):
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

        cages = self.make_cages(cage_constraints, size)
        grid = np.zeros(size * size).reshape(size, size)
        grid = self.fill_most_constrained(grid, cage_constraints, size)
        is_solved, solved = self.solve_kenken(
            grid, cage_constraints, size, number_cages, cages)
        if is_solved:
            solved = solved.astype(int)
            return(solved)
        else:
            solved = []
            return solved

    operator_dict = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv}
   
                 

if __name__ == '__main__':

        gamme=InitializeArc()
