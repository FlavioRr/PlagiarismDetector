import os

# Define the paths to the directories
plagio_dir = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\plagio'
noplag_dir = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\noplag'

def count_files(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

# Count files in each directory
plagio_count = count_files(plagio_dir)
noplag_count = count_files(noplag_dir)

print(f'Cantidad de archivos en "plagio": {plagio_count}')
print(f'Cantidad de archivos en "noplag": {noplag_count}')
