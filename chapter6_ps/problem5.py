list = ["Naman", "Tushar", "Modi", "Monu"]
lc = [n.lower() for n in list]
name = input("enter your name: ").lower()

if(name in lc):
    print("your name in the list ")
else:
    print("your name not in list")