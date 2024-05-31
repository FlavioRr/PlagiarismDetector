import os
import random
import shutil

# Rutas de las carpetas de origen y destino
plagio_folder = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\plagio'
noplag_folder = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\noplag'

data_split_folder = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\data_split'

# Crear carpeta de destino si no existe
if not os.path.exists(data_split_folder):
    os.makedirs(data_split_folder)

# Crear subcarpetas para train, test y validation
for folder in ['train', 'test', 'validation']:
    folder_path = os.path.join(data_split_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for category in ['plagio', 'noplag']:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

# Obtener lista de archivos de plagio y no plagio
plagio_files = os.listdir(plagio_folder)
noplag_files = os.listdir(noplag_folder)

# Mezclar los archivos para una selección aleatoria
random.shuffle(plagio_files)
random.shuffle(noplag_files)

# Calcular el tamaño de los conjuntos de train, test y validation
total_plagio = len(plagio_files)
total_noplag = len(noplag_files)

train_size = int(0.7 * total_plagio)
test_size = int(0.2 * total_plagio)
valid_size = total_plagio - train_size - test_size

# Mover los archivos de plagio al conjunto de train
for file in plagio_files[:train_size]:
    shutil.move(os.path.join(plagio_folder, file), os.path.join(data_split_folder, 'train', 'plagio', file))

# Mover los archivos de plagio al conjunto de test
for file in plagio_files[train_size:train_size + test_size]:
    shutil.move(os.path.join(plagio_folder, file), os.path.join(data_split_folder, 'test', 'plagio', file))

# Mover los archivos de plagio al conjunto de validation
for file in plagio_files[train_size + test_size:]:
    shutil.move(os.path.join(plagio_folder, file), os.path.join(data_split_folder, 'validation', 'plagio', file))

# Mover los archivos de no plagio al conjunto de train
for file in noplag_files[:train_size]:
    shutil.move(os.path.join(noplag_folder, file), os.path.join(data_split_folder, 'train', 'noplag', file))

# Mover los archivos de no plagio al conjunto de test
for file in noplag_files[train_size:train_size + test_size]:
    shutil.move(os.path.join(noplag_folder, file), os.path.join(data_split_folder, 'test', 'noplag', file))

# Mover los archivos de no plagio al conjunto de validation
for file in noplag_files[train_size + test_size:]:
    shutil.move(os.path.join(noplag_folder, file), os.path.join(data_split_folder, 'validation', 'noplag', file))

print("Proceso completado.")
