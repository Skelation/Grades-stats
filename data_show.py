import os
import json
import tkinter
import matplotlib
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from mpldatacursor import datacursor

def on_closing():
    # This function will be called when the window is closed
    window.quit()  # Quit the main loop
    window.destroy()

# Set the working directory to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Load data from data.json
with open("data.json", "r") as file:
    data_from_file = json.load(file)

# Extract grades from the data
grades = [int(entry.get("Grade", 0)) for entry in data_from_file.values() if entry.get("Grade")]
names = [entry.get("Name", "") for entry in data_from_file.values() if entry.get("Name")]

# Set the Matplotlib backend to "TkAgg"
matplotlib.use("TkAgg")

# Create a tkinter window
window = tkinter.Tk()
window.minsize(400, 400)
window.geometry("+580+100")
window.title("Grades")
window.config(bg="#242324")

# Create the title frame using the grid manager
title_label = tkinter.Label(window, text="Grades", bg="#242324", fg="white", font=("Poppins", 20))
title_label.grid(row=0, column=0, sticky="w", padx=10, pady= 10)

# Create the Grades Frame
grade_frame = ctk.CTkScrollableFrame(window, fg_color="#2b2b2b", orientation= "vertical", scrollbar_button_color="#696968")
grade_frame.grid(row=1, column=0, padx=10, sticky="nsew", pady=10)

for key, entry in data_from_file.items():
    grade = entry.get("Grade")
    name = entry.get("Name")
    if grade:
        grade_label = tkinter.Label(grade_frame, text=f"{name}: {grade}%", bg="#2b2b2b", fg="white", font=("Poppins", 12))
        grade_label.pack(anchor="w", padx=5, pady=5)

# Create the Graph frame
graph_frame = tkinter.Frame(window, bg="#2b2b2b")
graph_frame.grid(row=1, column=1, padx=10, sticky="nsew")

# Set row and column weights to control resizing
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Create a line graph of the grades using Matplotlib
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(range(1, len(grades) + 1), grades, marker='o', linestyle='-')
ax.set_xlabel("Grades")
ax.set_ylabel("Grade Value")
ax.set_title("Grades Overview")
ax.grid(True)

# Annotate data points with names
for i, name in enumerate(names):
    ax.annotate(name, (i + 1, grades[i]), xytext=(1, 5), textcoords='offset points')

# Embed the Matplotlib figure in the tkinter window
canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_frame)
canvas.get_tk_widget().pack(pady=10)

# Bind the closing function to the window's close button
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
