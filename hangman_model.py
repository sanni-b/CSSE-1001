#!/usr/bin/env python3
"""
Assignment 3 - View
CSSE1001
Semester 2, 2018
"""
import random

__author__ = "Sannidhi Bosamia - 45101618"

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TOTAL_ATTEMPTS = 6


class Letters:
    """Creates two lists comprised of letters from the alphabet which are used
    and unused by a string."""
    def __init__(self, string):
        """Construct Letters.

        Parameter:
            letters(str): The string that is being transformed to a Letters
                          class.
        """
        self._letters = string
        self._used_letters = list(self._letters)
        self._unused_letters = []

    def get_used_letters(self):
        """(list) Returns the letters used by the string."""
        return self._used_letters

    def get_unused_letters(self):
        """(list) Returns the letters not used by the string."""
        for letter in self._letters:
            if letter not in ALPHABET:
                self._unused_letters.append(letter)

    def set_used(self, letters):
        """Sets a letter or letters as used letters."""
        for letter in letters:
            self._used_letters.append(letter)

    def in_letters(self, letter):
        """Checks if the letter is used by the word/keyboard.

        Parameter:
            letter(str): The letter that is being checked.

        Returns:
            bool: True if the letter is used.
        """
        if letter in self.get_used_letters():
            return True
        return False

    def __repr__(self):
        """Representation of the Letters class."""
        return f"{self.get_used_letters()}"


class Letter:
    """Create a letter which has positions and whether it has been used or
    not."""
    def __init__(self, letter):
        """Construct a Letter class.

        Parameter:
            letter(str): A letter from the alphabet.
        """
        self._letter = letter
        self._string_pos = []
        self._row = int
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._keyboard_pos = (self._x1, self._y1)
        self._letter_coords = (self._x1, self._y1, self._x2, self._y2)
        self._list_pos = int

    def get_letter(self):
        """(string) Returns the letter of the object."""
        return self._letter

    def set_row(self, int):
        self._row = int

    def get_row(self):
        return self._row

    def get_string_position(self, string):
        """(list) Returns the position(s) of the letter in a string of words."""
        for i, letter in enumerate(string):
            if letter == self.get_letter():
                self._string_pos.append(i)
        return self._string_pos

    def get_keyboard_position(self):
        """(tuple) Returns a tuple containing the GUI location of the letter.
        The x and y coordinates refer to the top-left corner of the letter."""
        return self._keyboard_pos

    def get_letter_coordinates(self, key_width):
        self._x1, self._y1 = self.get_keyboard_position()
        self._x2 = int(self._x1 + key_width)
        self._y2 = int(self._y1 + key_width)
        self._letter_coords = (self._x1, self._y1, self._x2, self._y2)
        return self._letter_coords

    def set_keyboard_position(self, x, y):
        """Set the position of the letter by inputting the coordinate of the top
        left x and y coordinate.

        Parameters:
            x(int): The x-coordinate of the letter.
            y(int): The y-coordinate of the letter.
        """
        self._x1 = x
        self._y1 = y
        self._keyboard_pos = (self._x1, self._y1)

    def get_list_position(self, letters):
        """(list) Returns the position(s) of the letter in letters of the Letters
        class.

        Parameter:
            letters(Letters): The letters which the letter is being checked
                              against.
        """
        pos = []
        for letter in letters.get_used_letters():
            if letter == self._letter:
                pos.append(letters.get_used_letters().index(self._letter))
        if len(pos) > 0:
            return pos
        return None

    def __repr__(self):
        return f"Letter({self._letter})"

    def __str__(self):
        return str(self.__repr__())


class Player:
    """Creates a player of the game and keeps track of their attempts and the
    letters they have guessed."""
    def __init__(self, word):
        """Construct the player.

        Parameter:
            word(Word): The word that the player is trying to guess.
        """
        self._word = word
        self._used_letters = []
        self._attempts = 0

    def add_attempt(self):
        """Adds a (wrong) attempt."""
        self._attempts += 1

    def get_attempts(self):
        """(int) Returns the number of wrong attempts made by the player."""
        return self._attempts

    def get_attempts_left(self):
        """(int) Returns the number of attempts left by the player."""
        return TOTAL_ATTEMPTS - self._attempts

    def get_used_letters(self):
        """(list) Returns the letters used by the player."""
        return self._used_letters

    def add_letter(self, letter):
        """Adds a letter to the player's list of used letters.

        Parameter:
            letter(str): The letter that the student
        """
        if letter not in self._used_letters:
            self.get_used_letters().append(letter)

    def has_used(self, letter):
        for letters in self.get_used_letters():
            if letter.get_letter() == letters.get_letter():
                return True
        return False

    def has_won(self):
        if self._attempts > TOTAL_ATTEMPTS:
            return False
        elif self._word.get_used_letters() in self.get_used_letters():
            return True
        return None

    def __repr__(self):
        return f"Player Solving: {self._word})"


class Word(Letters):
    def __init__(self, word_list):
        self._word_list = word_list
        self._word = self._word_list[random.randint(0, len(self._word_list)-1)]
        self._word = self._word.upper()
        super().__init__(self._word)
        #self._word = self._word_list[random.randint(0, len(self._word_list)-1)]
        self._guessed = []
        #self._letters = Letters(self._word)
        self._converted = []
        self._length = 0
        self.convert()
        # get_letters = used_letters
        # has_letter = in_letters

    def get_word(self):
        return self._word

    def get_length(self):
        return len(self._word)

    def convert(self):
        for letter in self.get_used_letters():
            self._converted.append(Letter(letter))

    def get_converted(self):
        return self._converted

    def get_position(self, letter):
        pos = []
        if self.in_letters(letter):
            for i, elem in enumerate(self.get_used_letters()):
                if elem == letter:
                    pos.append(i)
            return pos
        return None

    def __repr__(self):
        return f"Word({self.get_word()})"


# do i neeed main thing
# go through my hangman gui
# phantom button