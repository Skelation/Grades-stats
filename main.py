import os
import json
from datetime import datetime
import tkinter as tk
import tkinter as ttk
from tkinter import *
from PIL import Image, ImageTk


def validate_input(value, action_type):
    if action_type == '1':  # Insert
        return value.isdigit()
    return True


def submit_values():
    name = name_entry.get()
    grade = grade_entry.get()

    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)
    # Generate a timestamp to use as a unique identifier
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Check if the JSON file exists
    if os.path.exists("data.json"):
        # If the file exists, load the existing data
        with open("data.json", "r") as file:
            data = json.load(file)
    else:
        # If the file doesn't exist, initialize an empty dictionary
        data = {

        }

    # Count the existing entries and assign the next integer key
    next_key = str(len(data) + 1)

    # Define the new data entry with the next integer key
    json_input = {
        next_key: {
            "Grade": grade,
            "Timestamp": timestamp,
            "Name": name
        }
    }

    # Add the new data entry to the dictionary
    data.update(json_input)

    # Write the updated data dictionary to the JSON file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=1)
    window.destroy()


# window
window = tk.Tk()
window.title("Grade Grapher")
window.geometry("830x500")
window.iconbitmap("./assets/sheet.ico")

validation = (window.register(validate_input), '%P', '%d')

# Title/Main header
left_title_label = ttk.Label(
    master=window,
    text='Grade Grapher',
    font='poppins 25 ')

# Change the foreground and the background of the title_label
left_title_label.configure(fg='white', bg='#242324')

left_title_label.pack(anchor='w', padx=10, pady=10)

coffee_label = ttk.Label(
    master=window,
    text='Support us by buying us a coffee!',
    font=('poppins, 8')
)
coffee_label.configure(fg='white', bg='#242324')
coffee_label.pack(anchor='ne', padx=10, pady=10)
coffee_label.place(relx=1, rely=0, anchor='ne')


# text box for Name input
name_label = ttk.Label(
    master=window,
    text='Input the name of your subject:',
    font='poppins 15'
)
name_label.configure(fg='white', bg='#242324')
name_label.place(x='60', y='200')

name_entry = tk.Entry(window, width=30, justify="left")
name_entry.pack(pady=10)

name_entry.place(x="70", y="250")

submission_label_name = tk.Label(window, text="")
submission_label_name.pack()
submission_label_name.place(x='70', y='290')
submission_label_name.configure(fg='white', bg="#242324")

# ext box for Grade Input
grade_label = ttk.Label(
    master=window,
    text='Input the grade of your test(%)',
    font='poppins 15'
)
grade_label.configure(fg='white', bg='#242324')
grade_label.place(x='450', y='202')

grade_entry = tk.Entry(window, width=30, justify="right",
                       validate="key", validatecommand=validation)
grade_entry.pack(pady=10)
grade_entry.place(x='465', y='252')

submission_label_grade = tk.Label(window, text="")
submission_label_grade.pack()
submission_label_grade.place(x='466', y='290')
submission_label_grade.configure(fg="white", bg="#242324")

# Submit button
submit_button = ttk.Button(window, text="Submit", command=submit_values)
submit_button.place(x='320', y='300')

# Change the background color of the window
window.configure(bg='#242324')

# To make the GUI run/loop
window.mainloop()
