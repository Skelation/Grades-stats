import tkinter as tk
import tkinter as ttk
from tkinter import *


def submit_text1():
    submission_label_name.config(text=" Name Submitted! ")
    

def submit_text2():
    submission_label_grade.config(text=" Grade Submitted! ")
    

def validate_input(value, action_type):
        if action_type == '1':  # Insert
            return value.isdigit()
        return True
    

    
#window

window = tk.Tk()
window.title("Grade Grapher")
window.geometry("830x500")
window.iconbitmap("./assets/noun-grade-sheet-3239955 (1).ico")

validation = (window.register(validate_input), '%P', '%d')

#Title/Main header

left_title_label = ttk.Label(
    master = window,   
    text =  'Grade Grapher',
    font = 'poppins 25 ')
left_title_label.configure(fg = 'white', bg='#242324')#Change the foreground and the background of the title_label

left_title_label.pack(anchor='w', padx = 10, pady = 10)

right_title_label = ttk.Label(
    master = window,
    text = 'Support us by buying us a coffee!',
    font = ('poppins, 8')
)
right_title_label.configure(fg='white', bg='#242324')
right_title_label.pack(anchor='ne', padx = 10, pady = 10)
right_title_label.place(relx=1, rely=0, anchor='ne')

#text box for Name input

name_label = ttk.Label(
    master = window,
    text = 'Input the name of your subject:',
    font = 'poppins 15'
)
name_label.configure(fg='white',bg='#242324' )
name_label.place(x ='60', y = '200')

entry = tk.Entry(window, width=30, justify="left")
entry.pack(pady=10)

entry.place(x="70", y="250")

submit_button = tk.Button(window, text="Submit Name", command= submit_text1 )
submit_button.pack(pady=10)

submit_button.place(x='280', y='248')

submission_label_name = tk.Label(window, text="")
submission_label_name.pack()
submission_label_name.place(x = '70', y = '290')
submission_label_name.configure(fg = 'white', bg = "#242324" )

#Text box for Grade Input

grade_label = ttk.Label(
    master = window,
    text = 'Input the grade of your test(%)',
    font = 'poppins 15'
)
grade_label.configure(fg = 'white', bg = '#242324')
grade_label.place(x = '450', y = '202')

entry_2 = tk.Entry(window, width=30, justify="right", validate="key", validatecommand=validation)
entry_2.pack(pady=10)
entry_2.place(x = '465', y = '252')

submit_button_2 = tk.Button(window, text = 'Submit Grade', command= submit_text2 )
submit_button_2.pack(pady=10)

submit_button_2.place(x = '680', y = '248')

submission_label_grade = tk.Label(window, text="")
submission_label_grade.pack()
submission_label_grade.place(x = '466', y = '290')
submission_label_grade.configure(fg = "white", bg = "#242324")

#Canvas Widget for the rectangles





#Change the background color of the window

window.configure(bg='#242324')

#To make the GUI run/loop

window.mainloop()