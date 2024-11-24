import tkinter as tk

class GraphicalInterface:
    def __init__(self):
        root = tk.Tk()

        root.title('Phaser Asset Importer')
        root.geometry("800x600")

        # Add a label widget
        label = tk.Label(root, text="Hello, Tkinter!")
        label.pack(pady=20)  # Add label to the window and set padding

        # Define a function to update the label text when the button is clicked 
        def on_button_click():
            label.config(text="Button clicked!")

        # Add a button widget
        button = tk.Button(root, text="Click me", command=on_button_click)
        button.pack()

        root.mainloop()