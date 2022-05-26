

# class csp():

#       def __init__(self, variables, domains, neighbors, constraints):
#         "Construct a CSP problem. If variables is empty, it becomes domains.keys()."
#         # variables = variables or list(domains.keys())

#         self.variables = variables
#         self.domains = domains
#         self.neighbors = neighbors
#         self.constraints = constraints
        
#         self.curr_domains = None

from itertools import combinations, permutations
import operator

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


def cageConstraint(A,variables):
    cages=[]
    validValues=[]
    operation=A['operation']
    target=A['target']
    for v in variables :
       if(v['cage']==A['cage']):
           cages.append(v)
    combinations=permutations(A['domain'],len(cages))
    for comb in combinations:
      myflag=calculate(comb,target,operation)
      if(myflag):
          for i in range (len(cages)):
            validValues.append(comb[i])
    myset=list(set(validValues))
    return myset







def neighborConstraint (A,a,B,b):
    if B in A['neighbors'] and a == b:
         return False
    else:
       return True


def prune( var, value, removals):
        "Rule out var=value."
        var['domain'].remove(value)
        # print (var['domain'])
        if removals is not None:
            removals.append((var, value))

       

def generateNeighbours (variables , size):
 for v in variables:
            dictNeighborValue = []
            coordinateX = int(v['cellNo'][0])
            coordinateY = int(v['cellNo'][1])
    
            for i in range(size):
                if i != coordinateY:
                    string =  str(coordinateX) + str(i)
                    dictNeighborValue.append(string)
                if i != coordinateX:
                    string =  str(i) + str(coordinateY)
                    dictNeighborValue.append(string)
    
            v['neighbors'] = dictNeighborValue
#  return variables
## need to append the value of the neighbours with each cell (variable) and the value of the domain

#### xi is the first map in variables
#### xk is the list of neighbors of first map

def AC3(variables, queue=None, removals=None):
    """[Figure 6.3]"""
    if queue is None:
        queue = [(Xi, Xk) for Xi in variables for Xk in Xi['neighbors']]
        # print(queue)
    # csp.support_pruning()
    while queue:
        (Xi, Xj) = queue.pop()
        if revise( Xi, Xj, removals):
            if not Xi['domain']:
                return False
            for Xk in Xi['neighbors']:
                if Xk != Xi:
                    queue.append((Xk, Xi))
        # print(queue)
    return True


def revise( Xi, Xj, removals):
    "Return true if we remove a value."
    revised = False
    for z in variables :
      if (z['cellNo']==Xj):
          domainArray=z['domain']
          break
        #   print('-----------------------')
        #   print(domainArray)
        
    domain=Xi['domain'].copy()
    print(domain)
    for x in domain:
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        # for y in  domainArray:
        #     non=neighborConstraint(Xi,x,Xj,y)
        #     if(non):
        #         flag=1

        # if(not flag):
        #     prune(Xi, x, removals) 
        #     revised=True    
        if all(not neighborConstraint(Xi, x, Xj, y) for y in  domainArray):

            prune(Xi, x, removals)
            # print(Xi)
        cageValues=cageConstraint(Xi,variables)
        # print(cageValues)
        if(x not in cageValues):
            prune(Xi, x, removals)
            
            revised = True
    return revised


if __name__ == '__main__':
  
    variables=[{'cellNo':'00','neighbors':[],'domain':[1,2,3],'cage':1,'target':12,'operation':'*'},
    {'cellNo':'01','neighbors':[],'domain':[1,2,3],'cage':1,'target':12,'operation':'*'},
    {'cellNo':'02','neighbors':[],'domain':[1,2,3],'cage':2,'target':1,'operation':'='},
    {'cellNo':'10','neighbors':[],'domain':[1,2,3],'cage':1,'target':12,'operation':'*'},
    {'cellNo':'11','neighbors':[],'domain':[1,2,3],'cage':1,'target':12,'operation':'*'},
    {'cellNo':'12','neighbors':[],'domain':[1,2,3],'cage':3,'target':6,'operation':'+'},
    {'cellNo':'20','neighbors':[],'domain':[1,2,3],'cage':4,'target':3,'operation':'='},
    {'cellNo':'21','neighbors':[],'domain':[1,2,3],'cage':3,'target':6,'operation':'+'},
    {'cellNo':'22','neighbors':[],'domain':[1,2,3],'cage':3,'target':6,'operation':'+'},
    ]

    generateNeighbours(variables,3)
    k=AC3(variables)
    # print(variables)
    print(k)