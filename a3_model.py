#!/usr/bin/env python3
"""
Assignment 3 - Queue
CSSE1001
Semester 2, 2018
"""
import datetime as dt

__author__ = "Sannidhi Bosamia -- 45101618"


class Student:
    """Representation of a student with a name, number of questions asked, and
    the time they put in the request for the question."""
    def __init__(self, name, quick_qtn=0, long_qtn=0):
        """Creates a student with a name, number of questions asked, the
        time they put in the request.

        Parameters:
            name(str): The name of the student.
            quick_qtn(int): The number of quick questions asked by the student
                            (default value is 0).
            long_qtn(int): The number of long questions asked by the student
                           (default value is 0).
        """
        self._name = name
        self._quick_qtn = quick_qtn
        self._long_qtn = long_qtn
        self._q_status = False
        self._l_status = False
        self._req_time = dt.datetime.now()
        self._row_num = int
        self._label = None

    def get_name(self):
        """(str) Returns the student's name."""
        """(str) Returns the student's name."""
        return self._name

    def get_qtns(self, qtn_type):
        """Returns the number of questions asked by the student.

        Parameter:
            qtn_type(str): Whether the question is for the long questions queue
                           ("l") or quick queue ("q").

        Returns:
            (int): The number of questions asked by the student of the
                   specified question type.
        """
        if qtn_type == "q":
            return self._quick_qtn
        elif qtn_type == "l":
            return self._long_qtn

    def get_quick_status(self):
        """(bool) Returns True if the student's quick question has been
        accepted."""
        return self._q_status

    def get_long_status(self):
        """(bool) Returns True if the student's long question has been
        accepted."""
        return self._l_status

    def set_status(self, qtn_type):
        """Sets the status of whether their question has been accepted or not.

        Parameter:
            qtn_type(str): Whether the questions need to be set to the quick
                           questions counter ("q") or the long one ("l").
        """
        if qtn_type == "q":
            self._q_status = True
        elif qtn_type == "l":
            self._l_status = True

    def set_row_num(self, row_num):
        """Sets the students row number.

        Parameter:
            row_num(int): The student's row number.
        """
        self._row_num = row_num

    def get_row_num(self):
        """(int) Returns the row number."""
        return self._row_num

    def add_qtn(self):
        """Adds a question to the student's number of questions asked and
        returns it."""
        if self.get_quick_status():
            self.set_qtn(self.get_qtns("q") + 1, "q")
            self._q_status = False
        elif self.get_long_status():
            self.set_qtn(self.get_qtns("l") + 1, "l")
            self._l_status = False

    def set_qtn(self, num, qtn_type):
        """Sets the number of questions asked by the student.

        Parameters:
            num(int): The number of questions.
            qtn_type(str): Whether the questions need to be set to the quick
                           questions counter ("q") or the long one ("l").
        """
        if qtn_type == "q":
            self._quick_qtn = num
        elif qtn_type == "l":
            self._long_qtn = num

    def get_time(self):
        """(datetime) Returns the time the student put in the request."""
        return self._req_time

    def get_wait_time(self):
        """(int) Returns how long the student has been waiting in line, in
        minutes, and is rounded down to the lowest integer."""
        time_change = dt.datetime.now() - self._req_time
        minute = time_change.seconds // 60  # the number of seconds in a minute
        return minute

    def get_str_time(self):
        """(str) Returns how long the student has been waiting."""
        minute = self.get_wait_time()
        hour = minute // 60  # the number of minutes in an hour
        if minute <= 0:  # less than 60 seconds have passed
            return "a few seconds ago"
        elif minute in range(1, 2):  # between 1 and 2 minutes
            return "a minute ago"
        elif minute in range(2, 60):  # between 2 minutes and an hour
            return f"{minute} minutes ago"
        elif minute in range(60, 120):  # between 1 and 2 hours
            return "1 hour ago"
        else:
            return f"{hour}, hours ago"  # beyond 2 hours

    def set_label_ref(self, label):
        self._label = label

    def get_label_ref(self):
        return self._label

    def __repr__(self):
        """(str) Representation of an object in the Student class."""
        return f"Student({self._name}, Q: {self._quick_qtn}, " \
               f"L: {self._long_qtn}, {self.get_wait_time()})"
