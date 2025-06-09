a = (23,353,43.44,44,True,"NAMAN") # We can't change Tuple with a[0] = 2  (patthar ki lakkir)

print(a)

number = a.count(44)
print(number)

number = a.index(44)
print(number)

print(len(a))

a,b,c,d,e,f = a
print(a,b,c,d,e,f)