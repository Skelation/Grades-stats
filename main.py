import os, json, webbrowser
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib

class ToplevelWindow(tk.Toplevel):
    def __init__(self, window):

        # Load data from data.json
        with open("data.json", "r") as file:
            data_from_file = json.load(file)

        # Extract grades from the data
        grades = [int(entry.get("Grade", 0)) for entry in data_from_file.values() if entry.get("Grade")]
        names = [entry.get("Name", "") for entry in data_from_file.values() if entry.get("Name")]

        # Set the Matplotlib backend to "TkAgg"
        matplotlib.use("TkAgg")

        self.master = window
        # Create a tkinter window
        window = tk.Tk()
        window.iconbitmap("./assets/sheet.ico")
        window.minsize(830, 500)
        window.geometry("+580+100")
        window.title("Grades")
        window.config(bg="#242324")
        window.maxsize(830, 500)

        # Create the Grades Frame
        grade_frame = ctk.CTkScrollableFrame(window, fg_color="#2b2b2b", 
                                            orientation= "vertical", 
                                            scrollbar_button_color="#696968", 
                                            label_text="Grades", 
                                            label_font= ('Poppins bold', 20), 
                                            label_anchor="w", 
                                            label_text_color="white", 
                                            label_fg_color="#2b2b2b")
        grade_frame.grid(row=1, column=0, padx=10, sticky="nsew", pady=10)

        for key, entry in data_from_file.items():
            grade = entry.get("Grade")
            name = entry.get("Name")
            if grade:
                grade_label = tk.Label(grade_frame, text=f"{name}: {grade}%", bg="#2b2b2b", fg="white", font=("Poppins", 12))
                grade_label.pack(anchor="w", padx=5, pady=5)

        # Create the Graph frame
        Linear_graph_frame = tk.Frame(window, bg="#2b2b2b")
        Linear_graph_frame.grid(row=1, column=1, padx=10, sticky="nsew", pady= 10)

        # Set row and column weights to control resizing
        window.grid_rowconfigure(1, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # Create a line graph of the grades using Matplotlib
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.set_facecolor("#2b2b2b")
        ax.set_facecolor("#2b2b2b")
        ax.plot(range(1, len(grades) + 1), grades, marker='o', linestyle='-')

        # Set the color of x and y labels to white
        ax.set_xlabel("Grades", color = "white")
        ax.set_ylabel("Grade Value", color = "white")
        ax.set_title("Grades Overview", color = "white")
        ax.grid(True)

        # Set the color of tick labels on the x and y axes to white
        ax.tick_params(axis='x', labelcolor='white')
        ax.tick_params(axis='y', labelcolor='white')

        ax.grid(color='white')

        # Update the line and marker colors to make them more visible on a black background
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')

        # Annotate data points with names
        for i, name in enumerate(names):
            ax.annotate(name, (i + 1, grades[i]), xytext=(1, 5), textcoords='offset points', color="limegreen")

        # Embed the Matplotlib figure in the tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=Linear_graph_frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)

        # Bind the closing function to the window's close button
        window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # This function will be called when the window is closed
        self.master.quit()  # Quit the main loop
        self.master.destroy()

class GradeGrapherApp:
    def __init__(self, master):
        self.master = master
        master.title("Grade Grapher")
        master.geometry("600x270")
        master.iconbitmap("./assets/sheet.ico")
        master.minsize(600, 270)
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

        open_toplevel_button = ctk.CTkButton(self.master, command=self.open_toplevel, text="Open Graph")
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
