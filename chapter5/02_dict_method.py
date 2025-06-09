marks = {"Naman": 100,"Chuchu": 96,"Modi": 69,0: "Naman"}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Naman": 99 , "Sachin": 50}) # we can update and also we can add (bcoz its mutable)
# print(marks)

# print(marks.get("Naman")) #if we enter ()and.get if cannot exist in dict. PRINTS(NONE) 
# print(marks["Naman"]) #if we enter []andif cannot exist in dict. PRINTS(ERROR)
print(marks.pop("Naman")) #pop (remove)
print(marks)
