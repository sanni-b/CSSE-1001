#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random

__author__ = "Sannidhi Bosamia -- 45101618"

# Write your classes here

#                  ---          class: Card         ---                        #
class Card:
    def __init__(self, number, colour):
        """Construct a card with a number and colour.

        Parameters:
            number (int): a number that the card has.
            colour (CardColour): a colour that the card has.
        """
        self._number = number
        self._colour = colour

    def get_number(self):
        """(int) Returns the card number."""
        return self._number

    def get_colour(self):
        """(CardColour) Returns the card colour."""
        return self._colour

    def set_number(self, number: int):
        """Set the number value of the card.

        Parameter:
            number (int): random integer value between 0 and 9 (inclusive).
        """
        self._number = number

    def set_colour(self, colour):
        """Set the colour of the card.

        Parameter:
            colour (CardColour): a colour from the choice of blue, black, red,
            green and yellow.
        """
        self._colour = colour

    def get_pickup_amount(self):
        """(int) Returns the amount of cards the next player should pickup."""
        return 0

    def matches(self, card):
        """Determines if the next card to be placed on the pile matches
        this card.

        Parameter:
            card (Card): a card with a colour and number.

        Returns:
            bool: True if it matches, False if not.
        """
        if self.get_colour() == card.get_colour():
            return True
        elif self.get_number() == card.get_number():
            return True
        else:
            return False

    def play(self, player, game):
        """Perform a special card action. Base class has no special action.

        Parameters:
            player (Player): the player who has played the card.
            game (UnoGame): a game of Uno++.
        """
        pass

    def __str__(self):
        """(str) Returns the string representation of this card."""
        return f"Card({self.get_number()}, {self.get_colour()})"

    def __repr__(self):
        """(str) Returns the string representation of this card."""
        return str(self)

class SkipCard(Card):
    def __init__(self, number, colour):
        """Construct a skip card which skips the turn of the next player.

        Parameters:
            number (int): a number which the card has.
            colour (CardColour): a colour which the card has.
        """
        super().__init__(number, colour)

    def matches(self, card):
        """Determines if the next card to be placed on the pile matches
        this card, needs to be the same colour.

        Parameter:
            card (Card): a card with a colour and number.

        Returns:
            bool: True if it matches, False if not.
        """
        if self.get_colour() == card.get_colour():
            return True
        else:
            return False

    def play(self, player, game):
        """Perform a special card action.

        Parameters:
            player (Player): the player who has played the card.
            game (UnoGame): a game of Uno++.
        """
        game.skip()

    def __str__(self):
        """(self) Returns the string representation of this card."""
        return f"SkipCard({self.get_number()}, {self.get_colour()})"

    def __repr__(self):
        """(str) Returns the string representation of this card."""
        return str(self)

class ReverseCard(Card):
    def __init__(self, number, colour):
        """Construct a reverse card which reverses the order of turns.

        Parameters:
            number (int): a number which the card has.
            colour (CardColour): a colour which the card has.
        """
        super().__init__(number, colour)

    def matches(self, card):
        """Determines if the next card to be placed on the pile matches
        this card, needs to be the same colour.

        Parameter:
            card (Card): a card with a colour and number.

        Returns:
            bool: True if it matches, False if not.
        """

        if self.get_colour() == card.get_colour():
            return True
        else:
            return False

    def play(self, player, game):
        """Perform a special card action.

        Parameters:
            player (Player): the player who has played the card.
            game (UnoGame): a game of Uno++.
        """
        game.reverse()

    def __str__(self):
        """(self) Returns the string representation of this card."""
        return f"ReverseCard({self.get_number()}, {self.get_colour()})"

    def __repr__(self):
        """(str) Returns the string representation of this card."""
        return str(self)

class Pickup2Card(Card):
    def __init__(self, number, colour):
        """Construct a card which makes the next player pickup two cards.

        Parameters:
            number (int): a number which the card has.
            colour (CardColour): a colour which the card has.
        """
        super().__init__(number, colour)

    def get_pickup_amount(self):
        """(int) Returns the amount of cards the next player should pickup."""
        return 2

    def matches(self, card):
        """Determines if the next card to be placed on the pile matches
        this card, needs to be the same colour.

        Parameter:
            card (Card): a card with a colour and number.

        Returns:
            bool: True if it matches, False if not.
        """
        if self.get_colour() == card.get_colour():
            return True
        else:
            return False
    
    def play(self, player, game):
        """Perform a special card action.

        Parameters:
            player (Player): the player who has played the card.
            game (UnoGame): a game of Uno++.
        """
        next_player_deck = game.get_turns().peak().get_deck()
        pickup_cards = game.pickup_pile.pick(self.get_pickup_amount())
        next_player_deck.add_cards(pickup_cards)

    def __str__(self):
        """(self) Returns the string representation of this card."""
        return f"Pickup2Card({self.get_number()}, {self.get_colour()})"

    def __repr__(self):
        """(str) Returns the string representation of this card."""
        return str(self)

class Pickup4Card(Card):
    def __init__(self, number, colour):
        """Construct a card which makes the next player pickup four cards.

        Parameters:
            number (int): a number which the card has.
            colour (CardColour): a colour which the card has.
        """
        super().__init__(number, colour)

    def get_pickup_amount(self):
        """(int) Returns the amount of cards the next player should pickup."""
        return 4

    def matches(self, card):
        """Matches with any card.

        Parameter:
            card (Card): a card with a colour and number.

        Returns:
            True (bool): the card matches with  any card, therefore will always
            be True.
        """
        return True

    def play(self, player, game):
        """Perform a special card action.

        Parameters:
            player (Player): the player who has played the card.
            game (UnoGame): a game of Uno++.
        """
        next_player_deck = game.get_turns().peak().get_deck()
        pickup_cards = game.pickup_pile.pick(self.get_pickup_amount())
        next_player_deck.add_cards(pickup_cards)

    def __str__(self):
        """(self) Returns the string representation of this card."""
        return f"Pickup4Card({self.get_number()}, {self.get_colour()})"

    def __repr__(self):
        """(str) Returns the string representation of this card."""
        return str(self)

#                  ---          class: Deck          ---                       #

class Deck:
    def __init__(self, starting_cards = None):
        """Construct a deck, which is a collection of Uno cards.

        Parameter:
            starting_cards (None / list): if no cards are passed through the
            deck will be initialised with None, otherwise, a list of cards.
        """
        self._cards = starting_cards
        if self._cards == None:
            self._cards = []

    def get_cards(self):
        """(list) Returns a list of cards in the deck."""
        return self._cards

    def get_amount(self):
        """(int) Returns the amount of cards in a deck."""
        return len(self._cards)

    def shuffle(self):
        """Shuffles the order of the cards in the deck."""
        random.shuffle(self._cards)

    def pick(self, amount = 1):
        """Takes the first 'amount' of cards off the deck and returns them.

        Parameter:
            amount (int): The amount of cards to take off the deck.

        Returns:
            card(s) (tuple): The card(s) taken off the deck.
        """
        picked_cards = []
        if self.get_amount() > 0:
            for n in range(amount):
                picked_cards.append(self._cards.pop(-1))
            return picked_cards

    def add_card(self, card):
        """Place a card on the top of the deck.

        Parameter:
            card (Card): a card to be added to a deck.
        """
        self._cards.append(card)

    def add_cards(self, cards):
        """Places a list of cards on the top of the deck.

        Parameter:
            cards (list): a list of cards to be added to a deck.
        """
        self._cards.extend(cards)

    def top(self):
        """Peaks at the card on top of the deck and returns it.

        Returns:
            None: if there are no cards.
            Card: the card on top of the deck.
        """
        if len(self._cards) == 0:
            return None
        else:
            return self._cards[-1]

#                  ---          class: Player          ---                     #

class Player:
    def __init__(self, name):
        """Construct a player who will be playing Uno.

        Parameter:
            name (str): the name of the player.
        """
        self._name = name
        self._deck = Deck()

    def get_name(self):
        """(str) Returns the player's name."""
        return self._name

    def get_deck(self):
        """(Deck) Returns the player's deck of cards."""
        return self._deck

    def is_playable(self):
        """Raises a NotImplemented Error on base class."""
        raise NotImplementedError("is_playable to be implemented by \
subclasses")

    def has_won(self):
        """(bool) Returns True iff the player has an empty deck and has
        therefore won."""
        deck = self.get_deck()
        if deck.get_amount() == 0:
            return True
        else:
            return False

    def pick_card(self, putdown_pile):
        """Raises a NotImplemented Error on base class."""
        raise NotImplementedError("pick_card to be implemented by subclasses")

class HumanPlayer(Player):
    def __init__(self, name):
        """Construct a human player that uses the GUI to play using the GUI.

        Parameter:
            name (str): the name of the player.
        """
        super().__init__(name)

    def is_playable(self):
        """(bool) Returns True iff the player's moves aren't automatic."""
        return True

    def pick_card(self, putdown_pile):
        """Selects a card to play from the player's current deck.

        Parameter:
            putdown_pile (Deck): the deck where the cards will be put down by
            the player.

        Returns:
            None: for non-automated players.
        """
        return None

class ComputerPlayer(Player):
    def __init__(self, name):
        """Construct a computer player that selects cards to play automatically.

        Parameter:
            name (str): the name of the player.
        """
        super().__init__(name)

    def is_playable(self):
        """(bool) Returns True iff the player's moves aren't automatic."""
        return False

    def pick_card(self, putdown_pile):
        """Selects a card to play from the player's current deck.

        Parameter:
            putdown_pile (Deck): the deck where the cards will be put down by
            the player.

        Returns:
            card (Card): a card to be played.
            None: when a card to be played cannot be found.
        """
        cards = self.get_deck().get_cards()
        for card in cards:
            if card.matches(putdown_pile.top()) == True:
                cards.remove(card)
                return card
        return None

def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
