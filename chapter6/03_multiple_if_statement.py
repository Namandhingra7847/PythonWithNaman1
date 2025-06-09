a = int(input("enter your age: "))

# if statement no: 1

if(a%2==0):
    print("Number is even") # The space name is    INDENT  
else:
    print("Number is odd")

# end of if statement no: 1

# if statement no: 2
if(a>=18):
    print("You are above the age of consent") # The space name is    INDENT
elif(a<0):
    print("you are entering the invalid negative age")
else:
    print("You are below the age of consent")

# end of if statement no: 2

print("End of the program")