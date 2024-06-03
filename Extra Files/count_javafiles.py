import os

def count_java_files(directory):
    """Count all .java files in the specified directory."""
    java_file_count = 0
    # List all files in the directory
    files = os.listdir(directory)
    
    # Count files that end with .java
    for file in files:
        if file.endswith('.java'):
            java_file_count += 1
            
    return java_file_count

# Specify the path to your destination folder
destination_folder = r'C:\Users\droid\Documents\Aplicaciones_Avanzadas\Proyecto\PlagiarismDetector\finalDataset\javafiles'

# Call the function and print the result
java_count = count_java_files(destination_folder)
print(f"There are {java_count} Java files in the directory.")