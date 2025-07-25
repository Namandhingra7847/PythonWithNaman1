try:
    a = int(input("Enter a number: "))
    print(a**2)

except ValueError as n:
    print(f"{n} is a value errror")

else:
    print("i'm inside else") # This is executed only if the try was successful