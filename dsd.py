import tkinter as tk
from PIL import Image, ImageTk

def rotate_image():
    # Load the image
    original_image = Image.open("src\\app\\assets\\images\\ship_flow.png")
    rotated_image = original_image.rotate(90)

    # Convert the rotated image to Tkinter format
    tk_image = ImageTk.PhotoImage(rotated_image)

    # Update the label with the rotated image
    label.config(image=tk_image)
    label.image = tk_image  # Keep a reference to avoid garbage collection

root = tk.Tk()
root.geometry("300x200")

# Load the initial image
initial_image = Image.open("src\\app\\assets\\images\\ship_flow.png")
tk_initial_image = ImageTk.PhotoImage(initial_image)

# Create Label with initial image
label = tk.Label(root, image=tk_initial_image)
label.pack()

# Button to rotate the image
rotate_button = tk.Button(root, text="Rotate Image", command=rotate_image)
rotate_button.pack()

root.mainloop()
