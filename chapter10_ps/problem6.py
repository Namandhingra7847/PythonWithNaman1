from random import randint

class train:

    def __init__(slf,trainNo,fromm,to):
        slf.trainNo = trainNo
        slf.fromm = fromm
        slf.to = to

    def book(naman):
        print(f"\n🚇ticket is booked in train no: {naman.trainNo} from {naman.fromm} to {naman.to}")
        

    def getstatus(slf):
        print(f"\n🚇train no: {slf.trainNo} is running on 🥳time")

    def getfare(slf):
        print(f"\nticket fare in train no: {slf.trainNo} from {slf.fromm} to {slf.to} is ₨{randint(1200,3000)}")

t = train(34565,"Rohtak","Amritsar")
t.book()
t.getstatus()
t.getfare()

