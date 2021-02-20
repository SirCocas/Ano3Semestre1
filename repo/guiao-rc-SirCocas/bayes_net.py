from itertools import product

class BayesNet:

    def __init__(self, ldep=None):  # Why not ldep={}? See footnote 1.
        if not ldep:
            ldep = {}
        self.dependencies = ldep

    # The network data is stored in a dictionary that
    # associates the dependencies to each variable:
    # { v1:deps1, v2:deps2, ... }
    # These dependencies are themselves given
    # by another dictionary that associates conditional
    # probabilities to conjunctions of mother variables:
    # { mothers1:cp1, mothers2:cp2, ... }
    # The conjunctions are frozensets of pairs (mothervar,boolvalue)
    def add(self,var,mothers,prob):
        self.dependencies.setdefault(var,{})[frozenset(mothers)] = prob

    # Joint probability for a given conjunction of
    # all variables of the network
    def jointProb(self,conjunction):
        prob = 1.0
        for (var,val) in conjunction:
            for (mothers,p) in self.dependencies[var].items():
                if mothers.issubset(conjunction):
                    prob*=(p if val else 1-p)
        return prob

    def individualProb(self, item, value):
        conjunctions = self.conjunctions(self.ancestors(item))
        prob = 0.0
        for c in conjunctions:
            prob += self.jointProb(c+[(item, value)])
        return prob


    def ancestors (self, v):
        probs = self.dependencies[v]
        mothers = [m[0] for m in list(probs.keys())[0]]
        lanc = mothers
        for m in mothers:
            lanc+=self.ancestors(m)
        return(list(set(lanc)))
    
    def conjunctions(self, lv):
        var = product([True, False], repeat= len(lv))
        return list(map(lambda c: list(zip(lv, c)), var))

        
# Footnote 1:
# Default arguments are evaluated on function definition,
# not on function evaluation.
# This creates surprising behaviour when the default argument is mutable.
# See:
# http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments

