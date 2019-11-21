import random
money = 100

#Write your game of chance functions here

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
        return -bet

def cho_han(guess,bet):
    total_roll = random.randint(2, 12)
    print("You have rolled a total of " + str(total_roll))
    if total_roll % 2 == 0 and guess == "Even":
        print("Even, you win " + str(bet))
        return bet
    elif total_roll % 2 != 0 and guess == "Even":
        print("Odd, you lose " + str(-bet))
        return -bet
    elif total_roll % 2 == 0 and guess == "Odd":
        print("Even, you lose " + str(-bet))
        return -bet
    else:
        print("Odd, you win " + str(bet))
        return bet

def card_draw(bet):
    player_card = random.randint(1, 10)
    print("You have drawn a " + str(player_card))
    dealer_card = random.randint(1, 10)
    print("The dealer has drawn a " + str(dealer_card))
    if player_card > dealer_card:
        print("You win! Your card is higher than the dealer's card. You win " + str(bet))
        return bet
    elif player_card < dealer_card:
        print("You lose! The dealer has a higher card than you! You have lost " + str(-bet))
        return -bet
    else:
        print("It's a tie! You keep your stake and win nothing!")
        return 0

#Call your game of chance functions here
print("Coin toss game:")
coin_toss("Heads",25)
print("Cho-Han:")
cho_han("Even",25)
print("Card Draw:")
card_draw(25)