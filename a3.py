#!/usr/bin/env python3
"""
Assignment 3 - View
CSSE1001
Semester 2, 2018
"""
import tkinter as tk
from hangman_gui import HangmanWindow
from  import BORDER, SIDE_PADDING
from queue3 import QueueApp, StudentFrame

__author__ = "Sannidhi Bosamia -- 45101618"

TITLE_SIZE = 30
SUBTITLE_SIZE = 14


class QueueHeader(tk.Frame):
    """Creates a GUI for the top half of the queue, including the important
    header, and the quick question and long question labels and the bottom
    text. It also adds students to the queue."""
    def __init__(self, master):
        """Constructs the GUI for the queue headers and the frames for the
        queues.

        Parameter:
            master(tk.Tk): The Tkinter interface for the GUI to be created on.
        """
        super().__init__(master)
        self._master = master
        self._master.title("CSSE1001 Queue")
        self._quick_list = [] # students currently in the quick queue
        self._long_list = [] # students currently in the long queue
        self._stu_list = []  # all the students who have ever been in the queue
        # game menu
        menubar = tk.Menu(self._master)
        # tell master what it's menu is
        self._master.config(menu=menubar)
        gamemenu = tk.Menu(menubar)
        menubar.add_cascade(label="Play Game!", menu=gamemenu)
        gamemenu.add_command(label="New Game", command=self.play_game)

        important_frame = tk.Frame(self._master,
                                   bg="#fefcec")
        important_frame.pack(side=tk.TOP,
                             anchor=tk.NW,
                             fill=tk.BOTH,
                             ipady=25)

        important_title = tk.Label(important_frame,
                                   text="Important",
                                   font=("Helvetica", 16, "bold"),
                                   fg="#cf9943",
                                   bg="#fefcec",
                                   justify=tk.LEFT,
                                   anchor=tk.W)
        important_title.pack(side=tk.TOP,
                             padx=SIDE_PADDING,
                             anchor=tk.SW,
                             expand=True,
                             fill=tk.X)

        important_text = tk.Label(important_frame,
                                  text="Individual assessment items must be \
solely your own work. While students are encouraged to have high level \
conversations about the problems they are trying to solve, you must not look \
at another student's code or copy from it. The university uses sophisticated \
anti-collusion measures to automatically detect similarity between \
assignment submissions.",
                                  bg="#fefcec",
                                  justify=tk.LEFT,
                                  anchor=tk.NW,
                                  wraplength=1100)
        important_text.pack(side=tk.TOP,
                            padx=SIDE_PADDING,
                            anchor=tk.N,
                            fill=tk.X,
                            expand=True)

        self._quick_frame = tk.Frame(self._master,
                                     bg = "white")
        self._quick_frame.pack(side=tk.LEFT,
                               pady=SIDE_PADDING,
                               padx=SIDE_PADDING,
                               anchor=tk.N,
                               expand=True,
                               fill=tk.X)

        quick_qtns = tk.Label(self._quick_frame,
                              text="Quick Questions",
                              bg="#daf2d5",
                              fg="#227b3b",
                              highlightbackground="#d1ecc3",
                              highlightthickness=BORDER,
                              font=("Helvetica", TITLE_SIZE, "bold"))
        quick_qtns.pack(side=tk.TOP,
                        anchor=tk.NW,
                        fill=tk.BOTH,
                        expand=True,
                        ipady=30)

        quick_label = tk.Label(self._quick_frame,
                               text="< 2 mins with a tutor",
                               bg="#daf2d5",
                               fg="#666",
                               font=("Helvetica", SUBTITLE_SIZE),
                               highlightbackground="#d1ecc3",
                               highlightthickness=BORDER)
        quick_label.pack(side=tk.TOP,
                         ipady=5,
                         anchor = tk.N,
                         fill=tk.BOTH,
                         expand=True)

        quick_text = tk.Label(self._quick_frame,
                              text=("Some examples of quick questions:\n  " +
                                    u"\u2022 Syntax errors\n  " +
                                    u"\u2022 Interpreting error output\n  " +
                                    u"\u2022 Assignment/MyPyTutor \
interpretation\n  " +
                                    u"\u2022 MyPyTutor submission issues"),
                              justify=tk.LEFT,
                              bg = "white")
        quick_text.pack(side=tk.TOP,
                        anchor=tk.NW,
                        pady=SIDE_PADDING/2)

        quick_btn = tk.Button(self._quick_frame,
                              text="Request Quick Help",
                              command=self.quick_request,
                              bg="#9adaa4",
                              fg="white",
                              font="Helvetica",
                              highlightbackground="#62b975",
                              highlightthickness=BORDER,
                              relief = tk.FLAT)
        quick_btn.pack(side=tk.TOP,
                       ipady=SIDE_PADDING/2,
                       ipadx=SIDE_PADDING/2,
                       pady=SIDE_PADDING/2,
                       anchor = tk.N)

        self._quick_headings = QueueApp(self._quick_frame)
        self._quick_headings.pack(side=tk.TOP)
        self._quick_headings.update_label(self._quick_list)

        self._quick_student_frame = tk.Frame(self._quick_frame,
                                            bg = "white")
        self._quick_student_frame.pack(side = tk.TOP)

        self._long_frame = tk.Frame(self._master,
                                    bg = "white")
        self._long_frame.pack(side=tk.LEFT,
                              pady=SIDE_PADDING,
                              padx=SIDE_PADDING,
                              anchor=tk.N,
                              fill=tk.X,
                              expand=True)

        long_qtn = tk.Label(self._long_frame,
                            text="Long Questions",
                            bg="#d5edf9",
                            fg="#186f93",
                            font=("Helvetica", TITLE_SIZE, "bold"),
                            highlightthickness=BORDER,
                            highlightbackground="#b2e9f3")
        long_qtn.pack(side=tk.TOP,
                      anchor=tk.NE,
                      fill=tk.BOTH,
                      expand=True,
                      ipady=30)

        long_label = tk.Label(self._long_frame,
                              text="> 2 mins with a tutor",
                              bg="#d5edf9",
                              fg="#666",
                              font=("Helvetica", SUBTITLE_SIZE),
                              highlightbackground="#b2e9f3",
                              highlightthickness=BORDER)
        long_label.pack(side=tk.TOP,
                        ipady=5,
                        fill=tk.BOTH,
                        expand=True)

        long_text = tk.Label(self._long_frame,
                             text=("Some examples of long questions:\n  " +
                                   u"\u2022 Open ended questions\n  " +
                                   u"\u2022 How to start a problem\n  " +
                                   u"\u2022 How to improve code\n  " +
                                   u"\u2022 Debugging\n  " +
                                   u"\u2022 Assignment help"),
                             justify=tk.LEFT,
                             bg = "white")
        long_text.pack(side=tk.TOP,
                       anchor=tk.W,
                       pady=SIDE_PADDING/2)

        long_btn = tk.Button(self._long_frame,
                             text="Request Long Help",
                             command=self.long_request,
                             bg="#9ddced",
                             font="Helvetica",
                             fg="white",
                             highlightbackground="#66bacf",
                             highlightthickness=BORDER,
                             relief = tk.FLAT)
        long_btn.pack(side=tk.TOP,
                      ipady=SIDE_PADDING/2,
                      ipadx=SIDE_PADDING/2,
                      pady=SIDE_PADDING/2)

        self._long_headings = QueueApp(self._long_frame)
        self._long_headings.pack(side=tk.TOP)
        self._long_headings.update_label(self._long_list)

        self._long_student_frame = tk.Frame(self._long_frame,
                                            bg = "white")
        self._long_student_frame.pack(side = tk.TOP)

        self._long = StudentFrame(self._long_student_frame,
                     self._long_list,
                     self._quick_list,
                     self._stu_list,
                     "l")
        self._long.pack()


        self._quick = StudentFrame(self._quick_student_frame,
                     self._quick_list,
                     self._long_list,
                     self._stu_list,
                     "q")
        self._quick.pack()

    def quick_request(self):
        """What happens when a student clicks on the 'Request Quick Help'
        button."""
        self._quick.add_student()

    def long_request(self):
        """What happens when a student clicks on the 'Request Long Help'
        button."""
        self._long.add_student()

    def play_game(self):
        app = HangmanWindow(self._master, "words.txt")


def main():
    """Create a window for the queue."""
    root = tk.Tk()
    root.config(bg = "white")
    root.geometry('1200x800')
    csse_queue = QueueHeader(root)
    root.mainloop()

if __name__  == "__main__":
    main()