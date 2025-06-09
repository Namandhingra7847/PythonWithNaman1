f = open("chapter9/n.txt", "r")
data = f.read()
print(data)
f.close()

# the same can be written using statement like this:

with open("chapter9/n.txt", "r") as f:
    print(f.read())

    # you don't have you explicity close the file 