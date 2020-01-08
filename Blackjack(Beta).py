import random

deck = {"Ace of Diamonds": 11, "Two of Diamonds" : 2, "Three of Diamonds": 3 , "Four of Diamonds": 4 , "Five of Diamonds" : 5,
        "Six of Diamonds": 6, "Seven of Diamonds": 7, "Eight of Diamonds": 8, "Nine of Diamonds": 9, "Ten of Diamonds": 10,
        "Jack of Diamonds" :10,"Queen of Diamonds": 10, "King of Diamonds" : 10, "Ace of Hearts": 11,
        "Two of Hearts": 2, "Three of Hearts": 3 ,"Four of Hearts": 4, "Five of Hearts": 5, "Six of Hearts": 6,
        "Seven of Hearts": 7, "Eight of Hearts": 8,"Nine of Hearts": 9, "Ten of Hearts": 10,
        "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10,
        "Ace of Spades": 11, "Two of Spades": 2, "Three of Spades": 3, "Four of Spades": 4,
        "Five of Spades": 5, "Six of Spades": 6, "Seven of Spades": 7, "Eight of Spades": 8, "Nine of Spades": 9,
        "Ten of Spades": 10, "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10, "Ace of Clubs": 11,
        "Two of Clubs": 2, "Three of Clubs": 3, "Four of Clubs": 4, "Five of Clubs": 5, "Six of Clubs": 6,
        "Seven of Clubs": 7, "Eight of Clubs": 8, "Nine of Clubs": 9, "Ten of Clubs": 10,
        "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10
        }

def score_hand(hand):
    score_without_aces = 0
    ace_count = 0
    possible_scores = []
    for card in hand:
        if card.startswith('Ace'):
            ace_count += 1
            pass
        else:
            score_without_aces += deck[card]
    if ace_count == 0:
        return score_without_aces
    elif ace_count == 1:

        possible_scores.append(score_without_aces + 1)
        possible_scores.append(score_without_aces + 11)
    elif ace_count == 2:

        possible_scores.append(score_without_aces + 2)
        possible_scores.append(score_without_aces + 12)
    elif ace_count == 3:

        possible_scores.append(score_without_aces + 3)
        possible_scores.append(score_without_aces + 13)
    elif ace_count == 4:

        possible_scores.append(score_without_aces + 4)
        possible_scores.append(score_without_aces + 14)
    elif ace_count == 5:

        possible_scores.append(score_without_aces + 5)
        possible_scores.append(score_without_aces + 15)
    for s in sorted(possible_scores, reverse = True):
        if s > 21:
            continue
        else:
            return s

class Players:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw(self):
        list_deck = list(deck)
        if len(self.hand) == 0:
            self.hand.append(random.choice(list_deck))
            self.hand.append(random.choice(list_deck))
            print(self.name + "Hand: " + ' , '.join(self.hand))
        else:
            self.hand.append(random.choice(list_deck))
            print(self.name + "Hand: " + ' , '.join(self.hand))

dealer = Players("Dealer")
player = Players("Player")

Start_or_Stop = input("Welcome to Casino Blackjack table, Press Enter to continue or 'NO' to Exit")
Start_or_Stop = Start_or_Stop.upper()
if Start_or_Stop == '' \
                    '':
    print("Rules: 1. Dealer must stay on all 17's" '\n' + '       ' + "2. When player has 5 cards in hand and value less than or equal to 21, player wins.  ")#  " '\n' + '       '
    #  + "3.
    print("***************************************************************************************************************")

if Start_or_Stop == '' \
                    '':
    player.draw()
    sum_of_player = score_hand(player.hand)
    print("Player Total: ", sum_of_player)
    #print("Cards in Hand: ", len(player.hand))
    if sum_of_player == 21:
        print("Blackjack, YOU WIN")
        exit()
    choice = input("Do you want to 'HIT' or 'STAY', type your result. ")
    decision = choice.upper()
    while decision == 'HIT':
        #print(player.hand)
        player.draw()
        #print(player.hand)
        sum_of_player = score_hand(player.hand)
        if sum_of_player == None:
            print("BUST, better luck next time.")
            exit()
        print("Player Total: ", sum_of_player)
        #print("Cards in Hand: ", player.hand)
        if sum_of_player == 21:
            print("Blackjack, YOU WIN")
            break
        if len(player.hand) >= 5 and sum_of_player < 21:
            print("You beat the odds, YOU WIN")
            exit()
        elif sum_of_player > 21:
            print("BUST, better luck next time.")
            exit()

        choice = input("Do you want to 'HIT' or 'STAY', type your result. ")
        decision = choice.upper()
    while decision == "STAY":
            dealer.draw()
            sum_of_dealer = score_hand(dealer.hand)
            print("Dealer Total: ", sum_of_dealer)
            #print("Cards in Hand: ", dealer.hand)
            #print(sum_of_dealer)
            if sum_of_player == sum_of_dealer:
                print("push....you Tie, maybe next time.")
                exit()
            while sum_of_dealer < 17:
                dealer.draw()
                sum_of_dealer = score_hand(dealer.hand)
                print("Dealer Total: ", sum_of_dealer)
                #print("number of cards in dealer hand", dealer.hand)
                #print("Total of dealer cards", sum_of_dealer)
                if sum_of_player == sum_of_dealer:
                    print("push....you Tie, maybe next time.")
                    exit()
                if sum_of_dealer == None:
                    print("Dealer BUST, better luck next time.")
                    print("Player Wins!")
                    exit()
                if sum_of_dealer > 21:
                         print("Dealer Bust, Player wins")
                         exit()
            if sum_of_dealer >= 17:
                if sum_of_player > 21:
                    print("You Win, Test your luck with another round?")
                    exit()
                if sum_of_dealer < sum_of_player:
                    print("You Win, Test your luck with another round?")
                    exit()
                elif sum_of_dealer > sum_of_player:
                    print("You lose, play again???")
                    exit()
            exit()

if Start_or_Stop == "NO":
        print("You have exited game")
        exit()

