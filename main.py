import tkinter as tk
from tkinter import *
from TemperatureConverter import *

# app window configuration and UI
root = tk.Tk()
root.geometry('450x400+100+200')
root.title('UNIT CONVERTER')
root.configure(background='#09A3BA')
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

labelfont = ('Segoe UI', 56, 'bold')

title_label = tk.Label(root,
                       text='UNIT CONVERTER',
                       font = ("Segoe UI", 20, 'bold'),
                       justify = tk.CENTER,
                       bg = '#09a3ba',
                       fg = '#ffffff'
                       )

title_label.place(x=120,y=20)


quit_btn = tk.Button(None,
                text="QUIT",
                background='red',
                foreground="#FFFFFF",
                font = ("Segoe UI", 14, 'bold'),
                relief = tk.RAISED,
                bd=5,
                justify = tk.CENTER,
                highlightbackground = "red",
                overrelief = tk.GROOVE,
                activebackground = "green",
                activeforeground="blue",
                command=root.destroy
                ).place(x=340,y=340)

#TEMPERATURE CONVERTER WIDGET
temp_widget = tk.Button(root,
                text="Temperature converter",
                background='#ffffff',
                foreground="#09A3BA",
                font = ("Segoe UI", 14),
                relief = tk.RAISED,
                bd=3,
                justify = tk.CENTER,
                highlightbackground = "red",
                overrelief = tk.GROOVE,
                activebackground = "green",
                activeforeground="blue",
                command = TemperatureConverter
                ).place(x=40,y=90)

#ADD YOUR OWN WIDGETS HERE

root.mainloop()
