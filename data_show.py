import os
import json
import tkinter
import matplotlib
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
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
window.minsize(800, 800)
window.geometry("+580+100")
window.title("Grades")
window.config(bg="#E7EFFA")

# Create the title frame
title_frame = ctk.CTkFrame(window, bg_color="#E7EFFA")
title_frame.pack()
title_label = ctk.CTkLabel(title_frame, text="Grades", bg_color="#E7EFFA", font=("Poppins", 20))
title_label.pack(side="left")

grade_frame = ctk.CTkFrame(window, bg_color="#E7EFFA")
grade_frame.pack()

for key, entry in data_from_file.items():
    grade = entry.get("Grade")
    name = entry.get("Name")
    if grade:
        grade_label = ctk.CTkLabel(grade_frame, text=f"{name}: {grade}%", bg_color="#E7EFFA")
        grade_label.pack()

# Create the frame for the graph
graph_frame = tkinter.Frame(window, bg="white")
graph_frame.pack()

# Create a line graph of the grades using Matplotlib
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(range(1, len(grades) + 1), grades, marker='o', linestyle='-')
ax.set_xlabel("Grades")
ax.set_ylabel("Grade Value")
ax.set_title("Grades Overview")
ax.grid(True)

# Annotate data points with names
for i, name in enumerate(names):
    ax.annotate(name, (i + 1, grades[i]), xytext=(1,5), textcoords='offset points')

# Embed the Matplotlib figure in the tkinter window
canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_frame)
canvas.get_tk_widget().pack()

# Bind the closing function to the window's close button
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
