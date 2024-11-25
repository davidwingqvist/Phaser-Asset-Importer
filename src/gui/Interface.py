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
        root.resizable(False, False)
        root.config(bg="darkgray")
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1, uniform="equal")
        root.grid_rowconfigure(2, weight=1)
        root.grid_rowconfigure(3, uniform="equal")
        root.grid_columnconfigure(0, weight=1, uniform="equal")
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)  # Adjust column 0
        root.grid_rowconfigure(9, weight=1)
        root.grid_rowconfigure(10, weight=0)   # Adjust row 10

        # Function to open folder dialog and get folder path
        def open_folder_dialog(entry):  
            initial_dir = os.getcwd()  # Get the current working directory
            folder_path = filedialog.askdirectory(initialdir=initial_dir)
            if folder_path:  # If a folder was selected (path is not empty)
                entry.delete(0, tk.END)  # Clear any existing text in the entry field
                entry.insert(0, folder_path)  # Insert the selected folder path into the entry field
                entry.config(bg="green")  # Reset to white if the input is filled

        # Add a label widget
        label = tk.Label(root, text="Enter Input Folder", bg="darkgray")
        label.grid(row=0, column=0, sticky="nsew")  # Position the label in the first row

        # Add an Entry widget for text input
        entry = tk.Entry(root, width=40)
        entry.grid(row=1, column=0, padx=10, sticky="ew")  # Position the input field in the second row, first column
        entry.config(bg="red")

        # Add a button widget to open the folder dialog
        button = tk.Button(root, text="Browse", command=lambda: open_folder_dialog(entry))
        button.grid(row=1, column=1, padx=10, sticky="ew")  # Use grid for the button
        
        outputFolderLabel = tk.Label(root, text="Enter Output Folder", bg="darkgray")
        outputFolderLabel.grid(row=3, column=0, sticky="nsew")
        
        outputEntry = tk.Entry(root, width=40)
        outputEntry.grid(row=4, column=0, padx=10, sticky="ew")  # Output directory entry
        outputEntry.config(bg="red")
        
        outputButton = tk.Button(root, text="Browse", command=lambda: open_folder_dialog(outputEntry))
        outputButton.grid(row=4, column=1, padx=10, sticky="ew")

        outputFileLabel = tk.Label(root, text="Output File Name:", bg="darkgray")
        outputFileLabel.grid(row=5, column=0, padx=(10, 0), sticky="w")

        outputFileEntry = tk.Entry(root, width=20)
        outputFileEntry.grid(row=5, column=0, padx=(0, 115), sticky="e")
        outputFileEntry.config(bg="red")

        def select_output_file_name():
            self.outputFile = outputFileEntry.get()
            if self.outputFile:
                outputFileEntry.config(bg="green")

        outputFileButton = tk.Button(root, text="Select", width=10, command=select_output_file_name)
        outputFileButton.grid(row=5, column=0, padx=(50, 0), sticky="e")

        fileExtensionLabel = tk.Label(root, text="File Extension: ", bg="darkgray")
        fileExtensionLabel.grid(row=6, column=0)
        
        fileExtensionEntry = tk.Entry(root, width=40)
        fileExtensionEntry.grid(row=6, column=1)
        
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
        fileExtensionButton.grid(row=7, column=1, padx=(50, 0), sticky="w")
        
        fileExtensionRemoveButton = tk.Button(root, text="remove", command=remove_file_extension)
        fileExtensionRemoveButton.grid(row=7, column=1, padx=(150, 150), sticky="ew")
        
        fileExtensionRemoveAllButton = tk.Button(root, text="clear", command=clear_file_extension)
        fileExtensionRemoveAllButton.grid(row=7, column=1, padx=(0, 50), sticky="e")

        soundButton = tk.Button(root, text="Sound", width=10, command=lambda: self.UpdateContentFrame("sound"))
        soundButton.grid(column=0, row=9, sticky="w", padx=(0, 100))

        textureButton = tk.Button(root, text="Texture", width=10, command=lambda: self.UpdateContentFrame("texture"))
        textureButton.grid(column=0, row=9, sticky="ew", padx=(125, 125))

        animationButton = tk.Button(root, text="Animation", width=10, command=lambda: self.UpdateContentFrame("animation"))
        animationButton.grid(column=0, row=9, sticky="e", padx=(100, 0))

        self.content_frame = tk.Frame(root, bg="lightgray", width=400, height=300)
        self.content_frame.grid(column=0, row=10, padx=(0, 0), pady=(0, 50), sticky="nsew")
        self.content_frame.pack_propagate(False)

        exportButton = tk.Button(root, text="Export", width=20, command=self.ExportToJSON)
        exportButton.grid(pady=(0, 25))

        root.mainloop()

    def UpdateContentFrame(self, type):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if type == "sound":
            label = tk.Label(self.content_frame, text="Sound Exporter", font=("Arial", 11), bg="lightgray")
            label.pack()

        if type == "texture":
            label = tk.Label(self.content_frame, text="Texture Exporter", font=("Arial", 11), bg="lightgray")
            label.pack()

        if type == "animation":
            label = tk.Label(self.content_frame, text="Animation Exporter", font=("Arial", 11), bg="lightgray")
            label.pack()

    def ExportToJSON(self):
        pass
        