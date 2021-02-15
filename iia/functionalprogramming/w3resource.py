# https://www.w3resource.com/python-exercises/python-functions-exercises.php

def ex1(arg1, arg2, arg3):
    currentMax = arg1 if arg1 > arg2 else arg2
    return arg3 if arg3 > currentMax else currentMax


print("ex1:" + str(ex1(1, 23, 4)))


def ex2(list):
    if(list == []):
        return 0
    return list[0] + ex2(list[1:])


print("ex2:" + str(ex2([8, 2, 3, 0, 7])))


def ex3(list):
    if(list == []):
        return 1
    return list[0] * ex3(list[1:])


print("ex3:" + str(ex3([8, 2, 3, -1, 7])))


def ex4(word):
    word = list(word)
    toRet = ""
    while(word):
        toRet += word.pop(-1)
    return toRet


print("ex4:" + ex4("1234abcd"))


def ex5(number):
    if(number == 1):
        return 1
    return number*ex5(number-1)


print("ex5:" + str(ex5(10)))


def ex6(lower, upper, val):
    return lower <= val and val <= upper


print("ex6:" + str(ex6(10, 123, 27)))


def ex7(word):
    tmp = list(word)
    upper = 0
    lower = 0
    while(tmp):
        if(tmp.pop().isupper()):
            upper += 1
        else:
            lower += 1
    return (upper, lower)


print("ex7:" + str(ex7("AAbbb")))


def ex8(values):
    return list(set(values))


print("ex8:" + str(ex8([1, 2, 3, 3, 3, 3, 4, 5])))


def ex9(value):
    tmp = value - 1
    while(tmp > 1):
        if(not value % tmp):
            return False
        tmp -= 1
    return True


print("ex9:" + str(ex9(4)))


def ex10(values):
    return [elem for elem in values if not elem % 2]


print("ex10:" + str(ex10([1, 2, 3, 4, 5, 6, 7, 8, 9])))


def ex11(value):
    divisorList = divisors(value)
    return ex2(divisorList) == value*2


def divisors(value):
    list = [1]
    tmp = value
    while(tmp > 1):
        if(not value % tmp):
            list.append(tmp)
        tmp -= 1
    return list


print("ex11:" + str(ex11(6)))


def ex12(word):
    tmp = list(word)
    while(len(tmp) > 1):
        if(tmp.pop(0) != tmp.pop(-1)):
            return False
    return True


print("ex12:" + str(ex12("tacocat")))


def ex13(value):
    if(value == 1):
        return [1]
    if(value == 2):
        return [1, 1]
    return [1] + sumPairs(ex13(value-1))+[1]


def sumPairs(list):
    tmp = list
    toRet = []
    while(len(tmp) > 1):
        toRet.append(tmp.pop(0)+tmp[0])
    return toRet


print("ex13:" + str(ex13(5)))


def ex14(word):
    tmp = list(set(list(word.lower())))
    toRet = [elem for elem in tmp if elem.isalpha()]
    return len(toRet) == 26


print("ex14:" + str(ex14("The quick brown fox jumps over the lazy dog")))


def ex15(word):
    tmp = word.split('-')
    tmp.sort()
    toRet = ""
    while(tmp):
        toRet += str(tmp.pop(0))+"-"
    return toRet[:-1]


print("ex15:" + str(ex15("green-red-yellow-black-white")))
