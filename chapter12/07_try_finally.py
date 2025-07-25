def main():
    try:
        a = int(input("Enter a number: "))
        print(a**2)
        return

    except ValueError as n:
        print(f"{n} is a value errror")
        return

    finally:
        print("i'm inside finally")  # i will definatly work (breaking all the rules) [try or except]
        
    
main()