#Nome: Sofia Teixeira Vaz
#Nmec: 92968
from tree_search import *
from cidades import *
from strips import *
import sys


class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth'): 
        super().__init__(problem,strategy)

    def hybrid1_add_to_open(self,lnewnodes):
        even = [lnewnodes[i] for i in range (len(lnewnodes)) if  i%2 == 0]
        even.reverse()   #we're working with a queue
        odd = [lnewnodes[t] for t in range (len(lnewnodes)) if t%2 == 1]
        
        self.open_nodes = even + self.open_nodes + odd
        
    def hybrid2_add_to_open(self,lnewnodes):
        self.open_nodes+=lnewnodes
        self.open_nodes.sort(key = (lambda x: x.depth - x.offset))
        

    def search2(self):
        layers = []     #array that will have the number of nodes in a given layer (arr[i] will tell you how many nodes there are with depth i)
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            if(node.parent == None):                #if the parent doesn't exist then we're at the root and the depth is 0
                node.depth = 0                      
            else:
                node.depth = node.parent.depth + 1  #if the parent isn't None, then the depth will be the parent's depth +1 
            if self.problem.goal_test(node.state):
                self.terminal = len(self.open_nodes)+1
                self.solution = node
                return self.get_path(node)
            self.non_terminal+=1
            node.children = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                if newstate not in self.get_path(node):
                    newnode = SearchNode(newstate,node)
                    newnode.depth = node.depth + 1
                    while(len(layers)<newnode.depth+1):         #ensuring that the layers array has a place for the current depth
                        layers.append(None)
                    newnode.offset = layers[newnode.depth] if layers[newnode.depth]!= None else 0   #if the value in the array is None it's because it was just created, which means this is the first node there
                    layers[newnode.depth]= newnode.offset+1     #a new node has been added in a given depth
                    node.children.append(newnode)
            self.add_to_open(node.children)
        return None


    def search_from_middle(self):
        m = self.problem.domain.middle(self.root.state, self.problem.goal)

        #tree from root to middle
        upper = SearchProblem(self.problem.domain,self.root.state,m)
        self.from_init = SearchTree(upper, self.strategy)
        result = self.from_init.search()

        #tree from middle to objective
        lower = SearchProblem(self.problem.domain,m, self.problem.goal)
        self.to_goal = SearchTree(lower, self.strategy)
        otherResult = self.to_goal.search()

        return result + otherResult[1:]    #[1:] because we don't want to see the middle twice in the result


class MinhasCidades(Cidades):

    # state that minimizes heuristic(state1,middle)+heuristic(middle,state2)
    def middle(self,city1,city2):
        
        middle = city2
        smallest = sys.maxsize
        way = list(self.coordinates.keys())
        while(way):
            tmp= way.pop(0)
            current = self.heuristic(city1,tmp) + self.heuristic(tmp,city2)
            
            #if we're looking for a mid-way point then we can't have city1 nor city2 as possible solutions - would defeat the point of the function
            if( current < smallest and tmp!= city1 and tmp!= city2):
                smallest = current
                middle = tmp
        return middle

class MySTRIPS(STRIPS):
    def result(self, state, action):
        newstate = [p for p in state if p not in action.neg]
        newstate.extend(action.pos)
        return newstate
        

    def sort(self,state):
        res = [c for c in state]             #saving to a temporary array as to have everything in one place
        res.sort(key = (lambda x: str(x)))   #sorting alphabetically
        return res