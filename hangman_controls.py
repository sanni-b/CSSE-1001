#!/usr/bin/env python3
"""
Assignment 3 - Controls
CSSE1001
Semester 2, 2018
"""
import tkinter as tk
from tkinter import messagebox
from hangman_model import Letter, ALPHABET

__author__ = "Sannidhi Bosamia - 45101618"

ROW1 = 'QWERTYUIOP'
ROW2 = 'ASDFGHJKL'
ROW3 = 'ZXCVBNM'

VERTICAL_LINE = 300
STAND_DIFFERENCE = 25
FACE_DIAMETER = 80
BODY_LENGTH = 120
LEG_LENGTH = 140
ARM_LENGTH = 100
TOTAL_WIDTH = VERTICAL_LINE + STAND_DIFFERENCE + ARM_LENGTH

KEY_PADDING = 10
KEY_WIDTH = (TOTAL_WIDTH + 2*ARM_LENGTH - 11*KEY_PADDING) / 10
KEYBOARD_WIDTH = TOTAL_WIDTH + 2*ARM_LENGTH
KEY_COLOUR = "#a697e2"
TITLE_PAD = 15


class Controls:
    """The controls of the game."""
    def __init__(self, window, key_canvas, word_canvas, word, player, man):
        """Construct the controls."""
        self._window = window
        self._key_canvas = key_canvas
        self._word_canvas = word_canvas
        self._word = word
        self._player = player
        self._man = man
        self._word_letters = word.get_used_letters()
        self._keyboard = []
        self._player_letters = player.get_used_letters()
        self._player_attempts = player.get_attempts()
        self._key_canvas.create_text(KEYBOARD_WIDTH/2, TITLE_PAD,
                                     text="Click on a letter to choose:",
                                     font=("Courier New", 16, "bold"),
                                     fill="black",
                                     anchor=tk.N)
        self._key_canvas.create_text(KEYBOARD_WIDTH/2,
                                     3*KEY_WIDTH + 4*KEY_PADDING + 4*TITLE_PAD,
                                     text = "Letters Used:",
                                     font = ("Courier New", 16, "bold"),
                                     fill = "black",
                                     anchor = tk.N)
        self.get_default_setup()

    def get_default_setup(self):
        """Creates the setup for the alphabet similar to that of a QWERTY
        keyboard."""
        for letter in ALPHABET:
            self._keyboard.append(Letter(letter))
        for key in self._keyboard:
            if key.get_letter() in ROW1:
                key.set_row(1)
            elif key.get_letter() in ROW2:
                key.set_row(2)
            elif key.get_letter() in ROW3:
                key.set_row(3)
            self.set_key_position(key)
        return self._keyboard

    def set_key_position(self, key):
        """Sets the positions for all the keys.

        Parameter:
            key(Letter): The key whose position is being set.
        """
        if key.get_row() == 1:
            x = KEY_PADDING
            pos = ROW1.index(key.get_letter()) + 1
            key.set_keyboard_position(pos*x + (pos-1)*KEY_WIDTH,
                                      3*KEY_PADDING + TITLE_PAD)
        elif key.get_row() == 2:
            x = 2*KEY_PADDING
            pos = ROW2.index(key.get_letter()) + 1
            key.set_keyboard_position(x + pos*KEY_PADDING + (pos-1)*KEY_WIDTH,
                                      x + KEY_WIDTH + 2*KEY_PADDING + TITLE_PAD)
        elif key.get_row() == 3:
            x = 3*KEY_PADDING + KEY_WIDTH
            pos = ROW3.index(key.get_letter()) + 1
            key.set_keyboard_position(x + pos*KEY_PADDING + (pos-1)*KEY_WIDTH,
                                      5 * KEY_PADDING + 2*KEY_WIDTH + TITLE_PAD)

    def create_keyboard(self):
        """Creates the keyboard, which allows the player to press on each key in
        order to guess the letters."""
        for key in self._keyboard:
            letter = key.get_letter()
            x, y = key.get_keyboard_position()
            self._key_canvas.create_rectangle(x,
                                              y,
                                              x + KEY_WIDTH,
                                              y + KEY_WIDTH,
                                              activefill = KEY_COLOUR)
            self._key_canvas.create_text((x + x + KEY_WIDTH) / 2,
                                         (y + y + KEY_WIDTH) / 2,
                                         text = letter,
                                         font = ("Helvetica", 16),
                                         activefill = KEY_COLOUR)
        self._key_canvas.bind("<Button-1>", self.pressed)

    def pressed(self, event):
        """Gets which key is being clicked on by the player.

        Parameter:
            event(event): The event of the key being pressed on (note: it is
                          passed on its own by the bind method).

        Returns:
            key(Letter): The key being pressed.
        """
        for key in self._keyboard:
            x1, y1, x2, y2 = key.get_letter_coordinates(KEY_WIDTH)
            if event.x in range(int(x1), int(x2)) and event.y in range(int(y1), int(y2)):
                self.in_word(key)
                return key

    def used_keyboard(self, key):
        """Creates the keyboard of used letters."""
        x, y = key.get_keyboard_position()
        y += 3*KEY_WIDTH + 4*KEY_PADDING + 3*TITLE_PAD
        self._key_canvas.create_rectangle(x,
                                          y,
                                          x + KEY_WIDTH,
                                          y + KEY_WIDTH,
                                          fill = "black")
        self._key_canvas.create_text((x + x + KEY_WIDTH) / 2,
                                     (y + y + KEY_WIDTH) / 2,
                                     text=key.get_letter(),
                                     font=("Helvetica", 16),
                                     fill="white")

    def in_word(self, key):
        """Checks to see if the key (letter) chosen by the player is in the word
        or not. If the player has lost or won, it will also display this."""
        self._player.add_letter(key.get_letter())
        self.used_keyboard(key)
        if self._word.in_letters(key.get_letter()):
            index_list = self._word.get_position(key.get_letter())
            # Convert the word to a Letters object so that each letter in the
            # word becomes a Letter object with its own coordinate position
            ltrs = self._word.get_converted()
            for index in index_list:
                x, y = ltrs[index].get_keyboard_position()
                self._word_canvas.create_text(x, y,
                                              text=key.get_letter(),
                                              font = ("Helvetica", 20))
            player_letters = self._player.get_used_letters()
            if set(self._word_letters).issubset(player_letters):
                messagebox.showinfo("Congratulations!",
                                    f"YOU SAVED A LIFE!\
[ {self._word.get_word()} ]")
                self._window.destroy()
        else:
            self._player.add_attempt()
            self._man.add_attempt()
            self._man.create()
            if self._player.has_won() is False:
                messagebox.showinfo("Oh no!",
                                    f"YOU KILLED A MAN!\nThe word was: \
{self._word.get_word()}")
                self._window.destroy()
