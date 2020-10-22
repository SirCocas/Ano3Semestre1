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


#5.1a
def selectSort(list, index = 0):
    if(index == length(list)):
        return list
    temp = minimumIndex(list, index, length(list)-1)

    if(temp != index):
        list[temp], list[index] = list[index], list[temp]

    return selectSort(list, index + 1)

def minimumIndex(list, i, j):
    if(i==j):
        return i
    temp = minimumIndex(list, i+1, j)
    return (i if list[i] < list[temp] else temp)

#5.1b
def bubbleSort(list, n = None):
    if(n == None):
        return(bubbleSort(list, length(list)))
    if n == 1:
        return list
    for i in range(n-1):
        if(list[i]>list[i+1]):
            list[i], list[i+1] = list[i+1], list[i]
    return bubbleSort(list, n-1)

#5.1c
def quickSort(list, low=None, high=None):
    if(low == None or high == None ):  #second is unnecessary but doesn't hurt to check
        return quickSort(list,0, length(list)-1)
    if(low<high):
        index = partition(list, low, high)
        quickSort(list, low, index-1)
        quickSort(list, index+1, high)
    return list

def partition(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if(list[j]<= pivot):
            i=i+1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1]   
    return i+1


#5.2

#5.2a
def selectSortComp(list, comp, index = 0):
    if(index == length(list)):
        return list
    temp = minimumIndexComp(list, index, length(list)-1, comp)

    if(temp != index):
        list[temp], list[index] = list[index], list[temp]

    return selectSortComp(list,  comp, index + 1)

def minimumIndexComp(list, i, j, comp):
    if(i==j):
        return i
    temp = minimumIndexComp(list, i+1, j, comp)
    return (i if comp(list[i], list[temp]) < 0 else temp)


#5.2b
def bubbleSortComp(list,comp, n = None):
    if(n == None):
        return(bubbleSortComp(list,comp, length(list)))
    if n == 1:
        return list
    for i in range(n-1):
        if(comp(list[i],list[i+1])>0):
            list[i], list[i+1] = list[i+1], list[i]
    return bubbleSortComp(list,comp, n-1)



#5.2c
def quickSortComp(list,comp, low=None, high=None):
    if(low == None or high == None ):  #second is unnecessary but doesn't hurt to check
        return quickSortComp(list,comp,0, length(list)-1)
    if(low<high):
        index = partitionComp(list,comp, low, high)
        quickSortComp(list,comp, low, index-1)
        quickSortComp(list,comp, index+1, high)
    return list

def partitionComp(list,comp, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if(comp(list[j], pivot)<= 0):
            i=i+1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1]   
    return i+1

print(quickSortComp([1,6,2,5,0,21,-1], lambda x,y:x-y))
