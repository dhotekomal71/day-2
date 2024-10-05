import tkinter as tk
import time

# Function to update the clock every second
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)

# Creating the main window
root = tk.Tk()
root.title("Digital Clock")

# Configuring the label for the clock
label = tk.Label(root, font=('Arial', 50), bg='black', fg='white')
label.pack(anchor='center')

# Start the clock update
update_clock()

# Run the application
root.mainloop()
