#!/usr/bin/env python3
# _*_ coding: utf8 _*_

"""
The calculator text presenter.
"""

import tkinter


class Display:
    def __init__(self, frame: tkinter.Tk):
        """
        Setup a tkinter.Text object to make a string display for App class.
        """
        
        self.display = tkinter.Text(frame, font=frame.display_font, 
                                    bg=frame.color_frame_bg, 
                                    foreground=frame.color_frame_fg, height=3, 
                                    width=20)
        
        self.display['state'] = tkinter.DISABLED
        self.display.grid(row=0, columnspan=4)

    def update(self, _title):
        """
        Change the label from the last one char.
        """
        
        self.display['state'] = tkinter.NORMAL
        self.display.insert("end-1c", _title)
        self.display['state'] = tkinter.DISABLED

        self.display.update()

    def clear(self):
        """
        Fully clear the string of the display.
        """
        
        self.display['state'] = tkinter.NORMAL
        self.display.replace("1.0", "end-1c", "")
        self.display['state'] = tkinter.DISABLED

    def delete_char(self):
        """
        Clear the string char by char.
        """
        
        self.display['state'] = tkinter.NORMAL
        self.display.replace("end-2c", "end-1c", "")
        self.display['state'] = tkinter.DISABLED
