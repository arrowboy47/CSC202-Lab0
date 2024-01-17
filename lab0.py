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
            return(balance - 50 * quanity)
            
        if self.name == "textbook":
            return(balance - 80 * quanity)
            
        if self.name == "history book":
            return(balance - 50 * quanity)
            
        if self.name == "memory card":
            return(balance - 140 * quanity)
            
        if self.name == "wrist watch":
            return(balance - 120 * quanity)

# Question 3
class Converter:
    def __init__(self, length, unit):
        # error for when unit is not one of the excepted units
        if unit not in ["m", "cm", "mm", "km", "yd", "ft", "in"]:
            raise ValueError("unit must be one of m, cm, mm, km, yd, ft, in")
        
        self.length = length
        self.unit = unit
    
    
    
    def m(self):
        if self.unit == "m":
            return self.length
        elif self.unit == "cm":
            return self.length / 100
        elif self.unit == "mm":
            return self.length / 1000
        elif self.unit == "km":
            return self.length * 1000
        elif self.unit == "yd":
            return self.length * 0.9144
        elif self.unit == "ft":
            return self.length * 0.3048
        elif self.unit == "in":
            return self.length * 0.0254
        
    def cm(self):
        if self.unit == "m":
            return self.length * 100
        elif self.unit == "cm":
            return self.length
        elif self.unit == "mm":
            return self.length / 10
        elif self.unit == "km":
            return self.length * 100000
        elif self.unit == "yd":
            return self.length * 91.44
        elif self.unit == "ft":
            return self.length * 30.48
        elif self.unit == "in":
            return self.length * 2.54

    def mm(self):
        if self.unit == "m":
            return self.length * 1000
        elif self.unit == "cm":
            return self.length * 10
        elif self.unit == "mm":
            return self.length
        elif self.unit == "km":
            return self.length * 1000000
        elif self.unit == "yd":
            return self.length * 914.4
        elif self.unit == "ft":
            return self.length * 304.8
        elif self.unit == "in":
            return self.length * 25.4
        
        
    def km(self):
        if self.unit == "m":
            return self.length / 1000
        elif self.unit == "cm":
            return self.length / 100000
        elif self.unit == "mm":
            return self.length / 1000000
        elif self.unit == "km":
            return self.length
        elif self.unit == "yd":
            return self.length * 0.0009144
        elif self.unit == "ft":
            return self.length * 0.0003048
        elif self.unit == "in":
            return self.length * 0.0000254

    def inch(self):
        if self.unit == "m":
            return self.length * 39.3701
        elif self.unit == "cm":
            return self.length * 0.393701
        elif self.unit == "mm":
            return self.length * 0.0393701
        elif self.unit == "km":
            return self.length * 39370.1
        elif self.unit == "yd":
            return self.length * 36
        elif self.unit == "ft":
            return self.length * 12
        elif self.unit == "in":
            return self.length

    def ft(self):
        if self.unit == "m":
            return self.length * 3.28084
        elif self.unit == "cm":
            return self.length * 0.0328084
        elif self.unit == "mm":
            return self.length * 0.00328084
        elif self.unit == "km":
            return self.length * 3280.84
        elif self.unit == "yd":
            return self.length * 3
        elif self.unit == "ft":
            return self.length
        elif self.unit == "in":
            return self.length * 0.0833333

    def yd(self):
        if self.unit == "m":
            return self.length * 1.09361
        elif self.unit == "cm":
            return self.length * 0.0109361
        elif self.unit == "mm":
            return self.length * 0.00109361
        elif self.unit == "km":
            return self.length * 1093.61
        elif self.unit == "yd":
            return self.length
        elif self.unit == "ft":
            return self.length * 0.333333
        elif self.unit == "in":
            return self.length * 0.0277778


# test cases:


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

# q2 test cases
p1 = Product("shirt", 50, 5)
print(p1.getPrice())

p2 = Product("textbook", 80, 10)
print(p2.getPrice())

p3 = Product("history book", 50, 100)

# price test cases
p1.getPrice()
p2.getPrice()
p3.getPrice()

# make_purchase test cases
p1.make_purchase(1000, 5)

p2.make_purchase(1000, 10)



# q3 test cases
meas1 = Converter(12, "m")
meas2 = Converter(0.232, "km")
meas3 = Converter(1000001, "mm")
meas4 = Converter(480, "in")

invalid = Converter(100, "liters")

# m test cases
meas1.m()
meas2.m()
meas3.m()

# yd test cases
meas1.yd()
meas2.yd()
meas3.yd()