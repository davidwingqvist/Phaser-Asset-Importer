import os
import json

class Exporter:
    def __init__(self):
        self.data = {}
        self.ResetData()

    def ResetData(self):
        self.data = {
            "preload": {
                "files": []
            }
        }

    def ExportToJSON(self, interface):
        self.ResetData()

        # Ensure that fileExtension is a tuple of strings (e.g., ('.mp3', '.wav'))
        if isinstance(interface.fileExtension, str):
            self.formats = (interface.fileExtension,)  # Convert single string to a tuple
        else:
            self.formats = tuple(interface.fileExtension)  # Ensure it's a tuple if it's already a list

        self.inputFolder = interface.inputFolder
        self.outputFolder = interface.outputFolder
        self.outputFile = interface.outputFile

        print(interface.outputFolder)

        # Get all files that match the given extensions in the input folder
        file_names = [file for file in os.listdir(self.inputFolder) if file.endswith(self.formats)]
        
        # If no files found, log and return early
        if not file_names:
            print(f"No files found with the specified extensions {self.formats} in the input folder.")
            return

        # Get filenames without extension
        file_names_without_extension = [os.path.splitext(file)[0] for file in file_names]

        # Add file data to the dictionary
        for index, file in enumerate(file_names_without_extension):

            relative_path = os.path.relpath(file_names[index], self.inputFolder)
            
            # Prepend "assets/" to the relative path to ensure it's in the assets directory in the JSON
            # This ensures that the file is referenced from the 'assets/' directory regardless of its original location
            relative_path = os.path.join("assets", relative_path).replace("\\", "/")  # Use forward slashes for JSON

            self.data["preload"]["files"].append({
                "key": file,
                "path": relative_path
            })

        # Create the output folder if it doesn't exist
        os.makedirs(self.outputFolder, exist_ok=True)

        # Define the full path to save the JSON file
        output_file_path = os.path.join(self.outputFolder, self.outputFile)

        # Write the JSON data to the file
        with open(output_file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

        print(f"JSON data exported successfully to {output_file_path}")   