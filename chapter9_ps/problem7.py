with open("chapter9_ps/log file.txt","r") as f:
    p = f.readlines()

lineno = 1
for l in p:
    if "python" in l:
        print(f"python is present, line no. {lineno}")
        break
    lineno +=1

else:
    print("python is not present")
