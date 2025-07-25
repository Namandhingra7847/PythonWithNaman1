def generatetable(n):
    table = ""
    for i in range (1,11):
        table += f"{n} x {i} = {n * i}\n"
    with open(f"chapter9_ps/tables of 2,20/table_{n}.txt","w") as file:
        file.write(table)

for i in range(2,21):
    generatetable(i)