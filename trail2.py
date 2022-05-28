class CSP():


    def __init__(self, variables, domains, neighbors, constraints):
        "Construct a CSP problem. If variables is empty, it becomes domains.keys()."
        variables = variables or list(domains.keys())

        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0

    

    def support_pruning(self):
        """Make sure we can prune values from domains. (We want to pay
        for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    # def suppose(self, var, value):
    #     "Start accumulating inferences from assuming var=value."
    #     self.support_pruning()
    #     removals = [(var, a) for a in self.curr_domains[var] if a != value]
    #     self.curr_domains[var] = [value]
    #     return removals

    def prune(self, var, value, removals):
        "Rule out var=value."
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def choices(self, var):
        "Return all values for var that aren't currently ruled out."
        return (self.curr_domains or self.domains)[var]

    def infer_assignment(self):
        "Return the partial assignment implied by the current inferences."
        self.support_pruning()
        return {v: self.curr_domains[v][0]
                for v in self.variables if 1 == len(self.curr_domains[v])}


    
# ______________________________________________________________________________
# Constraint Propagation with AC-3

class ArcConsistency():
    def AC3(self,csp, queue=None, removals=None):
            """[Figure 6.3]"""
            if queue is None:
                queue = [(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]]
            csp.support_pruning()
            while queue:
                (Xi, Xj) = queue.pop()
                if self.revise(csp, Xi, Xj, removals):
                    if not csp.curr_domains[Xi]:
                        return False
                    for Xk in csp.neighbors[Xi]:
                        if Xk != Xi:
                            queue.append((Xk, Xi))
            return True

    def revise(self,csp, Xi, Xj, removals):
            "Return true if we remove a value."
            revised = False
            for x in csp.curr_domains[Xi][:]:
                # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
                if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
                    csp.prune(Xi, x, removals)
                    revised = True
            return revised   


    