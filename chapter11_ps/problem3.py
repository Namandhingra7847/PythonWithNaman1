class employee:
    salary = 234
    increment = 20

    @property
    def afterincrement(self):
        return self.salary + self.salary * self.increment/100
    
    @afterincrement.setter
    def afterincrement(self,salary):
        self.increment = ((salary/self.salary) - 1) * 100


e = employee()
print(e.afterincrement)
e.afterincrement = 280.8
print(e.increment)

