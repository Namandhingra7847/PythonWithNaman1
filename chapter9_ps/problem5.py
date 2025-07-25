words = ["donkey","dirty","agressive"]

with open("chapter9_ps/file.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open ("chapter9_ps/file.txt","w") as f:
    f.write(content)
