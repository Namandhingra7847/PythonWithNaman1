with open ("chapter9_ps/old.txt") as f:
    content = f.read()

with open ("chapter9_ps/renamed_by_ python.txt","w") as f:
    f.write(content)

# this is by using {os module} by python
'''import os

# Original file name
old_name = "chapter9_ps/old.txt"  # Make sure this file exists

# New file name
new_name = "chapter9_ps/renamed_by_ python.txt"

try:
    os.rename(old_name, new_name)
    print(f"File renamed successfully to '{new_name}'")

except FileNotFoundError:
    print(f"The file '{old_name}' does not exist.")
except Exception as e:
    print("An error occurred:", e)'''