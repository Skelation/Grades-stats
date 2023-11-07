import os
import json
import tkinter
import matplotlib
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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

# Set the Matplotlib backend to "TkAgg"
matplotlib.use("TkAgg")

# Create a tkinter window
window = tkinter.Tk()
window.geometry("600x400")
window.title("Grades")
window.config(bg="#E7EFFA")

# Create the title frame
title_frame = ctk.CTkFrame(window, bg_color="#E7EFFA")
title_frame.pack()
title_label = ctk.CTkLabel(title_frame, text="Grades", bg_color="#E7EFFA", font=("Poppins", 20))
title_label.pack(side="left")

grade_frame = ctk.CTkFrame(window)
grade_frame.pack()

for key, entry in data_from_file.items():
    grade = entry.get("Grade")
    if grade:
        grade_label = ctk.CTkLabel(grade_frame, text=f"Grade {key}: {grade}", bg_color="#E7EFFA")
        grade_label.pack()

# Create the frame for the graph
graph_frame = tkinter.Frame(window, bg="white")
graph_frame.pack()

# Create a line graph of the grades using Matplotlib
plt.figure(figsize=(6, 4))
plt.plot(range(1, len(grades) + 1), grades, marker='o', linestyle='-')
plt.xlabel("Grades")
plt.ylabel("Grade Value")
plt.title("Grades Overview")
plt.grid(True)

# Embed the Matplotlib figure in the tkinter window
canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_frame)
canvas.get_tk_widget().pack()

# Bind the closing function to the window's close button
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
