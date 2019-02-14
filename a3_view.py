#!/usr/bin/env python3
"""
Assignment 3 - View
CSSE1001
Semester 2, 2018
"""
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from a3_model import Student
from queue2 import StudentFrame

__author__ = "Sannidhi Bosamia -- 45101618"

COLUMN_WIDTH = 15
COLUMN_PADDING = 5
SIDE_PADDING = 20

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
                            #ipady=0,
                            anchor=tk.N,
                            fill=tk.X,
                            expand=True)

        self._quick_frame = tk.Frame(self._master,
                                     bg = "white")
        self._quick_frame.pack(side=tk.LEFT,
                               pady=20,
                               padx=SIDE_PADDING,
                               anchor=tk.N,
                               expand=True,
                               fill=tk.X)

        quick_qtns = tk.Label(self._quick_frame,
                              text="Quick Questions",
                              bg="#daf2d5",
                              fg="#227b3b",
                              highlightbackground="#d1ecc3",
                              highlightthickness=1,
                              font=("Helvetica", 30, "bold"))
        quick_qtns.pack(side=tk.TOP,
                        anchor=tk.NW,
                        fill=tk.BOTH,
                        expand=True,
                        ipady=30)

        quick_label = tk.Label(self._quick_frame,
                               text="< 2 mins with a tutor",
                               bg="#daf2d5",
                               fg="#666",
                               font=("Helvetica", 14),
                               highlightbackground="#d1ecc3",
                               highlightthickness=1)
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
                        pady=10)

        quick_btn = tk.Button(self._quick_frame,
                              text="Request Quick Help",
                              command=self.quick_request,
                              bg="#9adaa4",
                              fg="white",
                              font="Helvetica",
                              highlightbackground="#62b975",
                              highlightthickness=1,
                              relief = tk.FLAT)
        quick_btn.pack(side=tk.TOP,
                       ipady=10,
                       ipadx=10,
                       pady=10,
                       anchor = tk.N)

        self._quick_headings = QueueHeadings(self._quick_frame)
        self._quick_headings.pack(side=tk.TOP)
        self._quick_headings.update_label(self._quick_list)

        self._quick_student_frame = tk.Frame(self._quick_frame,
                                            bg = "white")
        self._quick_student_frame.pack(side = tk.TOP)

        self._long_frame = tk.Frame(self._master,
                                    bg = "white")
        self._long_frame.pack(side=tk.LEFT,
                              pady=20,
                              padx=SIDE_PADDING,
                              anchor=tk.N,
                              fill=tk.X,
                              expand=True)

        long_qtn = tk.Label(self._long_frame,
                            text="Long Questions",
                            bg="#d5edf9",
                            fg="#186f93",
                            font=("Helvetica", 30, "bold"),
                            highlightthickness=1,
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
                              font=("Helvetica", 14),
                              highlightbackground="#b2e9f3",
                              highlightthickness=1)
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
                       pady=10)

        long_btn = tk.Button(self._long_frame,
                             text="Request Long Help",
                             command=self.long_request,
                             bg="#9ddced",
                             font="Helvetica",
                             fg="white",
                             highlightbackground="#66bacf",
                             highlightthickness=1,
                             relief = tk.FLAT)
        long_btn.pack(side=tk.TOP,
                      ipady=10,
                      ipadx=10,
                      pady=10)

        self._long_headings = QueueHeadings(self._long_frame)
        self._long_headings.pack(side=tk.TOP)
        self._long_headings.update_label(self._long_list)

        self._long_student_frame = tk.Frame(self._long_frame,
                                            bg = "white")
        self._long_student_frame.pack(side = tk.TOP)

    def quick_request(self):
        """What happens when a student clicks on the 'Request Quick Help'
        button."""
        self.add_to_queue(self._quick_student_frame, self._quick_list, "q")

    def long_request(self):
        """What happens when a student clicks on the 'Request Long Help'
        button."""
        self.add_to_queue(self._long_student_frame, self._long_list, "l")

class StudentFrames(tk.Frame):
    """Creates student frames for the queue."""
    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self._new_frame = tk.Frame
        self._stu_time = tk.Label

    def create_student_frames(self, qtn_type, row_num):
        """Creates the GUI for the student rows.

        Parameters:
            frame(tk.Frame): The frame under which the student frames are built.
            qtn_type(str): The type of question asked by the student. 'q' for
                           Quick and 'l' for Long.
            row_num(int): The row number that the student will have.
        """
        self._new_frame = tk.Frame(self._master,
                                   bg="white")
        self._new_frame.pack(side=tk.TOP,
                             fill = tk.X)

        number = tk.Label(self._new_frame,
                          text = row_num,
                          font = ("Helvetica", 15),
                          bg = "white",
                          width = 1,
                          anchor = tk.W)
        number.pack(side = tk.LEFT,
                    anchor = tk.W,
                    fill = tk.X,
                    padx = COLUMN_PADDING)

        stu_name = tk.Label(self._new_frame,
                            text = self._student.get_name(),
                            font = ("Helvetica", 15),
                            width = COLUMN_WIDTH,
                            bg = "white",
                            anchor = tk.W,
                            justify = tk.LEFT,
                            wraplength = 135)
        stu_name.pack(side = tk.LEFT,
                      anchor = tk.W,
                      fill = tk.X,
                      padx = COLUMN_PADDING)

        stu_qtns = tk.Label(self._new_frame,
                            text = self._student.get_qtns(qtn_type),
                            font = ("Helvetica", 15),
                            width = COLUMN_WIDTH,
                            bg = "white",
                            anchor = tk.W,
                            highlightthickness=1,
                            highlightbackground="black",
                            justify = tk.LEFT)
        stu_qtns.pack(side = tk.LEFT,
                      anchor = tk.W,
                      fill = tk.X,
                      padx = COLUMN_PADDING)

        self._stu_time = tk.Label(self._new_frame,
                                  text = self._student.get_str_time(),
                                  font = ("Helvetica", 15),
                                  width = COLUMN_WIDTH,
                                  bg = "white",
                                  anchor = tk.W,
                                  justify = tk.LEFT,
                                  highlightthickness = 1,
                                  highlightbackground = "black")
        self._stu_time.pack(side = tk.LEFT,
                            anchor = tk.W,
                            fill = tk.X,
                            padx = COLUMN_PADDING)

        self._stu_time.after(10000, self.update_time)

        reject_btn = tk.Button(self._new_frame,
                               width = 2,
                               bg = "#f6a5a3",
                               highlightthickness = 1,
                               highlightbackground = "#e44240",
                               relief = tk.FLAT,
                               command = lambda: self.reject(qtn_type))
        reject_btn.pack(side = tk.LEFT,
                        anchor = tk.W,
                        fill = tk.X)

        accept_btn = tk.Button(self._new_frame,
                               width = 2,
                               bg = "#a1e1ab",
                               highlightthickness = 1,
                               highlightbackground = "#28bf53",
                               relief = tk.FLAT,
                               command = lambda: self.accept(qtn_type))
        accept_btn.pack(side = tk.LEFT,
                        anchor = tk.W,
                        fill = tk.X)

    def reject(self, qtn_type):
        """Removes students from the queue and from the queue list they were in.
        Does not update the number of questions the student has asked.

        Parameter:
            qtn_type(str): The type of question asked by the student. 'q' for
                           Quick and 'l' for Long.
        """
        print(self._current_students)
        self._current_students.remove(self._student)
        print(self._current_students)
        self.redraw_students(qtn_type)

    def accept(self, qtn_type):
        """Removes students from the queue and from the queue list they were in.
        Updates the number of questions the student has asked (plus one)."""
        self._current_students.remove(self._student)
        self._student.set_status(qtn_type)
        self.redraw_students(qtn_type)

class QueueHeadings(tk.Frame):
    """Creates the headings for the quick questions and long questions queues
    and the label which shows the average wait time. It includes the headings
    for the student queue and updates the average wait time label."""
    def __init__(self, master):
        """Construct the GUI headings and average wait label.

        Parameter:
            master(tk.Frame): The frame under which to create the headings and
                               average wait labels.
        """
        super().__init__(master)
        self._master = master

        separator1 = tk.Frame(self._master,
                              bg = "#eeeeee",
                              height = 2)
        separator1.pack(side = tk.TOP,
                        fill = tk.X)

        self._wait_label = tk.Label(self._master,
                                    text = "No students in queue.",
                                    bg = "white",
                                    anchor = tk.W,
                                    justify = tk.LEFT)
        self._wait_label.pack(side = tk.TOP,
                              pady = 20,
                              anchor = tk.W)

        separator2 = tk.Frame(self._master,
                              bg = "#eeeeee",
                              height = 2)
        separator2.pack(side = tk.TOP,
                        fill = tk.X)

        self._frame = tk.Frame(self._master,
                               bg = "white")
        self._frame.pack(side = tk.TOP,
                         expand = True,
                         fill = tk.X,
                         pady = 5)

        num_header = tk.Label(self._frame,
                              text="#",
                              font=("Helvetica", 15, "bold"),
                              width = 1,
                              bg = "white")
        num_header.pack(side=tk.LEFT,
                        padx = COLUMN_PADDING,
                        fill = tk.X)

        name_header = tk.Label(self._frame,
                               text="Name",
                               font=("Helvetica", 15, "bold"),
                               width=COLUMN_WIDTH,
                               anchor = tk.W,
                               bg = "white",
                               justify = tk.LEFT)
        name_header.pack(side=tk.LEFT,
                         padx=COLUMN_PADDING)

        qtn_header = tk.Label(self._frame,
                              text="Questions Asked",
                              font=("Helvetica", 15, "bold"),
                              anchor = tk.W,
                              justify = tk.LEFT,
                              bg = "white",
                              width = COLUMN_WIDTH)
        qtn_header.pack(side=tk.LEFT,
                        padx=COLUMN_PADDING)

        time_header = tk.Label(self._frame,
                               text="Time",
                               font=("Helvetica", 15, "bold"),
                               anchor = tk.W,
                               width = COLUMN_WIDTH,
                               justify = tk.LEFT,
                               bg = "white")
        time_header.pack(side=tk.LEFT,
                         padx=COLUMN_PADDING)

        button_header = tk.Label(self._frame,
                                 width=4,
                                 bg = "white")
        button_header.pack(side=tk.LEFT,
                           padx=COLUMN_PADDING)

        separator3 = tk.Frame(self._master,
                              bg="#eeeeee",
                              height=2)
        separator3.pack(side=tk.TOP,
                        fill=tk.X)

    def update_label(self, queue_list):
        """Updates the average wait label.

        Parameter:
            queue_list(list): The list which is checked against (quick
                              questions or long questions) to calculate the
                              average wait time and update the label.
        """
        self._wait_label.config(text=self.get_avg_time(queue_list))
        self._wait_label.after(1, lambda: self.update_label(queue_list))

    def get_avg_time(self, queue_list):
        """Calculate the average wait time for the number of students currently
        in the queue.

        Parameter:
            queue_list(list): The list which is checked against (quick
                               questions or long questions) to calculate the
                               average wait time for students in the queue.
        """
        total_wait_time = 0
        avg_wait_time = 0
        if len(queue_list) > 0:
            for student in queue_list:
                total_wait_time += student.get_wait_time()
                avg_wait_time = total_wait_time // len(queue_list)

            if avg_wait_time == 0:
                wait_time = "a few seconds"
            else:
                wait_time = "about " + str(avg_wait_time) + " minutes"

            if len(queue_list) == 1:
                num_students = "1 student"
            else:
                num_students = str(len(queue_list)) + " students"

            avg_time=f"An average wait time of {wait_time} for {num_students}."
            return avg_time

        else:
            return "No students in queue."

def main():
    """Create a window for the queue."""
    root = tk.Tk()
    root.config(bg = "white")
    csse_queue = QueueHeader(root)
    root.mainloop()

if __name__  == "__main__":
    main()

# mvc thing
# windows v mac
