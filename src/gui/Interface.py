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
        label.place(x=100, y=50)  # Position the label in the first row

        # Add an Entry widget for text input
        entry = tk.Entry(root, width=40)
        entry.place(x=10, y=100)  # Position the input field in the second row, first column
        entry.config(bg="red")

        # Add a button widget to open the folder dialog
        button = tk.Button(root, text="Browse", command=lambda: open_folder_dialog(entry))
        button.place(x=260, y=97)  # Use grid for the button
        
        outputFolderLabel = tk.Label(root, text="Enter Output Folder", bg="darkgray")
        outputFolderLabel.place(x=530, y=50)
        
        outputEntry = tk.Entry(root, width=40)
        outputEntry.place(x=450, y=100)  # Output directory entry
        outputEntry.config(bg="red")
        
        outputButton = tk.Button(root, text="Browse", command=lambda: open_folder_dialog(outputEntry))
        outputButton.place(x=700, y=97)

        outputFileLabel = tk.Label(root, text="Output File Name:", bg="darkgray")
        outputFileLabel.place(x=500, y=150)

        outputFileEntry = tk.Entry(root, width=20)
        outputFileEntry.place(x=500, y=200)
        outputFileEntry.config(bg="red")

        def select_output_file_name():
            self.outputFile = outputFileEntry.get()
            if self.outputFile:
                outputFileEntry.config(bg="green")

        outputFileButton = tk.Button(root, text="Select", width=10, command=select_output_file_name)
        outputFileButton.place(x=650, y=197)

        fileExtensionLabel = tk.Label(root, text="File Extensions: ", bg="darkgray")
        fileExtensionLabel.place(x=100, y=150)
        
        fileExtensionEntry = tk.Entry(root, width=40)
        fileExtensionEntry.place(x=25, y=200)
        
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
                
        
        fileExtensionButton = tk.Button(root, text="Add", command=add_file_extension, width=5)
        fileExtensionButton.place(x=50, y=225)
        
        fileExtensionRemoveButton = tk.Button(root, text="remove", command=remove_file_extension, width=10)
        fileExtensionRemoveButton.place(x=110, y=225)
        
        fileExtensionRemoveAllButton = tk.Button(root, text="clear", command=clear_file_extension, width=5)
        fileExtensionRemoveAllButton.place(x=200, y=225)

        soundButton = tk.Button(root, text="Sound", width=10, command=lambda: self.UpdateContentFrame("sound"))
        soundButton.place(x=100 + (600 / 4) - ((10 * 5) / 2), y=275)

        textureButton = tk.Button(root, text="Texture", width=10, command=lambda: self.UpdateContentFrame("texture"))
        textureButton.place(x=100 + ((600 / 4) * 2) - ((10 * 7) / 2), y=275)

        animationButton = tk.Button(root, text="Animation", width=10, command=lambda: self.UpdateContentFrame("animation"))
        animationButton.place(x=100 + ((600 / 4) * 3) - ((10 * 9) / 2), y=275)

        self.content_frame = tk.Frame(root, bg="lightgray", width=600, height=300)
        self.content_frame.place(x=100, y=300)
        self.content_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its children

        exportButton = tk.Button(root, text="Export", width=20, command=self.ExportToJSON)
        exportButton.place(x=400 - ((20 * 6) / 2), y=570)

        root.mainloop()

    def UpdateContentFrame(self, type):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if type == "sound":
            label = tk.Label(self.content_frame, text="Sound Exporter", font=("Arial", 11), bg="lightgray")
            label.pack()
            texture = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "../../ui/btn_icon_megaphone.png"))
            imageLabel = tk.Label(self.content_frame, image=texture, bg="darkgray", borderwidth=2)
            imageLabel.place(x=500, y=15)
            self.texture = texture

        if type == "texture":
            label = tk.Label(self.content_frame, text="Texture Exporter", font=("Arial", 11), bg="lightgray")
            label.pack()
            texture = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "../../ui/btn_icon_photo.png"))
            imageLabel = tk.Label(self.content_frame, image=texture, bg="darkgray", borderwidth=2)
            imageLabel.place(x=500, y=15)
            self.texture = texture

        if type == "animation":
            label = tk.Label(self.content_frame, text="Animation Exporter", font=("Arial", 11), bg="lightgray")
            label.pack()
            texture = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "../../ui/btn_icon_layout.png"))
            imageLabel = tk.Label(self.content_frame, image=texture, bg="darkgray", borderwidth=2)
            imageLabel.place(x=500, y=15)
            self.texture = texture

    def ExportToJSON(self):
        pass
        