import math


#DESENVOLVIMENTO DE FUNÇÕES

#1.1
def length(list):
    if(list == []):
        return 0
    return length(list[1:])+1

#1.2
def sum(list):
    if(list == []):
        return 0
    return list[0]+ sum(list[1:])

#1.3
def check(list, elem):
    if(list == []):
        return False
    if(list[0] == elem):
        return True
    return check(list[1:], elem)

#1.4
def join(list1, list2):
    if(list2 == []):
        return list1
    return join(list1 + [list2[0]], list2[1:])

#1.5
def reverse(list):
    if(list == []):
        return []
    return reverse(list[1:])+ [list[0]]

#1.6
def capicua(list):
    if(list == []):
        return True
    if(list[0]==list[-1]):
        return capicua(list[1:-1])
    return False

#1.7
def explodeList(list):
    if(list == []):
        return []
    return list[0] + explodeList(list[1:])


#1.8
def replace(list, x,y):
    if(list == []):
        return []
    if(list[0] == x):
        list[0] = y
    return [list[0]] + replace(list[1:],x,y)


#1.9
def addListsOrdered(list1,list2):
    if(list1 == []):
        return list2
    if(list2 == []):
        return list1
    if(list1[0]> list2[0]):
        return [list2[0]] + addListsOrdered(list1, list2[1:])
    return [list1[0]] + addListsOrdered(list1[1:], list2)


#1.10
def subSets(list):
    if(list == []):
        return [[]]
    prev = subSets(list[1:])
    other =  [ [list[0]] + s for s in prev ]
    return prev+other
    
#2.1
def addPairs(list):
    if(list == []):
        return ([], [])
    prev = addPairs(list[1:])
    return ([list[0][0]] + prev[0] , [list[0][1]] + prev[1])


#2.2
def count(list, elem):
    if(list == []):
        return ([], 0)
    prev = count(list[1:], elem)
    if(list[0] == elem):
        return(prev[0], prev[1]+1)
    return ([list[0]] + prev[0], prev[1])


#2.3
def listPair(list):
    if(list == []):
        return []
    current = count(list, list[0])
    return [(list[0], current[1])] + listPair(current[0])


#3.1
def top(list):
    if(list == []):
        return None
    return list[0]

#3.2
def bottom(list):
    if(list == []):
        return None
    return list[1:]


#3.3
def juntar(list1,list2):
    if(length(list1)!= length(list2)):
        return None
    if(list1 == [] and list2 == []):
        return []
    return [(list1[0], list2[0])] + juntar(list1[1:], list2[1:]) 


#3.4
def smallestElem(list):
    if(list == []):
        return None
    prev = smallestElem(list[1:])
    if(prev == None or list[0]<prev):
        return list[0]
    return prev


#3.5
def smallestListNumber(list):
    if(list == []):
        return (None, [])
    prev = smallestListNumber(list[1:])
    if(prev[0] == None):
        return(list[0], prev[1])
    if(prev[0] > list[0]):
        return (list[0], [prev[0]] + prev[1])
    return (prev[0], [list[0]]+ prev[1])

    

#3.6
def max_min(list):
    if(list == []):
        return (None, None)
    prev = max_min(list[1:])
    if(prev[0] == None): 
        return (list[0], list[0])  #if one of them is none, both will be
    if(prev[0]< list[0]):
        return (list[0], prev[1])
    if(prev[1]>list[0]):
        return (prev[0], list[0])
    return prev



#3.7
def tupleSmall(list):
    if(list == []):
        return (None, None, [])
    currentSmallest = tupleSmall(list[1:])
    if(currentSmallest[0] == None ):
        return (list[0],list[0] , [])
    if(currentSmallest[0]>list[0]):
        return (list[0], currentSmallest[0],[currentSmallest[1]] + currentSmallest[2])
    if(currentSmallest[1]>list[0]):
        return(currentSmallest[0], list[0], [currentSmallest[1]] + currentSmallest[2])
    return (currentSmallest[0], currentSmallest[1], [list[0]] + currentSmallest[2])


#3.8
def mean(list):
    if(list ==  []):
        return (None, None)
    summ = recsum(list)
    leng = length(list)
    if(not leng%2):  #even size
        return (summ/leng,(list[leng//2]+ list[(leng//2)-1])/2 )  #NOTE: division has to be of int type and it always rounds up
    return (summ/leng, list[leng//2])

def recsum(list):
    if(list == []):
        return 0
    return sum(list[1:]) + list[0]


#4.1
four_one = lambda x: x%2==0 

#4.2
four_two = lambda x: x>0

#4.3
four_three = lambda x,y: abs(x)<abs(y)

#4.4
four_four = lambda pos: (math.sqrt(pos[0]*pos[0] +pos[1]*pos[1]), math.atan(pos[0]/pos[1]))


#4.5
def four_five(f,g,h):
    return lambda x,y,z: h(f(x,y), g(y,z))


#4.6
def allListUniv(list, func):
    if(list == []):
        return True
    if(not func(list[0])):
        return False
    return allListUniv(list[1:], func)


#4.7
def allListExist(list, func):
    if(list == []):
        return False
    if(func(list[0]) == True):
        return True
    return allListExist(list[1:], func)

#4.8 
def contains(small, big):
    if(big == []):
        return False
    if(small == []):
        return True
    if(small[0]== big[0]):
        return contains(small[1:], big) 
    return contains(small, big[1:])

#4.9
def smallest(list, comparison):
    if(list == []):
        return None
    currentSmallest = smallest(list[1:], comparison)
    if(currentSmallest == None ):
        return list[0]
    if(comparison(currentSmallest, list[0])>0):
        return list[0]
    return currentSmallest

#4.10
def smallestList(list, comparison):
    if(list == []):
        return (None, [])
    currentSmallest = smallestList(list[1:], comparison)
    if(currentSmallest[0] == None ):
        return (list[0], [])
    if(comparison(currentSmallest[0], list[0])>0):
        return (list[0], currentSmallest[1])
    return (currentSmallest[0], [list[0]] + currentSmallest[1]) 

#4.11
def smallestThree(list, comparison):
    if(list == []):
        return (None, None, [])
    currentSmallest = smallestThree(list[1:], comparison)
    if(currentSmallest[0] == None ):
        return (list[0],list[0] , [])
    if(comparison(currentSmallest[0], list[0])>0):
        return (list[0], currentSmallest[0],[currentSmallest[1]] + currentSmallest[2])
    if(comparison(currentSmallest[1], list[0])>0):
        return(currentSmallest[0], list[0], [currentSmallest[1]] + currentSmallest[2])
    return (currentSmallest[0], currentSmallest[1], [list[0]] + currentSmallest[2])

def polars(pos):  
    return (math.sqrt(pos[0]*pos[0] +pos[1]*pos[1]), math.atan(pos[0]/pos[1])) 

#4.12
def polarify(list):
    if(list == []):
        return None
    currentPolars = polarify(list[1:])
    if(currentPolars == None):
        return [polars(list[0])]
    return [polars(list[0])] + currentPolars

#4.13
def joinOrdered(list1,list2, comp):
    if(list1 == []):
        return list2
    if(list2== []):
        return list1
    if(comp(list1[0], list2[0])<=0):
        return [list1[0]] + joinOrdered(list1[1:], list2, comp)
    return [list2[0]] + joinOrdered(list1, list2[1:], comp)
     
#4.14
def explodeFunc(list, func):
    if(list == []):
        return []
    return applyFunc(list[0], func) + explodeFunc(list[1:], func)

def applyFunc(list, func):
    if(list == []):
        return []
    return [func(list[0])] + applyFunc(list[1:], func)

#4.15
def applyPair(list1, list2, func):
    if(length(list1)!= length(list2)):
        return None
    if(list1 == []):
        return []
    return [func(list1[0], list2[0])] + applyPair(list1[1:], list2[1:], func)


#4.16
#we're assuming that in this case that the function works like a numeral operation
def applyToAll(list, neut, func):
    if(list == []):
        return []
    return [function(list[0], neut, func)] + applyToAll(list[1:], neut, func)

def function(list,neut, func):
    if(list ==[]):
        return neut
    prev = function(list[1:],neut, func)
    return func(list[0],prev)


print(applyToAll([[1,2,3],[4,3], [8,7,-1]],0, lambda x,y: x+y))

#5.1a

#5.1b

#5.1c

#5.2