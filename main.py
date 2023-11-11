import os
import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import customtkinter as ctk


def submit_values():
    name = name_entry.get()
    grade = grade_entry.get()
    if grade.isnumeric() == True:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_directory)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        data = {}  # Initialize data as an empty dictionary

        if os.path.exists("data.json"):
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except json.decoder.JSONDecodeError:
                # Handle the case where the file is empty or not valid JSON
                pass

        next_key = str(len(data) + 1)

        json_input = {
            next_key: {
                "Grade": grade,
                "Timestamp": timestamp,
                "Name": name
            }
        }

        data.update(json_input)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=1)
        window.destroy()
    else:
        print("Valid input must be an integer")


window = tk.Tk()
window.title("Grade Grapher")
window.geometry("600x270")
window.iconbitmap("./assets/sheet.ico")
window.minsize(600, 270)
window.maxsize(600, 270)

left_title_label = ttk.Label(
    master=window,
    text='Grade Grapher',
    font='poppins 25 ')
left_title_label.configure(foreground='white', background='#242324')
left_title_label.grid(row=0, column=0, padx=20, pady=10, sticky='w')

coffee_label = ttk.Label(
    master=window,
    text='Support us by buying us a coffee!',
    font=('poppins, 8')
)
coffee_label.configure(foreground='white', background='#242324')
coffee_label.grid(row=0, column=1)

name_label = ttk.Label(
    master=window,
    text='Input the name of your subject:',
    font='poppins 15'
)
name_label.configure(foreground='white', background='#242324')
name_label.grid(row=1, column=0, padx=20, pady=10, sticky='w')

name_entry = ctk.CTkEntry(window, justify="left")
name_entry.grid(row=2, column=0, padx=20, pady=10, sticky='w')

submission_label_name = tk.Label(window, text="")
submission_label_name.grid(row=3, column=0, padx=10, pady=10, sticky='w')
submission_label_name.configure(foreground='white', background="#242324")

grade_label = tk.Label(
    master=window,
    text='Input the grade of your test(%)',
    font='poppins 15'
)
grade_label.configure(foreground='white', background='#242324')
grade_label.grid(row=1, column=1, padx=10, pady=10, sticky='w')

grade_entry = ctk.CTkEntry(window, )
grade_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

submission_label_grade = tk.Label(window, text="")
submission_label_grade.grid(row=3, column=1, padx=10, pady=10, sticky='w')
submission_label_grade.configure(foreground="white", background="#242324")

submit_button = ctk.CTkButton(window, text="Submit", command=submit_values)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

window.configure(bg='#242324')
window.mainloop()
