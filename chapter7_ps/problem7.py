'''
for n = 3
  *
 ***
*****


for n = 5
    *
   ***
  *****
 *******
*********
'''
n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("") # or if we want new line print("\n")
    

n = 5
for i in range(1, n + 1):
   print("*" * i)