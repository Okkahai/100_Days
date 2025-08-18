import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def isBusted(deck):
    for i in range(deck):
        val += deck[i]
    
    if(deck > 21):
        return True
    else:
        return False


def gameInit():
    
    player = []
    bank = []
    
    for _ in range(2):
        player.append(random.choice(cards))
        bank.append(random.choice(cards))
    
    print(f"your cards are {player[0]}, {player[1]}. Current score = {player[0] + player[1]}")
    print(f"computers first card is {bank[0]}")

    choice = input("type y to get another card")

    if choice == "y":
        player.append(random.choice(cards))
        print(f"your cards are {player[0]}, {player[1]}, {player[3]}. Current score = {player[0] + player[1] + player[3]}")
        print(f"computers first card is {bank[0]}")
        
        if isBusted == True:
            print 




gameInit()

