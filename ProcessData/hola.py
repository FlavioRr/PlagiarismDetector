import os

data_split_folder = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\data_split'

# Obtener lista de carpetas de train, test y validation
train_folder = os.path.join(data_split_folder, 'train')
test_folder = os.path.join(data_split_folder, 'test')
valid_folder = os.path.join(data_split_folder, 'validation')

# Obtener el número de archivos en cada carpeta
train_plagio_files = os.listdir(os.path.join(train_folder, 'plagio'))
train_noplag_files = os.listdir(os.path.join(train_folder, 'noplag'))
test_plagio_files = os.listdir(os.path.join(test_folder, 'plagio'))
test_noplag_files = os.listdir(os.path.join(test_folder, 'noplag'))
valid_plagio_files = os.listdir(os.path.join(valid_folder, 'plagio'))
valid_noplag_files = os.listdir(os.path.join(valid_folder, 'noplag'))

# Contar el número de archivos en cada carpeta
train_plagio_count = len(train_plagio_files)
train_noplag_count = len(train_noplag_files)
test_plagio_count = len(test_plagio_files)
test_noplag_count = len(test_noplag_files)
valid_plagio_count = len(valid_plagio_files)
valid_noplag_count = len(valid_noplag_files)

# Imprimir el número de archivos en cada carpeta
print("Número de archivos en la carpeta de entrenamiento (plagio):", train_plagio_count)
print("Número de archivos en la carpeta de entrenamiento (no plagio):", train_noplag_count)
print("Número de archivos en la carpeta de prueba (plagio):", test_plagio_count)
print("Número de archivos en la carpeta de prueba (no plagio):", test_noplag_count)
print("Número de archivos en la carpeta de validación (plagio):", valid_plagio_count)
print("Número de archivos en la carpeta de validación (no plagio):", valid_noplag_count)
