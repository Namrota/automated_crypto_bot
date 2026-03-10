'''
Main entry point of the application.

'''
from tkinter import *

root= Tk()
root.title("Cryptobot Application")
#--------------------- CONSTANTS----------------------
DEEP_TEAL= "#09637E"
TEAL= "#088395"
AQUA_GRAY= "#7AB2B2"
ICE_BLUE= "#EBF4F6"
#--------------------------------------------------
# Application aligment
root.update_idletasks()
width = 800
height = 800
sreen_width = root.winfo_screenwidth()
sreen_height = root.winfo_screenheight()
x = (sreen_width - width) // 2
y = (sreen_height - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")
root.config(padx=20, pady=20, bg=ICE_BLUE)
root.mainloop()