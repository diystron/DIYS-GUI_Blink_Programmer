from tkinter import *
import serial.tools.list_ports

def menu_init():
    global root

    root =Tk()
    root.title ("DIYS - Blink Programmer")
    root.geometry("500x500")
    root.config(background="white")

    # show 

menu_init()


root.mainloop()
