import os
import shutil

# Define the source and destination directories
source_directory = r'C:\Users\droid\Documents\Aplicaciones_Avanzadas\Proyecto\PlagiarismDetector\data\fire14-source-code-training-dataset\fire14-source-code-training-dataset\java'
destination_directory = r'C:\Users\droid\Documents\Aplicaciones_Avanzadas\Proyecto\PlagiarismDetector\finalDataset\javafiles'

# Ensure the destination directory exists, create if it doesn't
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Loop through the source directory to find all Java files
for filename in os.listdir(source_directory):
    if filename.endswith('.java'):  # Check if the file is a Java file
        source_file_path = os.path.join(source_directory, filename)
        destination_file_path = os.path.join(destination_directory, filename)
        
        # Move the file to the destination directory
        shutil.move(source_file_path, destination_file_path)

print("All Java files have been moved.")