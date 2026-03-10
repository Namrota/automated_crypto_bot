'''
Main entry point of the application.
1. Aligning the application to the center of the screen.
2. Setting the background color of the application.
3. Importing logging built-in module for monitoring the application and debugging purposes.
'''
from tkinter import *
import logging
import os
import sys

#---------------------------------------------------------

# Get the directory where the script is located
# PyInstaller creates a temp folder and stores path in _MEIPASS
if getattr(sys, 'frozen', False):
    SCRIPT_DIR = sys._MEIPASS
else:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


#--------------------- CONSTANTS ----------------------------
DEEP_TEAL= "#09637E"
TEAL= "#088395"
AQUA_GRAY= "#7AB2B2"
ICE_BLUE= "#EBF4F6"
#------------------------------------------------------------

#--------------------- LOGGING CONFIGURATION ----------------

formatter = logging.Formatter("%(asctime)s - %(levelname)s :: %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("application.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG,  handlers=[stream_handler, file_handler])
logger = logging.getLogger()


""" print("*" * 50)
logger.info("Application started successfully.")
logger.debug("Debugging information: Application is running in debug mode.")
logger.warning("Warning: This is a warning message.")
logger.error("Error: This is an error message.")
logger.critical("Critical: This is a critical message.")
print("*" * 50) """



if __name__ == "__main__":
    root= Tk()
    root.title("Cryptobot Application")
    # ----------------- ALIGNING THE APPLICATION -----------------
    root.update_idletasks()
    width = 800
    height = 800
    sreen_width = root.winfo_screenwidth()
    sreen_height = root.winfo_screenheight()
    x = (sreen_width - width) // 2
    y = (sreen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.config(padx=20, pady=20, bg=ICE_BLUE)
    #------------------------------------------------------------
    root.mainloop()