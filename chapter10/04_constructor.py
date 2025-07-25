class employee: 
    language = "python" #this is a class attributes
    salary = 1200000  
     
    def __init__(self,name,salary,language): # dunder method (init) which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def info(self):
        print(f"The language is {self.language}. The salaray is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

naman = employee("Naman", 1300000, "JavaScript")

print(naman.name,naman.salary,naman.language)



