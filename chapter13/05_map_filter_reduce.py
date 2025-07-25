from functools import reduce
# Map example

l = [2,4,1,65,4]

square = lambda x:x*x

sqlist = map(square, l)
print(list(sqlist))

# Filter example

def even(n):
    if n%2 == 0:
        return True
    return False

onlye = filter(even, l)
print(list(onlye))

#Reduce example

def sum(a,b):
    return a+b
print(reduce(sum,l))
