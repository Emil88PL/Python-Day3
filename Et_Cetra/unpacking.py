# unpacking promps for name - separate in two variables.
#

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [75,50,23]


print(total(*coins), "Knuts")


