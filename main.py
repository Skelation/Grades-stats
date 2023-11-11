import os
import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import customtkinter as ctk

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

class GradeGrapherApp:
    def __init__(self, master):
        self.master = master
        master.title("Grade Grapher")
        master.geometry("600x270")
        master.iconbitmap("./assets/sheet.ico")
        master.minsize(600, 270)
        master.maxsize(600, 270)

        self.setup_gui()

    def setup_gui(self):
        left_title_label = ttk.Label(
            master=self.master,
            text='Grade Grapher',
            font='poppins 25 ')
        left_title_label.configure(foreground='white', background='#242324')
        left_title_label.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        coffee_label = ttk.Label(
            master=self.master,
            text='Support us by buying us a coffee!',
            font=('poppins, 8')
        )
        coffee_label.configure(foreground='white', background='#242324')
        coffee_label.grid(row=0, column=1)

        name_label = ttk.Label(
            master=self.master,
            text='Input the name of your subject:',
            font='poppins 15'
        )
        name_label.configure(foreground='white', background='#242324')
        name_label.grid(row=1, column=0, padx=20, pady=10, sticky='w')

        self.name_entry = ctk.CTkEntry(self.master, justify="left")
        self.name_entry.grid(row=2, column=0, padx=20, pady=10, sticky='w')

        submission_label_name = tk.Label(self.master, text="")
        submission_label_name.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        submission_label_name.configure(foreground='white', background="#242324")

        grade_label = tk.Label(
            master=self.master,
            text='Input the grade of your test(%)',
            font='poppins 15'
        )
        grade_label.configure(foreground='white', background='#242324')
        grade_label.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.grade_entry = ctk.CTkEntry(self.master)
        self.grade_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        submission_label_grade = tk.Label(self.master, text="")
        submission_label_grade.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        submission_label_grade.configure(foreground="white", background="#242324")

        submit_button = ctk.CTkButton(self.master, text="Submit", command=self.submit_values)
        submit_button.grid(row=4, column=0, columnspan=3, pady=10)

        open_toplevel_button = ctk.CTkButton(self.master, text="Open Graph", command=self.open_toplevel, image=)
        open_toplevel_button.grid(row=4, column=1, columnspan=1, pady=10)

        self.master.configure(bg='#242324')

    def submit_values(self):
        name = self.name_entry.get()
        grade = self.grade_entry.get()
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
            self.master.destroy()
        else:
            print("Valid input must be an integer")

    def open_toplevel(self):
        ToplevelWindow(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    app = GradeGrapherApp(root)
    root.mainloop()
