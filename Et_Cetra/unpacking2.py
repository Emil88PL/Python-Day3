# unpacking promps for name - separate in two variables.
#

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons":100, "sickles":50, "knuts":24}


print(total(**coins), "Knuts")


