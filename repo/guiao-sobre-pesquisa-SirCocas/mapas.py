from constraintsearch import *

region = ['A', 'B', 'C', 'D', 'E']
colors = ['red', 'blue', 'green', 'yellow', 'white']


def colorConstraint(r1,c1,r2,c2):
    return c1!= c2


domain = {r: colors for r in region}


edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')]
edges+=[(R, 'E') for R in region if R!= 'E']
edges+=[(R2, R1) for (R1, R2) in edges]

restrict = {e: lambda x,y,z,w: y!=w for e in edges}

cs = ConstraintSearch(domain, restrict)

print(cs.search())