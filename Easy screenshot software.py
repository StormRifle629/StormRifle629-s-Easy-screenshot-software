import pyautogui
import time
from tkinter import*
import tkinter as tk

def screenshot():
    print("Button was clicked!")
    # Capture the screen
    screenshot = pyautogui.screenshot()
    # Save the screenshot to a file
    screenshot.save('screenshot.png')


# Create the main window
window = tk.Tk()

# Create a button
button = tk.Button(text="Click me", command=screenshot)

# Create the main window
root = tk.Tk()

def open_new_window():
    # Create a new top-level window
    new_window = tk.Toplevel()
    # Add a label to the new window
    tk.Label(new_window, text="This is a new window").pack()
    

# Add a button to the main window
tk.Button(root, text="Open new window", command=open_new_window).pack()
    

# Pack the button (display it)
button.pack()
import tkinter as tk

# Create the main window
root = tk.Tk()



# Change the window title
window.wm_title("StormRifle629's easy screenshot software!")


# Run the Tkinter event loop
window.mainloop()

canvas.create_window(110, 60,)
root.mainloop()



# Run the main loop
root.mainloop()

