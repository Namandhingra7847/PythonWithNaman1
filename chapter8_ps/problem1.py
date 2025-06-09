a = int(input("Enter rhe number 1: "))
b = int(input("Enter rhe number 2: "))
c = int(input("Enter rhe number 3: "))
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
print(greatest(a,b,c))