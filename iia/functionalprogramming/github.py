# https://gist.github.com/oskarkv/3168ea3f8d7530ccd94c97c19aafe266

def recursion(list):
    print("sum:")
    print(recSum(list))
    print("maximum depth:")
    print(depth(list))
    print("largest value:")
    print(largest(list))


def recSum(list):
    if(list == []):
        return 0
    recCall = recSum(list[1:])
    while(not isinstance(list[0], int)):
        list[0] = recSum(list[0])
    return list[0] + recCall


def depth(values, currentdepth=1):
    depths = [depth(elem, currentdepth + 1)
              for elem in values if isinstance(elem, list)]
    if(len(depths) != len(values)):
        depths.append(currentdepth)
    return max(depths)


def largest(values):
    if(not isinstance(values, list)):
        return values
    singleElements = [elem for elem in values if isinstance(elem, int)]
    compositElements = [largest(elem)
                        for elem in values if isinstance(elem, list)]
    return max(singleElements + compositElements)


recursion([1, [[2], 3], [4], 5, [6, 100, [[7], [[8]], 9]], 10])
