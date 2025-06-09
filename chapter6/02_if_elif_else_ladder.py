a = int(input("enter your age: "))

# if elif else ladder

if(a>=18):
    print("You are above the age of consent") # The space name is INDENT
elif(a<0):
    print("you are entering the invalid negative age")
elif(a==0):
    print("you entering 0 which is invalid")
else:
    print("You are below the age of consent")

print("End of the program")
