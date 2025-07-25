class employee: 
    language = "python" #this is a class attributes
    salary = 1200000  
     
    def info(self):
        print(f"The language is {self.language}. The salaray is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

naman = employee()
naman.greet()
naman.info()

