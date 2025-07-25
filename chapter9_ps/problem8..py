with open ("chapter9_ps/athis.txt","r") as f:
    content = f.read()

with open ("chapter9_ps/copy.txt","w") as f:
    f.write(content)