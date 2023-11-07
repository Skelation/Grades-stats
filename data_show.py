import os 
import json
import customtkinter as ctk
import tkinter

# Set the working directory to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Load data from data.json
with open("data.json", "r") as file:
    data_from_file = json.load(file)


#Ctk window
window = tkinter.Tk()
window.geometry("400x240")
window.title("Grades")
window.config(bg="#E7EFFA")

title_frame = ctk.CTkFrame(window)
title_frame.pack()
title_label = ctk.CTkLabel(title_frame, text="Grades", bg_color="#E7EFFA", font=("Poppins", 20))
title_label.pack(side= "left")

grade_frame = ctk.CTkFrame(window)
grade_frame.pack()

for key, entry in data_from_file.items():
    grade = entry.get("Grade")
    if grade:
        grade_label = ctk.CTkLabel(grade_frame, text=f"Grade {key}: {grade}", bg_color="#E7EFFA")
        grade_label.pack()

window.mainloop()