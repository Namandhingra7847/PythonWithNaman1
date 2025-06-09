Letter = '''Dear <|Name|>
You are selected!
<|Date|>'''
print(Letter.replace("<|Name|>","Naman Dhingra").replace("<|Date|>","1 may 2025"))

# we add 2 replace in 1 print (this is called 'Chaining')