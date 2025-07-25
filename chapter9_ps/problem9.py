with open ("chapter9_ps/athis .txt") as f:
    content1 = f.read()

with open ("chapter9_ps/copy.txt") as f:
    content2 = f.read()

if (content1==content2):
    print("yes this file are identical")
else:
    print("no this file are not identical")