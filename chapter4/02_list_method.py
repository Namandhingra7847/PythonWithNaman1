name = ["apple","orange",5,32.3,False,"tushar","modi"] 
print(name)

name.append("Naman")
print(name)
#if we start method on string (it not change) but if we start method on list (its change)

l1 = [1,3,5,4,8,9] 
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(1,51)
print(l1) # insert 51 such that its index in the 1

l1.pop(2)
print(l1)

l1.remove(9)
print(l1)