#!/usr/bin/env python3
"""
Assignment 3 - View
CSSE1001
Semester 2, 2018
"""
import tkinter as tk
from math import cos, sin, pi
from hangman_model import Word, Player
from hangman_controls import VERTICAL_LINE, STAND_DIFFERENCE, FACE_DIAMETER
from hangman_controls import BODY_LENGTH, LEG_LENGTH, ARM_LENGTH, TOTAL_WIDTH
from hangman_controls import KEY_WIDTH, KEY_PADDING, KEYBOARD_WIDTH
from hangman_controls import Controls

__author__ = "Sannidhi Bosamia - 45101618"

WIN_HEIGHT = 750
PADDING = 30
HANG_HEIGHT = 450
HANG_LINE = 50
LINE_THICKNESS = 10
FACE_RADIUS = FACE_DIAMETER / 2
FACE_X1 = STAND_DIFFERENCE + VERTICAL_LINE - FACE_RADIUS - LINE_THICKNESS/2
FACE_X2 = STAND_DIFFERENCE + VERTICAL_LINE + FACE_RADIUS - LINE_THICKNESS/2
WOOD_COLOUR = "#362204"


class HangmanWindow(tk.Canvas):
    """The window in which Hangman is played."""
    def __init__(self, master, word_file):
        """Construct a Hangman game.

        Parameters:
            master(tk.Tk): The root of the window.
            word_file(): The text file of which the words will be used.
        """
        super().__init__(master)
        self._master = master
        self._master.title("Hangman")
        self._game_window = tk.Toplevel(self._master)

        # the canvas which has the hangman window and the keyboard
        big_canvas = tk.Canvas(self._game_window)
        big_canvas.pack(side = tk.TOP)

        # the hangman canvas
        hang_canvas = tk.Canvas(big_canvas,
                                height = HANG_HEIGHT,
                                width = TOTAL_WIDTH)
        hang_canvas.pack(side = tk.LEFT,
                         pady = PADDING,
                         padx= PADDING)

        # the canvas for the keyboard
        key_canvas = tk.Canvas(big_canvas,
                               height = HANG_HEIGHT + 2*PADDING,
                               width = KEYBOARD_WIDTH)
        key_canvas.pack(side = tk.LEFT,
                        pady = PADDING/2,
                        padx = 3*PADDING/4,
                        anchor = tk.N)

        # the canvas for the word
        word_canvas = tk.Canvas(self._game_window,
                                height=2*KEY_PADDING + KEY_WIDTH,
                                width = 2*TOTAL_WIDTH)
        word_canvas.pack(side = tk.TOP,
                         pady = PADDING/2)
        # getting a list of words from the word file submitted as a parameter
        with open(word_file) as file:
            self._word_list = []
            for i, line in enumerate(file, 1):
                word = line.strip()
                if len(word) in range(3, 10):
                    self._word_list.append(word)
        self._word = Word(self._word_list)
        self.draw_word(word_canvas)
        self.draw_hang_stand(hang_canvas)
        self._player = Player(self._word)
        man = Man(hang_canvas)
        controls = Controls(self._game_window, key_canvas, word_canvas,
                            self._word, self._player, man)
        controls.create_keyboard()

    def draw_word(self, canvas):
        """Draws the blanks for the word.

        Parameter:
            canvas(tk.Canvas): The canvas in which the word is being drawn.
        """
        blank = self._word.get_length()
        x = 10
        y = 10
        for i in range(blank):
            canvas.create_rectangle(x, y, x + KEY_WIDTH, y + KEY_WIDTH)
            ltr = self._word.get_converted()[i]
            ltr.set_keyboard_position((2*x + KEY_WIDTH)/2, (2*y + KEY_WIDTH)/2)
            x += KEY_WIDTH + 10

    def draw_hang_stand(self, canvas):
        """Draws the hangman stand.

        Parameter:
            canvas(tk.Canvas): The canvas in which to draw the hangman stand.
        """
        # vertical line at the top
        canvas.create_rectangle(STAND_DIFFERENCE,
                                0,
                                VERTICAL_LINE + STAND_DIFFERENCE,
                                LINE_THICKNESS,
                                fill = WOOD_COLOUR)
        # horizontal line that supports the structure
        canvas.create_rectangle(STAND_DIFFERENCE,
                                LINE_THICKNESS,
                                LINE_THICKNESS + STAND_DIFFERENCE,
                                HANG_HEIGHT - LINE_THICKNESS,
                                fill = WOOD_COLOUR)
        # bottom line that acts as the stabilizer of the structure
        canvas.create_rectangle(0,
                                HANG_HEIGHT - LINE_THICKNESS,
                                VERTICAL_LINE,
                                HANG_HEIGHT,
                                fill = WOOD_COLOUR)
        # the piece of structure where the noose is tied
        canvas.create_rectangle(STAND_DIFFERENCE+VERTICAL_LINE-LINE_THICKNESS,
                                LINE_THICKNESS,
                                VERTICAL_LINE + STAND_DIFFERENCE,
                                LINE_THICKNESS + HANG_LINE,
                                fill = WOOD_COLOUR)
        # diagonal line between horizontal and top vertical line
        canvas.create_line(STAND_DIFFERENCE + LINE_THICKNESS,
                           HANG_HEIGHT / 4,
                           TOTAL_WIDTH / 4,
                           LINE_THICKNESS,
                           fill = WOOD_COLOUR)


class Man(tk.Canvas):
    """The man that might be hanged."""
    def __init__(self, canvas):
        """Constructs the man.

        Parameter:
            canvas(tk.canvas): The canvas in which the man will appear.
        """
        super().__init__(canvas)
        self._canvas = canvas
        self._arms = 0  # keeps track of how many arms have been drawn
        self._legs = 0  # keeps track of how many legs have been drawn
        self._attempts = 0
        # the y-coordinate to draw the start of the body
        self._body_y = LINE_THICKNESS + HANG_LINE + FACE_DIAMETER
        # the x-coordinate to draw the start of the body
        self._body_x = STAND_DIFFERENCE + VERTICAL_LINE - LINE_THICKNESS/2

    def get_attempts(self):
        """(int) Returns the number of attempts."""
        return self._attempts

    def set_attempts(self, attempts):
        """Set the number of attempts made.

        Parameter:
            attempts(int): The number of attempts made by the player.
        """
        self._attempts = attempts

    def add_attempt(self):
        """Adds an attempt to the number of attempts made."""
        self._attempts += 1

    def create(self):
        """Creates all the parts."""
        self.create_face()
        self.create_body()
        self.create_arm()
        self.create_leg()

    def create_face(self):
        """Creates the face of the man if it is the first wrong attempt by the
        player."""
        if self._attempts == 1:
            self._canvas.create_oval(FACE_X1,
                                     LINE_THICKNESS + HANG_LINE,
                                     FACE_X2,
                                     self._body_y)

    def create_body(self):
        """Creates the body of the man if it is the second wrong attempt by the
        player."""
        if self._attempts == 2:
            x = self._body_x
            self._canvas.create_line(x, self._body_y,
                                     x, self._body_y + BODY_LENGTH)

    def create_arm(self):
        """Creates the arms of the man if it is the second or third wrong
        attempt by the player."""
        if self._attempts in [3, 4]:
            arm_start_x = self._body_x
            arm_start_y = self._body_y + BODY_LENGTH / 6
            arm_end_y = arm_start_y + cos(pi/4) * ARM_LENGTH
            if self._arms == 0:
                arm_end_x = arm_start_x - sin(pi/4) * ARM_LENGTH
                self._arms += 1
            else:
                arm_end_x = arm_start_x + sin(pi/4) * ARM_LENGTH

            self._canvas.create_line(arm_start_x, arm_start_y,
                                     arm_end_x, arm_end_y)

    def create_leg(self):
        """Creates the legs of the man if it is the fourth or fifth wrong
        attempt by the player."""
        if self._attempts in [5, 6]:
            leg_start_x = self._body_x
            leg_start_y = self._body_y + BODY_LENGTH
            leg_end_y = self._body_y + BODY_LENGTH + cos(2*pi/7) * LEG_LENGTH
            if self._legs == 0:
                leg_end_x = self._body_x - cos(2*pi/7) * LEG_LENGTH
                self._legs += 1
            else:
                leg_end_x = self._body_x + cos(2*pi/7) * LEG_LENGTH

            self._canvas.create_line(leg_start_x, leg_start_y,
                                     leg_end_x, leg_end_y)

def main():
    root = tk.Tk()
    hang = HangmanWindow(root, 'words.txt')
    root.mainloop()


if __name__ == '__main__':
    main()
