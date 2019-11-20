import random

def coin_toss(call,bet):
    num = random.randint(1, 2)
    if call == "Heads" and num == 1:
        print("Heads, you won " + str(bet))
        return bet
    elif call == "Tails" and num == 2:
        print("Tails, you won " + str(bet))
        return bet
    elif call == "Tails" and num == 1:
        print("Heads, you lost " + str(-bet))
        return -bet
    else:
        print("Tails, you lost " + str(-bet))

#Test
coin_toss("Heads",25)
