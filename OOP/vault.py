# store coin

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"Galleons: {self.galleons}, Sickles: {self.sickles}, Knots: {self.knuts}"

    #operator overloading
    def __add__(self, other):
        gelleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(gelleons,sickles,knuts)


potter = Vault(11,33,1)
print(potter)

weasley = Vault(100,213,241)
print(weasley)


# operator overloading
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts
total = Vault(galleons, sickles, knuts)
print(total)
# object.__add__(self, other)
totalV = potter + weasley
print(totalV)








