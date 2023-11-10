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
names = [entry.get("Name", "") for entry in data_from_file.values() if entry.get("Name")]

# Set the Matplotlib backend to "TkAgg"
matplotlib.use("TkAgg")

# Create a tkinter window
window = tkinter.Tk()
window.iconbitmap("./assets/sheet.ico")
window.minsize(830, 500)
window.geometry("+580+100")
window.title("Grades")
window.config(bg="#242324")
window.attributes('-alpha', 0.95)
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
        grade_label = tkinter.Label(grade_frame, text=f"{name}: {grade}%", bg="#2b2b2b", fg="white", font=("Poppins", 12))
        grade_label.pack(anchor="w", padx=5, pady=5)

# Create the Graph frame
Linear_graph_frame = tkinter.Frame(window, bg="#2b2b2b")
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
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
