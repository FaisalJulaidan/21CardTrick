from deck import Deck


def start_game():
    """ starts the 21 Cards Trick game """
    deck = Deck()
    # getting a deck of 21 cards and deal it into 3 piles of 7 cards each
    cards = set_into_3_piles(deck.get_deck(21))
    print(' WELCOME TO 21-CARD TRICK GAME\n', 'Choose A Card And Remember It')
    # 3 rounds needed to perform the trick
    for r in range(3):
        show_cards(cards)
        # validating users's input
        chosen_pile = validate_input(' The card in pile {}-{} >>> ', 1, 3)
        cards = do_trick(chosen_pile, cards)
    return cards


def show_cards(cards):
    """ show cards in organized columns """
    # {:20} adds 20 spaces after the assigned value in that postion by format()
    print(' | {0:20} | {1:20} | {2:20}\n'
          .format('Pile 1:', 'Pile 2:', 'Pile 3:',), '-' * 60)
    # accessing the 3 piles in parallel to show them in columns
    for c in zip(*cards):
        print(" | {0:<20} | {1:20} | {2:20}".format(*c))


def set_into_3_piles(cards):
    """ deal 21 cards into 3 piles of 7 cards in each """
    return [cards[0:7], cards[7:14], cards[14:21]]


def validate_input(msg, start, end):
    """ validate user's input depends on the given range and input type """
    while True:
        try:
            usr_input = int(input(msg.format(start, end)))
            # if user's input valid and in correct range as given
            if start <= usr_input <= end:
                return usr_input
            else:
                print('-' * 60, '\n-ERROR: only numbers between {}-{}'
                      .format(start, end))
        # if user typed non-integer values
        except ValueError:
            print('-' * 60, '\n-ERROR: Please type a number')


def do_trick(chosen_pile, cards):
    """ This function will do the following:
    1. Put the chosen pile in the middle of the deck
    2. reshuffle the deck in a specific manner then return it
    """
    # remove the selected pile form the list and reassing it to a variable
    middle_pile = cards.pop(chosen_pile - 1)
    # insert it again but in the middle [[pile] [chosen_pile] [pile]]
    cards.insert(1, middle_pile)
    # convert the list of lists (cards) into one big list
    c = sum(cards, [])
    # insert cards from 'cards' list in a new list row by row
    shuffled_deck = [c[0::3], c[1::3], c[2::3]]
    return shuffled_deck


def get_11th_card(cards):
    """ return the 11th card in the given deck """
    # convert the list of lists (cards) into one big list
    cards = sum(cards, [])
    return cards[10]

# will only execute if this file run directly and not by importing it
if __name__ == '__main__':
    print("Your card is", get_11th_card(start_game()))
