class hey:
    a = 4

object = hey()
print(object.a)# Prints the class attribute because instance attribute is not present
object.a = 0 # instance attribute is set
print(object.a) # Prints the instance attributes because instance attributes is present
print(hey.a) # Prints the class attribute