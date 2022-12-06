from random import shuffle
import trick21


def start_game():
    # start the original game and get the deck of cards and the 11th card
    deck = trick21.start_game()
    usr_card = trick21.get_11th_card(deck)
    deck = set_into_7_piles(deck)
    # p_index = the index of the pile that has the 11th card
    p_index = deck.index(next(p for p in deck if usr_card in p))
    # c_index = the index of the 11th card in that deck[p_index]
    c_index = deck[p_index].index(usr_card)

    # faced-down cards and will be shown to the user
    hidden_cards = [['Card 1', 'Card 2', 'Card 3']] * 7

    while True:
        show_cards(hidden_cards)
        # if still more than one pile left
        if hidden_cards.count('Removed') < 6:
            print("Choose Two Piles")

            # remove chosen pile if it does't have the 11th card
            pile_1 = trick21.validate_input("First Pile {}-{} >>> ", 1, 7)
            filter_cards(pile_1, hidden_cards, p_index)

            pile_2 = trick21.validate_input("Second Pile {}-{} >>> ", 1, 7)
            filter_cards(pile_2, hidden_cards, p_index)

        # if only one pile left after filtering which has the 11th card
        else:
            # remove selected cards that are not the 11th card
            print("Choose One Card")
            card_1 = trick21.validate_input("The Card is {}-{} >>> ", 1, 3)
            filter_cards(card_1, hidden_cards[p_index], c_index)

            # if only one card left in the last pile (the 11th card)
            if hidden_cards[p_index].count('Removed') > 1:
                show_cards(hidden_cards)
                # end the game
                break
    print('The left card, Card {}, is your card >> {}'
          .format(c_index + 1, usr_card))


def show_cards(cards):
    """ show piles in speparate lines"""
    for index, pile in enumerate(cards):
        print(' Pile {}: {}\n'.format(index + 1, pile), '-' * 60)


def set_into_7_piles(cards):
    """ deal 21 cards into 7 piles of 3 cards each"""
    # convert the old list of lists (deck) to one big list
    cards = sum(cards, [])
    # shuffle the deck to avoid having the 11th card +
    # every time in the same pile
    shuffle(cards)
    return [cards[0:3], cards[3:6], cards[6:9], cards[9:12], cards[12:15],
            cards[15:18], cards[18:21]]


def filter_cards(choice, cards, target):
    """ remove cards that are not the 11th card from given list(cards)"""
    # this function will filter piles that does't have the 11th card +
    # in addtion to filtering cards in piles if it is not the 11th card
    new_cards = cards
    choice -= 1
    # remove the pile/card if it does not have/is not the 11th card
    if (choice is not target):
        new_cards[choice] = "Removed"
    # if the chosen pile/card has/is the 11th card remove all other +
    # piles/cards expcet that chosen piles/card
    else:
        for i, p in enumerate(new_cards):
            if i is not target:
                new_cards[i] = "Removed"

start_game()
