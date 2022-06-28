
#Import the required libraries
from tkinter import *
import tkinter as tk
from tkinter import Label 
import sys
 

def link():
   print("Loading.....")
   print("Directing to Main Menu")
   

   
#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of the Tkinter library
win.geometry("850x530")
win.attributes("-fullscreen", True)

label = Label(win, text="Multiple Choice  Quiz",
                      width=80, height=2, bg="#512E5F", fg="white", font=("Ariel", 50, "bold"))

label.pack(pady= 40)

#Add Menu
popup = Menu(win, tearoff=0)

def menu_popup(event):
   # display the popup menu
   try:
      popup.tk_popup(event.x_root, event.y_root, 0)
   finally:
      #Release the grab
      popup.grab_release()   
    


button = tk.Button(win, text="Start", bg="#512E5F", command=win.destroy, width = 20,  fg="white", font=('Ariel', 45,))
button.place(relx=0.25, rely=0.35)


button_2 = tk.Button(win, text="Quit", bg="#512E5F", command=quit, width = 20, fg="white",font=('Ariel', 45))
button_2.place(relx=0.25, rely=0.65)

def quit():
   sys.exit()

mainloop()




