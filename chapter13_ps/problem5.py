from functools import reduce
l = [3,4,5,65,332,735,645,3246,99]

def greater(a,b):
    if a>b:
        return a
    return b

print(reduce(greater,l))