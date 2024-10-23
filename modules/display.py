# _*_ coding: utf8 _*_

"""
The calculator text presenter.
"""

import tkinter


class Display:
    def __init__(self, root: tkinter.Tk):
        """
        Setup a tkinter.Text object to make a string frame for App class.
        """
        
        self.frame = tkinter.Text(root, font=root.display_font, 
                                    bg=root.color_frame_bg, 
                                    foreground=root.color_frame_fg, height=3, 
                                    width=20)
        
        self.frame['state'] = tkinter.DISABLED
        self.frame.grid(row=0, columnspan=4)

    def update_string(self, _title):
        """
        Change the label from the last one char.
        """
        
        self.frame['state'] = tkinter.NORMAL
        self.frame.insert("end-1c", _title)
        self.frame['state'] = tkinter.DISABLED

        self.frame.update()

    def clear_frame(self):
        """
        Fully clear the string of the frame.
        """
        
        self.frame['state'] = tkinter.NORMAL
        self.frame.replace("1.0", "end-1c", "")
        self.frame['state'] = tkinter.DISABLED

    def delete_char(self):
        """
        Clear the string char by char.
        """
        
        self.frame['state'] = tkinter.NORMAL
        self.frame.replace("end-2c", "end-1c", "")
        self.frame['state'] = tkinter.DISABLED
