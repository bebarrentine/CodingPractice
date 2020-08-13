# BLACKJACK

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace Low': 1, 'Ace High': 11}

# CARD CLASS

class Card:
    def __init__(self, rank, suit):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        if rank.capitalize() != 'Ace':
            self.value = values[rank.capitalize()]
        else:
            self.ace_low = values['Ace Low']
            self.ace_high = values['Ace High']

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(rank, suit)
                self.deck_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal(self):
        return self.deck_cards.pop(0)

class Bankroll:
    def __init__(self, balance):
        self.balance = balance

    def balance(self):
        return self.balance

    def win_bet(self, bet):
        self.balance += 2 * bet
        return self.balance

    def blackjack(self, bet):
        self.balance += int(2.5 * bet)
        return self.balance

    def lose_bet(self, bet):
        self.balance -= bet
        return self.balance

    def __str__(self):
        return f'Balance: ${self.balance}'

class PlayerAndDealer:
    def __init__(self, name):
        self.name = name
        self.playable_cards = []

    def hit(self, new_cards):
        self.playable_cards.append(new_cards)

    #def stay(self):
        #print("Dealer's turn.")

   # def __str__(self):
        #if self.name == 'Dealer':
          #  return f'The Dealer has a {self.playable_cards[0]} and a face down card.'
       # else:
           # return f'{self.name} has a {self.playable_cards[0]} and a {self.playable_cards[1]}.'

# GAME LOGIC

game_on = True
first_playthrough = True
while game_on:

    player = PlayerAndDealer('Bri')
    dealer = PlayerAndDealer('Dealer')

    deck = Deck()
    deck.shuffle()


    for z in range(2):
        player.hit(deck.deal())
        dealer.hit(deck.deal())

    def card_value(name):
        aceless_player_list = []
        ace_list = []
        for i in range(0, name.playable_cards.index(name.playable_cards[-1]) + 1):
            if name.playable_cards[i].rank != 'Ace':
                aceless_player_list.append(name.playable_cards[i].value)
            else:
                if sum(aceless_player_list) <= 10:
                    ace_list.append(name.playable_cards[i].ace_high)
                elif sum(aceless_player_list) > 10:
                    ace_list.append(name.playable_cards[i].ace_low)
        if sum(aceless_player_list) > 10 and sum(ace_list) > 10 and sum(aceless_player_list) + sum(ace_list) > 21:
            return sum(aceless_player_list) + sum(ace_list) - (10 * int(len(ace_list)))
        elif sum(aceless_player_list) <= 10 and sum(ace_list) > 10 and sum(aceless_player_list) + sum(ace_list) > 21:
            return sum(aceless_player_list) + sum(ace_list) - (10 * int(len(ace_list) - 1))
        else:
            return sum(aceless_player_list) + sum(ace_list)


        #print(aceless_player_list)
        #print(ace_list)
        #print(sum(aceless_player_list) + sum(ace_list))

    face_down = True
    def active_cards():
        print(' ')
        print('The Dealer has:')
        for i in range(1, dealer.playable_cards.index(dealer.playable_cards[-1]) + 1):
            print(f'{dealer.playable_cards[i]}')
        if face_down == True:
            print('1 face down card')
        else:
            print(f'{dealer.playable_cards[0]}')
        print(' ')
        print(f'{player.name} has:')
        for i in range(0, player.playable_cards.index(player.playable_cards[-1]) + 1):
            print(f'{player.playable_cards[i]}')
        print(' ')

    if first_playthrough == True:
        player_bankroll = Bankroll(100)
    else:
        player_bankroll = Bankroll(player_bankroll.balance)

    if player_bankroll.balance < 10:
        print("You don't have enough money to play anymore.")
        print('The bouncer threw you out. Time to go home and think about your crippling debt and gambling addiction.')
        game_on = False
        break

    bet = 0.001
    while bet > player_bankroll.balance or bet % 10 != 0 or bet <= 0 or bet == 0.001:
        print(player_bankroll)
        try:
            bet = int(input('Place your bet (multiples of 10): '))
        except:
            print(' ')
            print('That is not a valid bet. Try again.')
        if bet > player_bankroll.balance:
            print(' ')
            print("You don't have enough money to place that bet.")
            print(' ')
        elif bet == 0:
            print(' ')
            print("You can't bet $0.")
            print(' ')
        elif bet < 0:
            print(' ')
            print("You can't bet negative money, wizard.")
            print(' ')
        elif bet % 10 != 0:
            print(' ')
            print('Your bet must be a multiple of 10.')
            print(' ')

    print(' ')
    print(f"You bet ${bet}.")
    print(' ')
    active_cards()
    blackjack = False
    if card_value(player) == 21:
        print(f'{player.name} got a BlackJack! {player.name} should stay.')
        blackjack = True

    hit_or_stay = ''
    while hit_or_stay not in ['hit', 'stay'] or hit_or_stay == 'hit' or hit_or_stay == '21':
        hit_or_stay = input('Hit or Stay?: ').lower()
        if hit_or_stay not in ['hit', 'stay']:
            print('You must enter either Hit or Stay.')
        elif hit_or_stay == 'hit':
            player.hit(deck.deal())
            card_value(player)
            print(f"{player.name} received a {player.playable_cards[-1]}")
            active_cards()
            if card_value(player) > 21:
                break
            elif card_value(player) == 21:
                print(f'{player.name} hit 21! {player.name} should stay.')
                print(' ')
        elif hit_or_stay == 'stay':
            print(' ')
            print(f'The Dealer flipped his face down card to reveal a {dealer.playable_cards[0]}')
            face_down = False
            if card_value(dealer) == 21:
                active_cards()
                break
            elif card_value(dealer) >= card_value(player):
                active_cards()
                break
            else:
                while card_value(dealer) < card_value(player):
                    dealer.hit(deck.deal())
                    card_value(dealer)
                    print(f"The Dealer received a {dealer.playable_cards[-1]}")
                    active_cards()
                    if card_value(dealer) == 21:
                        break
                    elif card_value(dealer) >= card_value(player):
                        break
                break

    if card_value(player) > 21:
        print(f'{player.name} busted! The Dealer won.')
        print(f'{player.name} lost ${bet}!')
        player_bankroll.lose_bet(bet)
    elif card_value(dealer) > 21 and blackjack == True:
        print(f'The Dealer busted! {player.name} won with a BlackJack!')
        print(f'{player.name} won ${int(2.5 * bet)}!')
        player_bankroll.blackjack(bet)
    elif card_value(dealer) > 21:
        print(f'The Dealer busted! {player.name} won!')
        print(f'{player.name} won ${2 * bet}!')
        player_bankroll.win_bet(bet)
    elif card_value(dealer) == card_value(player):
        print('The game ends in a draw.')
        print(f'{player.name} won the ${bet} bet back.')
    elif blackjack == True and card_value(player) > card_value(dealer):
        print(f'{player.name} won with a BlackJack!')
        print(f'{player.name} won ${int(2.5 * bet)}!')
        player_bankroll.blackjack(bet)
    elif card_value(player) > card_value(dealer):
        print(f'{player.name} won!')
        print(f'{player.name} won ${2 * bet}!')
        player_bankroll.win_bet(bet)
    elif card_value(player) < card_value(dealer):
        print('The Dealer won.')
        print(f'{player.name} lost ${bet}!')
        player_bankroll.lose_bet(bet)

    print(' ')
    while game_on not in ['y', 'n']:
        game_on = input('Would you like to play again? (Y/N): ').lower()
        print(' ')
        if game_on not in ['y', 'n']:
            print('Please enter Y or N.')
        elif game_on == 'y':
            game_on = True
            first_playthrough = False
            break
        elif game_on == 'n':
            game_on = False
            break

print('Thanks for playing!')