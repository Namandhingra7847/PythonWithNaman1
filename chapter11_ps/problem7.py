class vector:
    def __init__(self,l):
        self.l = l

    
    def __len__(self):
        return len(self.l)

v1 = vector("naman")

print(len(v1))