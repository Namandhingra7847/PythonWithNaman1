with open("chapter9_ps/log file.txt","r") as f:
    p = f.read()

if "python" in p:
    print("python is present")
else:
    print("python is not present")
