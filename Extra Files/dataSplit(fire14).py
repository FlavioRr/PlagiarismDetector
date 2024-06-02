import os
import shutil

# Ruta de la carpeta de datos y archivo SOCO14-java.qrel
data_folder = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\data\fire14-source-code-training-dataset\fire14-source-code-training-dataset'
qrel_file = os.path.join(data_folder, 'SOCO14-java.qrel')

# Carpeta de destino para archivos sin plagio y con plagio
noplag_folder = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\noplag'
plagio_folder = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\plagio'

# Crear carpetas de destino si no existen
if not os.path.exists(noplag_folder):
    os.makedirs(noplag_folder)
if not os.path.exists(plagio_folder):
    os.makedirs(plagio_folder)

# Leer pares de archivos de SOCO14-java.qrel
plagiarism_pairs = set()
with open(qrel_file, 'r') as f:
    for line in f:
        pairs = line.strip().split()
        for pair in pairs:
            plagiarism_pairs.add(pair)

# Obtener lista de archivos .java
java_files_folder = os.path.join(data_folder, 'java')
java_files = [file for file in os.listdir(java_files_folder) if file.endswith('.java')]

# Iterar sobre los archivos .java y moverlos según la presencia en los pares de plagio
for java_file in java_files:
    file_number = java_file.split('.')[0]
    found = False
    for pair in plagiarism_pairs:
        if file_number in pair:
            found = True
            break
    if found:
        shutil.move(os.path.join(java_files_folder, java_file), os.path.join(plagio_folder, java_file))
    else:
        shutil.move(os.path.join(java_files_folder, java_file), os.path.join(noplag_folder, java_file))

print("Proceso completado.")
