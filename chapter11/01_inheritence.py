class employee:
    company = "Google"
    name = "Naman"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class programmer(employee):
#     company = "Microsoft"
#     name = "Naman"
#     def show(self,name):
#         print(f"the name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self,name):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class programmer(employee):
    company = "Microsoft"
    name = "Naman"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = employee()
b = programmer()
print(a.company,b.company)