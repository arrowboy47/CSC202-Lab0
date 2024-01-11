# question 1
class Flower:
#Common base class for all Flowers
    def __init__(self, petalName, petalNumber, petalPrice):
        self.name = petalName
        self.petals = petalNumber
        self.price = petalPrice

    def setName(self, petalName):
        self.name = petalName

    def setPetals(self, petalNumber):
        self.petals = petalNumber

    def setPrice(self, petalPrice):
        self.price = petalPrice

    def getName(self):
        return self.name

    def getPetals(self):
        return self.petals

    def getPrice(self):
        return self.price

#This would create first object of Flower class
f1 = Flower("Sunflower", 2, 1000)
print ("Flower Details:")
print ("Name: ", f1.getName())
print ("Number of petals:", f1.getPetals())
print ("Price:",f1.getPrice())
print ("\n")

#This would create second object of Flower class
f2 = Flower("Rose", 5, 2000)
f2.setPrice(3333)
f2.setPetals(6)
print ("Flower Details:")
print ("Name: ", f2.getName())
print ("Number of petals:", f2.getPetals())
print ("Price:",f2.getPrice())


# the issue was that there was not proper indentation in the code

# question 2  
class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
    
    def getPrice(self):

        # under 10 items
        if self.amount < 10:
            return self.amount * self.price

        # 10-99 items
        elif self.amount >= 10 and self.amount <= 99:
            # 10% discount
            return self.amount * self.price * 0.9

        # 100+ items
        else:
            # 20% discount
            return self.amount * self.price * 0.8
        
        
    def make_purchase(self, balance, quanity):
        if self.name == "shirt":
            self.balance = self.balance - 50 * self.quanity
            
        if self.name == "textbook":
            self.balance = self.balance - 80 * self.quanity
            
        if self.name == "history book":
            self.balance = self.balance - 50 * self.quanity
            
        if self.name == "memory card":
            self.balance = self.balance - 140 * self.quanity
            
        if self.name == "wrist watch":
            self.balance = self.balance - 120 * self.quanity

# Question 3
class Conveter:



        



