from random import randint

class train:

    def __init__(self,trainNo,fromm,to):
        self.trainNo = trainNo
        self.fromm = fromm
        self.to = to

    def book(self):
        print(f"\n🚇ticket is booked in train no: {self.trainNo} from {self.fromm} to {self.to}")
        

    def getstatus(self):
        print(f"\n🚇train no: {self.trainNo} is running on 🥳time")

    def getfare(self):
        print(f"\nticket fare in train no: {self.trainNo} from {self.fromm} to {self.to} is ₨{randint(1200,3000)}")

t = train(34565,"Rohtak","Amritsar")
t.book()
t.getstatus()
t.getfare()


