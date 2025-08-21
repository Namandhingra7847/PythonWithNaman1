while True:
    try:
            
        user1 = int(input("Enter the first number: "))
        user2 = int(input("Enter the second number: "))

        print("What kind of operation you want to perform \nPress + for Addition\nPress - for Substraction\nPress * for Multiplication\nPress / for Division\nPress q for Quit")
        o = input("Enter Operation: ")
        if o == "q":
            print("Quiting...")
            break # quit conditon
        match o:
            case "+":
                print(f"The result is {user1 + user2}")

            case "-":
                print(f"The result is {user1 - user2}")

            case "*":
                print(f"The result is {user1 * user2}")
                
            case "/":
                if user2 !=0:
                    print(f"The result is {user1 / user2}")
                else:
                    print("Error: Divison by zero is not allowed")
                    
            case _:
                print("Something went wrong")


    except Exception as e:
        print("Invalid input: please enter numbers only.")

