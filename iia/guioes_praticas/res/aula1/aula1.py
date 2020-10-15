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

#1.4

#1.5

#1.6

#1.7

#1.8

#1.9

#1.10

#2.1

#2.2

#2.3

#3.1

#3.2

#3.3

#3.4

#3.5

#3.6

#3.7

#3.8

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
def allList(list, func):
    if(list == []):
        return True
    if(not func(list[0])):
        return False
    return allList(list[1:], func)


#4.7
def allList(list, func):
    if(list == []):
        return False
    if(func(list[0]) == True):
        return True
    return allList(list[1:], func)

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
        return (list[0],None , [])
    if(currentSmallest[1] == None):
        if(comparison(currentSmallest[0], list[0])>0):
            return(list[0], currentSmallest[0], [])
        return (currentSmallest[0], list[0], [])
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

#4.15

#4.16

#5.1a

#5.1b

#5.1c

#5.2