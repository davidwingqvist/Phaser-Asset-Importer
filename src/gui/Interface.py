import tkinter as tk
from tkinter import filedialog
import os

class GraphicalInterface:
    def __init__(self):
        root = tk.Tk()
        self.inputFolder = ""
        self.outputFolder = ""
        self.outputFile = ""
        self.fileExtension = []

        root.title('Phaser Asset Importer')
        root.geometry("800x600")
        
        root.grid_rowconfigure(0, weight=0)
        root.grid_rowconfigure(1, weight=0)
        root.grid_rowconfigure(2, weight=0)
        root.grid_rowconfigure(3, uniform="equal")
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

        # Define a function to update the label text when the button is clicked 
        def on_button_input_folder_click():
            user_input = entry.get()  # Retrieve the text from the input field
            label.config(text=f"You entered: {user_input}")  # Display the entered text on the label
            # Function to open folder dialog and get folder path
        def open_folder_dialog(ouput, entry):  
            initial_dir = os.getcwd()  # Get the current working directory
            folder_path = filedialog.askdirectory(initialdir=initial_dir)
            if folder_path:  # If a folder was selected (path is not empty)
                entry.delete(0, tk.END)  # Clear any existing text in the entry field
                entry.insert(0, folder_path)  # Insert the selected folder path into the entry field
                output = folder_path
                #label.config(text=f"Current Folder: {output}")
                entry.config(bg="green")  # Reset to white if the input is filled

        # Add a label widget
        label = tk.Label(root, text="Enter Input Folder")
        label.grid(row=0, column=0, sticky="nsew")  # Position the label in the first row

        # Add an Entry widget for text input
        entry = tk.Entry(root, width=40)
        entry.grid(row=1, column=0, padx=10, sticky="ew")  # Position the input field in the second row, first column
        entry.config(bg="red")

        # Add a button widget to open the folder dialog
        button = tk.Button(root, text="Browse", command=lambda: open_folder_dialog(self.inputFolder, entry))
        button.grid(row=1, column=1, padx=10, sticky="ew")  # Use grid for the button
        
        outputFolderLabel = tk.Label(root, text="Enter Output Folder")
        outputFolderLabel.grid(row=3, column=0, sticky="nsew")
        
        outputEntry = tk.Entry(root, width=40)
        outputEntry.grid(row=4, column=0, padx=10, sticky="ew")  # Position the input field in the second row, first column
        outputEntry.config(bg="red")
        
        outputButton = tk.Button(root, text="Browse", command=lambda: open_folder_dialog(self.outputFolder, outputEntry))
        outputButton.grid(row=4, column=1, padx=10, sticky="ew")
        
        fileExtensionLabel = tk.Label(root, text="File Extension: ")
        fileExtensionLabel.grid(row=5, column=0)
        
        fileExtensionEntry = tk.Entry(root, width=40)
        fileExtensionEntry.grid(row=5, column=1)
        
        def add_file_extension():
            user_input = fileExtensionEntry.get()
            self.fileExtension.append(user_input)
            extensions_text = ", ".join(self.fileExtension)  # Join all extensions into a string
            fileExtensionLabel.config(text=f"File Extensions: {extensions_text}")  # Update the label
            fileExtensionEntry.delete(0, tk.END)  # Clear the input field
            
        def remove_file_extension():
            user_input = fileExtensionEntry.get()
            if user_input in self.fileExtension:
                self.fileExtension.remove(user_input)
                extensions_text = ", ".join(self.fileExtension)
                fileExtensionLabel.config(text=f"File Extensions: {extensions_text}")
                fileExtensionEntry.delete(0, tk.END)
        
        def clear_file_extension():
            self.fileExtension = []
            extensions_text = ", ".join(self.fileExtension)
            fileExtensionLabel.config(text=f"File Extensions: {extensions_text}")
            fileExtensionEntry.delete(0, tk.END)
                
        
        fileExtensionButton = tk.Button(root, text="add", command=add_file_extension)
        fileExtensionButton.grid(row=6, column=1, padx=(50, 0), sticky="w")
        
        fileExtensionRemoveButton = tk.Button(root, text="remove", command=remove_file_extension)
        fileExtensionRemoveButton.grid(row=6, column=1, padx=(150, 150), sticky="ew")
        
        fileExtensionRemoveAllButton = tk.Button(root, text="clear", command=clear_file_extension)
        fileExtensionRemoveAllButton.grid(row=6, column=1, padx=(0, 50), sticky="e")

        root.mainloop()