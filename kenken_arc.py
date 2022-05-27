import re
import sys

import trail2


class KenKen():
    
    def __init__(self, size, mylist):

        self.variables = list()
        self.neighbors = dict()
        self.blockVar = list()
        self.blockOp = list()
        self.blockValue = list()
        self.blockVariables = list()
        
        
        """Create variables list"""
        for i in range(size):
            for j in range(size):
                self.variables.append('K' + str(i) + str(j))
    
        """Create domains dictionary"""
        dictDomainsValues = list(range(1, size+1))
        self.domains = dict((v, dictDomainsValues) for v in self.variables)
    
        """Create neighbors dictionary"""
        for v in self.variables:
            dictNeighborValue = []
            coordinateX = int(list(v)[1])
            coordinateY = int(list(v)[2])
    
            for i in range(size):
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
            var=l[0]
            op=l[1]
            val=l[2]
            
            self.blockVar.append(var)
            self.blockOp.append(op)
            self.blockValue.append(int(val))
           
       
        # print(self.blockOp)
        # print(self.blockValue)   
        # print(self.blockVar)
        for i in range(len(self.blockVar)):
            blockList = []
            for j in range(0, len(self.blockVar[i])):
                mystring=str(self.blockVar[i][j])
                myvar=len(mystring)
                mystring=mystring[1:myvar-1]
                newstring=mystring.replace(', ','')
                string = 'K' + newstring 
                # print(string)
                blockList.append(string)
    
            self.blockVariables.append(blockList)
            print(self.blockVariables)                

   

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
    
    
    def display(self, dic, size):
        for i in range(size):
            for j in range(size):
                string = 'K' + str(i) + str(j)
                sys.stdout.write(str(dic[string]) + " ")
            print()
	

if __name__ == '__main__':
    
    """Read first line from file"""
    with open('kenken.txt', 'r') as f:
        size = int(f.readline())
        lines = f.readlines()[1:]
        print(size)

    f.close()


    kenken = KenKen(size, [[[(0,0),(1,0)], '+', 6],
     [[(0,1),(0,2)], '+', 5],
      [[(1,1),(1,2)], '*', 3],
       [[(0,3),(1,3)], '-', 1],
       [[(0,4),(1,4)], '/' ,2],
       [[(2,0),(2,1)] ,'-' ,1],
       [[(2,2),(3,1),(3,2)] ,'*' ,20],
       [[(2,3),(3,3)] ,'-', 1],
       [[(2,4),(3,4)], '-' ,2],
       [[(3,0),(4,0)] ,'+', 5],
       [[(4,1),(4,2)] ,'/' ,2],
       [[(4,3),(4,4)] ,'*', 5]])

    game_kenken = trail2.CSP(kenken.variables, kenken.domains, kenken.neighbors, kenken.kenken_constraint)
    x=trail2.AC3(game_kenken)
    print(game_kenken.curr_domains)
    mydomain=[]
    myListDomain=[]

    for i in range(0,size):
        mydomain=[]
        for j in range(0,size):
          mydomain.append(game_kenken.curr_domains['K'+str(i)+str(j)])
        myListDomain.append(mydomain)  
         
    print(myListDomain)
    # kenken.display(trail2.CSP.backtracking_search(game_kenken, inference=trail2.CSP.mac), size)
    