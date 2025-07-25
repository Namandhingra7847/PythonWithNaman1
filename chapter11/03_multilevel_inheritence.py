class employee:
    a = 1

class programmer(employee):
    b = 2

class manager(programmer):
    c = 3

o = employee()
o = programmer()
o = manager()
print(o.a)
print(o.a,o.b)
print(o.a,o.b,o.c)