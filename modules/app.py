#!/usr/bin/env python3
# _*_ coding: utf8 _*_

"""
Core application frame. Initializes the window and its widgets.
"""

import tkinter
from . import display
from . import math


class App(tkinter.Tk):
    def __init__(self, master=None):
        super().__init__(master)

        # Color config
        self.color_frame_bg = "#382b26"
        self.color_frame_fg = "#b8c2b9"

        self.color_btn_bg = "#382b26"
        self.color_btn_fg = "#b8c2b9"

        # Font config
        self.default_font = "Consolas 18"
        self.display_font = "Consolas 28"

        # Window setup
        self.title("Calcpytor")
        self.geometry("404x518")
        self.resizable(width=tkinter.FALSE, height=tkinter.FALSE)
        self.configure(bg=self.color_frame_bg)

        # Widgets
        self.display_ = display.Display(self)
        self.create_widgets()
    
    def create_widgets(self):
        """
        Config and present widgets in the main frame.
        """
        
        # buttons
        # row 1
        self.add_button(self, title="%", row=1, column=0, 
                        command="")                                     # %
        self.add_button(self, title="CE", row=1, column=1, 
                        command=lambda: self.display_.clear_frame())    # CE
        self.add_button(self, title="C", row=1, column=2, 
                        command=lambda: self.display_.clear_frame())    # C
        self.add_button(self, title="<x:", row=1, column=3, 
                        command=lambda: self.display_.delete_char())    # <x:
        
        # another rows
        self.create_buttons(("7", "8", "9", "*"), 2)        # row 2
        self.create_buttons(("4", "5", "6", "-"), 3)        # row 3
        self.create_buttons(("1", "2", "3", "+"), 4)        # row 4
        self.create_buttons(("+/-", "0", ","), 5)           # row 5
        self.add_button(self, title="=", row=5, column=3, 
                        command=lambda: self.equals_btn())  # equals button

    def create_buttons(self, _names: tuple, _row: int):
        """
        Create a row of buttons by a tuple range.
        """
        
        _col = 0    # the column indetifier
        
        for x in _names:
            self.add_button(self, title=x, row=_row, column=_col)
            _col += 1

    def add_button(self, _frame:tkinter.Tk, **kwargs):
        """
        Create and pack buttons to main frame.
        """
        
        _title = kwargs.get("title", "???")
        _width = kwargs.get("width", 7)
        _command = kwargs.get("command", lambda: self.display_.update_string(_title))
        _row = kwargs.get("row", 0)
        _column = kwargs.get("column", 0)


        _btn = tkinter.Button(_frame, text=_title, width=_width, 
                              command=_command, font=self.default_font, 
                              bg=self.color_btn_bg, 
                              foreground=self.color_btn_fg, height=2)
        _btn.grid(row=_row, column=_column)

    def equals_btn(self):
        """
        Send the expression to the module containing the Math class.
        """
        
        _expression = self.display_.frame.get("1.0", "end-1c")
        math_ = math.Math(self.display_)

        math_.calc(_expression)


def start():
    _app = App()
    _app.mainloop()

if __name__ == '__main__':
    start()
