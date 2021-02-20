
# Module: tree_search
# 
# This module provides a set o classes for automated
# problem solving through tree search:
#    SearchDomain  - problem domains
#    SearchProblem - concrete problems to be solved
#    SearchNode    - search tree nodes
#    SearchTree    - search tree with the necessary methods for searhing
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2019,
#  Inteligência Artificial, 2014-2019

from abc import ABC, abstractmethod

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    @abstractmethod
    def satisfies(self, state, goal):
        pass


# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return self.domain.satisfies(state,self.goal)

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent, cost = 0, heuristic = 0): 
        self.state = state
        self.parent = parent
        self.depth = self.parent.depth + 1 if self.parent != None else 0
        self.cost = cost
        self.heuristic = heuristic
        self.plan = []

    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'): 
        self.problem = problem
        root = SearchNode(problem.initial, None)
        self.open_nodes = [root]
        self.strategy = strategy
        self.terminals = 0
        self.non_terminals = 0
        self.plan = []
        

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)


    #def length(self):
    #    return self.solution.depth


    # procurar a solucao
    def search(self, limit = None):
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            
            if self.problem.goal_test(node.state):
                node.heuristic = 0
                self.solution = node
                self.terminals = len(self.open_nodes) + 1
                self.avg_branching = round((self.terminals + self.non_terminals - 1)/self.non_terminals, 2)
                self.cost = node.cost
                self.length = node.depth
                self.plan = node.plan
                return self.get_path(node)
            self.non_terminals +=1
            lnewnodes = []
            if(limit != None and node.depth >= limit):
                continue
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                if(newstate not in self.get_path(node)):
                    newnode = SearchNode(newstate,node)
                    newnode.cost = self.problem.domain.cost(node.state, a) + node.cost
                    newnode.heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                    newnode.plan = node.plan + [a]
                    lnewnodes.append(newnode)
            self.add_to_open(lnewnodes)
            

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            self.open_nodes+= lnewnodes
            self.open_nodes.sort(key=(lambda x: x.cost))
        elif self.strategy == 'greedy':
            self.open_nodes+=lnewnodes
            for i in range(len(self.open_nodes)):
                if(self.open_nodes[i].heuristic < self.open_nodes[0].heuristic):
                    temp = self.open_nodes[0]
                    self.open_nodes[0] = self.open_nodes[i]
                    self.open_nodes[i] = temp
        elif self.strategy == 'a*':
            self.open_nodes += lnewnodes
            self.open_nodes.sort(key = (lambda x: x.heuristic + x.cost))
            


#greedy: escolhe a melhor opção ATUAL -> colocar o que tem menor heurística no topo faz sentido porque é o que será "poppado" e testado primeiro