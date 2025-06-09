# c/5 = (f-32)/9  #formula of celsius to fahrenite
def f_to_c(f):
    return 5*(f-32)/9 #formula of celsius to fahrenite
f = int(input("Enter temperature in F = "))
print(round(f_to_c(f),2), "Degree C ")