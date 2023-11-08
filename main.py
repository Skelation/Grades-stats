import os
import json
from datetime import datetime

# Set the working directory to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Get user input (To change to a custom tkinter GUI)
grade = input("What's your grade? ")
name = input("What's your name ? ")

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
    
