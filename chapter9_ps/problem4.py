word = "donkey"

with open("chapter9_ps/file.txt","r") as f:
    content = f.read()

newcontent = content.replace(word,"####")

with open ("chapter9_ps/file.txt","w") as f:
    f.write(newcontent)

