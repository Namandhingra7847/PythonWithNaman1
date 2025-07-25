class employee: 
     language = "python" #this is a class attributes
     salary = 1200000  

# Note: Instance attributes, take preference over class attributes during assignment &
# retrieval.

naman = employee()
naman.language = "JavaScript" # this is an instance attributes
print(naman.language,naman.salary)