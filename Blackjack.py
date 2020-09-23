""" This is simplifed Blackjack game for one real player and one automatic dealer

"""
import random
import time

# Deck of cards with points
deck=['2 hearts', '3 hearts', '4 hearts', '5 hearts', '6 hearts', '7 hearts', \
      '8 hearts', '9 hearts', '10 hearts', 'J hearts', 'Q hearts', 'K hearts', \
      'A hearts', '2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds', '6 Diamonds', '7 Diamonds', \
      '8 Diamonds', '9 Diamonds', '10 Diamonds', 'J Diamonds', 'Q Diamonds', 'K Diamonds', \
      'A Diamonds', '2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs', '7 Clubs', \
      '8 Clubs', '9 Clubs', '10 Clubs', 'J Clubs', 'Q Clubs', 'K Clubs', \
      'A Clubs', '2 Spades', '3 Spades', '4 Spades', '5 Spades', '6 Spades', '7 Spades', \
      '8 Spades', '9 Spades', '10 Spades', 'J Spades', 'Q Spades', 'K Spades', 'A Spades']


def randomCard():
    # Random get and remove one card from deck
    global deck
    card = random.choice(deck)
    deck.remove(card)
    return card

def sumCard(cards):
    # Check total points for Player or Dealer after getting new card
    sum = 0
    numberA = 0
    for card in cards:
        if card.startswith('A'):
            numberA += 1
            sum += 1
        try:
            if isinstance(int(card[0]), int):
                try:
                    if isinstance(int(card[1]), int):
                        card = 10
                except ValueError:
                    card = int(card[0])
        except ValueError:
            card = 10
        sum = sum + card
    # If points more then 21 and we have 'A' card, we should to change 'A' points from 10 to 1
    if sum > 21 and numberA != 0:
        for cardA in range(1, numberA+1):
            sum = sum - 10
            if sum > 21:
                continue
            else:
                break
    return sum


class Player(object):

    def __init__(self, name, balance, wins):
        self.name = name
        self.balance = balance
        self.wins = wins

    def __str__(self):
        return f'Player {self.name} wins {self.wins} times and current balance = {self.balance}'

    def bet(self, bet):
        self.balance -= bet


class Dealer(object):

    def __init__(self, cards):
        self.cards = cards

    def __del__(self):
        del self



name = input('Choose your name: ')
player = Player(name, 0, 0)
balance = int(input(f'Choose CREDIT for {player.name}: '))
player.balance = balance
print(player)
while (input("Let's start the Game? (Yes or No) ").lower()).startswith('y'):
    while True:
        try:
            bet = int(input('Enter your BET: '))
            if (bet <= player.balance) and (bet > 0):
                player.bet(bet)
                print(f'Your BET = {bet}. Balance = {player.balance}')
                break
            else:
                print('The BET is not available. Try lower bet.')
                continue
        except ValueError:
            print('Bet must be an integer number. Try again.')
    dealer = Dealer([randomCard()])
    print('DEALER:')
    print('Card 1: ', dealer.cards[0])
    print('Card 2: XXXXXXXX')
    dealer.sum = sumCard(dealer.cards)
    print('DEALER points: ', dealer.sum)
    print('======================================================')
    time.sleep(1)
    player.cards = [randomCard(), randomCard()]
    player.sum = sumCard(player.cards)
    print('Player ', player.name, ':')
    print('Card 1: ', player.cards[0])
    print('Card 2: ', player.cards[1])
    print(f'PLAYER {player.name} points: {player.sum}')
    print('======================================================')
    while (input(f"Player {player.name}, want you Hit or Stand ").lower()).startswith('h'):
        player.cards.append(randomCard())
        print('Your card: ', player.cards[-1])
        player.sum = sumCard(player.cards)
        time.sleep(1)
        print('======================================================')
        print('Player ', player.name, ' cards:')
        for item in player.cards:
            print(item)
        print(f'PLAYER {player.name} points: {player.sum}')
        time.sleep(1)
        if player.sum == 21:
            print('You have 21 points! What about DEALER?')
            break
        elif player.sum > 21:
            print('Too much! DEALER WINS!')
            break
    if player.sum <= 21:
        while dealer.sum < player.sum:
            dealer.cards.append(randomCard())
            print('======================================================')
            print("DEALER's next card: ", dealer.cards[-1])
            dealer.sum = sumCard(dealer.cards)
            time.sleep(1)
            print("DEALER's cards: ")
            for item in dealer.cards:
                print(item)
            print('DEALER points: ', dealer.sum)
        if dealer.sum < 22:
            if dealer.sum == player.sum:
                print(f'Points are equal! {player.name} gets back the bet = {bet}')
                player.bet(-bet)
            else:
                print('DEALER WINS!!!')
        else:
            print(f'Player {player.name} WINS!!! and gets {2*bet}')
            player.bet(-2*bet)
            player.wins += 1
    print('======================================================')
    print(player)
    if player.balance == 0:
        print(f'Player {player.name} have not more money!')
        break
    dealer.__del__()



















