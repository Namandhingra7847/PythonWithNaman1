class employee: 
     language = "python" #this is a class attributes
     salary = 1200000  


naman = employee()
naman.name = "Naman" # this is an instance attributes
print(naman.name,naman.language,naman.salary)
# [WE CAN USE BOTH]
# print(f"{employee.name}, {employee.language}") (METHODS) [employee.name]

tushar = employee()
tushar.name = "Tushar"
print(tushar.name,tushar.salary,tushar.language)

# here name is instance/object attributes and salary , language are class
#  attributes as they directly belong to the class