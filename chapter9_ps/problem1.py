f = open("chapter9_ps/poem.txt")
content = f.read()

if "twinkle" in content.lower():
    print("The word twinkle is present")
else:
    print("The word twinkle is not present")

f.close()
