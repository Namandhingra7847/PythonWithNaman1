class employee:
    company = "Google"
    name = "Naman"
    def show(self):
        print(f"\nThe name of the employee is {self.name} and the company is {self.company}".title())

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"\nOut of all the languages here is your Language: {self.language}".title())

class programmer(employee,coder):
    def showlanguage(self):
        print(f"\nThe name is {self.name} and he is good with {self.language} language".title())

a = employee()
b = programmer()

b.show()
b.printlanguage()
b.showlanguage()
