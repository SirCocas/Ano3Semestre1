
from constraintsearch import *

amigos = ["Andre", "Bernardo", "Claudio"]


domain = {p: [a for a in amigos if a!=p] for p in amigos}

domain = {"Andre": [("Claudio", "Bernardo")],
          "Bernardo": [("Andre", "Claudio"), ("Claudio", "Andre")],
          "Claudio": [("Andre", "Bernardo"), ("Bernardo", "Andre")]}


edges = [(a1, a2) for a1 in amigos for a2 in amigos if a1!= a2]


restrict = {e: (lambda x,y,z,w: y[0]!=w[0] and y[1]!=w[1]) for e in edges}

cs = ConstraintSearch(domain, restrict)

print(cs.search())