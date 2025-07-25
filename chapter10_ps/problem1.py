class programmer:
    company = "Microsoft"

    def __init__(self,name,salary,city):
        self.name = name
        self.salary = salary
        self.city = city

p = programmer("Naman",2500000,"Rohtak")
print(f"The Name is {p.name} \nThe salary is {p.salary} \nfrom {p.city} \nCompany is {p.company}")

t = programmer("Tushar",2500000,"Rohtak")
print(f"\nThe Name is {t.name} \nThe salary is {t.salary} \nfrom {t.city} \nCompany is {t.company}")
        