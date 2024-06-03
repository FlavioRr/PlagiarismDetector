import os
import shutil

# Define the base directory where the version_2 folder is located
base_directory = r'C:\Users\droid\Documents\Aplicaciones_Avanzadas\Proyecto\PlagiarismDetector\data\conplag_version_2\versions\version_2'

# Define the destination directory where all Java files will be moved
destination_directory = r'C:\Users\droid\Documents\Aplicaciones_Avanzadas\Proyecto\PlagiarismDetector\finalDataset\javafiles'

# Ensure the destination directory exists, create if it doesn't
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Walk through the directory structure
for root, dirs, files in os.walk(base_directory):
    for file in files:
        if file.endswith('.java'):  # Check if the file is a Java file
            current_file_path = os.path.join(root, file)
            new_file_path = os.path.join(destination_directory, file)
            
            # Check if the file already exists in the destination directory
            if not os.path.exists(new_file_path):
                shutil.move(current_file_path, new_file_path)  # Move the file
            else:
                print(f"File {file} already exists in the destination directory.")

print("All Java files have been moved.")