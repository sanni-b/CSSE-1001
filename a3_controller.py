#!/usr/bin/env python3
"""
Assignment 3 - Queue
CSSE1001
Semester 2, 2018
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from a3_model import Student

__author__ = "Sannidhi Bosamia -- 45101618"

COLUMN_WIDTH = 15
SIDE_PADDING = 20
COLUMN_PADDING = 5
BORDER = 1
SEP_THICKNESS = 2
BTN_SIZE = 2


class QueueApp(tk.Frame):
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

        separator1 = tk.Frame(self,
                              bg = "#eeeeee",
                              height = SEP_THICKNESS)
        separator1.pack(side = tk.TOP,
                        fill = tk.X)

        self._wait_label = tk.Label(self,
                                    text = "No students in queue.",
                                    bg = "white",
                                    anchor = tk.W,
                                    justify = tk.LEFT)
        self._wait_label.pack(side = tk.TOP,
                              pady = 20,
                              anchor = tk.W)

        separator2 = tk.Frame(self,
                              bg = "#eeeeee",
                              height = SEP_THICKNESS)
        separator2.pack(side = tk.TOP,
                        fill = tk.X)

        self._frame = tk.Frame(self,
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

        separator3 = tk.Frame(self,
                              bg="#eeeeee",
                              height=SEP_THICKNESS)
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


class StudentFrame(tk.Frame):
    """Creates the GUI rows for each student, adds and removes them from the
    queue, and sorts them first by questions asked and then by time."""
    def __init__(self, master, queue_list, other_list, stu_list, qtn_type):
        """Constructs the base frame for a student.

        Parameters:
            master(tk.Frame): The parent frame that the student row will be
                              created in.
            queue_list(list): The list which the student comes from.
        """
        super().__init__(master)
        self._master = master
        self._current_students = queue_list
        self._other_list = other_list
        self._stu_list = stu_list
        self._qtn = qtn_type
        self._new_frame = tk.Frame(self._master,
                                   bg="white")
        self._stu_time = tk.Label
        self._counter = 0
        self._widgets = []
        self._step()

    def _step(self):
        self.redraw_students()
        self._master.after(1000, self._step)

    def add_student(self):
        """(bool) Asks the student for their name and then adds them to the
        queue."""
        stu_name = simpledialog.askstring("Student Name", "Enter your name:")
        new_stu = Student(stu_name, 0)
        while True:
            # if a student presses 'Cancel or doesn't input a name
            toggle = True
            if stu_name is None:
                return False

            # prevents student from joining both queues at the same time
            for stu_list in self._current_students, self._other_list:
                for student in stu_list:
                    if new_stu.get_name() == student.get_name():
                        messagebox.showerror("Error!",
                                             "You are already in a queue.")
                        return False

            # adds a question to the student's question counter
            for student in self._stu_list:
                if new_stu.get_name() == student.get_name():
                    student.add_qtn()
                    new_stu.set_qtn(student.get_qtns(self._qtn), self._qtn)
                    toggle = False

            # adds student to the queue
            self._current_students.append(new_stu)
            if toggle is True:
                self._stu_list.append(new_stu)
            self.redraw_students()
            return False

    def redraw_students(self):
        """Redraws the student and gives them a row number."""
        self._counter = 0

        for widget in self._widgets:
            widget.destroy()

        self._widgets = []

        sorted_stu = self.sort_students()
        stu_frames = []
        for elem in sorted_stu:
            student = self._current_students[self._counter]
            row_num=sorted_stu.index([student.get_qtns(self._qtn),
                                      student.get_wait_time(),
                                      student.get_name()]) + 1
            student.set_row_num(row_num)
            stu_frames.append([row_num, student])
            self._counter += 1
        stu_frames.sort()

        for student in stu_frames:
            row = self.create_student_frames(student[0], student[1])
            self._widgets.append(row)

    def create_student_frames(self, row_num, student):
        """Creates the GUI for the student rows.

        Parameters:
            row_num(int): The row number that the student will have.
            student(Student): The student being added to the queue.

        Returns:
            new_frame(tk.Frame): The student row.
        """
        new_frame = tk.Frame(self,
                             bg="white")
        new_frame.pack(side=tk.TOP,
                       fill = tk.X)

        number = tk.Label(new_frame,
                          text = row_num,
                          font = ("Helvetica", 15),
                          bg = "white",
                          width = 1,
                          anchor = tk.W)
        number.pack(side = tk.LEFT,
                    anchor = tk.W,
                    fill = tk.X,
                    padx = COLUMN_PADDING)

        stu_name = tk.Label(new_frame,
                            text = student.get_name(),
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

        stu_qtns = tk.Label(new_frame,
                            text = student.get_qtns(self._qtn),
                            font = ("Helvetica", 15),
                            width = COLUMN_WIDTH,
                            bg = "white",
                            anchor = tk.W,
                            highlightthickness=BORDER,
                            highlightbackground="black",
                            justify = tk.LEFT)
        stu_qtns.pack(side = tk.LEFT,
                      anchor = tk.W,
                      fill = tk.X,
                      padx = COLUMN_PADDING)

        stu_time = tk.Label(new_frame,
                            text = student.get_str_time(),
                            font = ("Helvetica", 15),
                            width = COLUMN_WIDTH,
                            bg = "white",
                            anchor = tk.W,
                            justify = tk.LEFT,
                            highlightthickness = BORDER,
                            highlightbackground = "black")
        stu_time.pack(side = tk.LEFT,
                      anchor = tk.W,
                      fill = tk.X,
                      padx = COLUMN_PADDING)

        student.set_label_ref(stu_time)

        reject_btn = tk.Button(new_frame,
                               width = BTN_SIZE,
                               bg = "#f6a5a3",
                               highlightthickness = BORDER,
                               highlightbackground = "#e44240",
                               relief = tk.FLAT,
                               command = lambda: self.reject(row_num))
        reject_btn.pack(side = tk.LEFT,
                        anchor = tk.W,
                        fill = tk.X)

        accept_btn = tk.Button(new_frame,
                               width = BTN_SIZE,
                               bg = "#a1e1ab",
                               highlightthickness = BORDER,
                               highlightbackground = "#28bf53",
                               relief = tk.FLAT,
                               command = lambda: self.accept(row_num))
        accept_btn.pack(side = tk.LEFT,
                        anchor = tk.W,
                        fill = tk.X)

        return new_frame

    def reject_callback(self, row_num):
        self.reject(row_num)

    def sort_students(self):
        """Sorts the student first by the number of questions they've asked in
        ascending order and then by time in descending order.

        Parameter:
            qtn_type(str): The type of question asked by the student. 'q' for
                           Quick and 'l' for Long.

        Returns:
            sorted_stu(list): The sorted list of students.
        """
        sorted_stu = []
        for student in self._current_students:
            sorted_stu.append([student.get_qtns(self._qtn),
                               student.get_wait_time(),
                               student.get_name()])
        sorted_stu.sort(key = lambda k: (-k[0], k[1]), reverse = True)
        return sorted_stu

    def reject(self, row_num):
        """Removes students from the queue and from the queue list they were in.
        Does not update the number of questions the student has asked."""
        for stu in self._current_students:
            if stu.get_row_num() == row_num:
                self._current_students.remove(stu)
        self.redraw_students()

    def accept(self, row_num):
        """Removes students from the queue and from the queue list they were in.
        Updates the number of questions the student has asked (plus one)."""
        for stu in self._current_students:
            if stu.get_row_num() == row_num:
                self._current_students.remove(stu)
            stu.set_status(self._qtn)
        self.redraw_students()
