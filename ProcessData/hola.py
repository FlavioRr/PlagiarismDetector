import os

# Paths base
new_base_dir = 'C:\\Users\\Flavio Ruvalcaba\\Documents\\Escuela\\Universidad\\8Semestre\\PlagiarismDetector\\finalDataset\\split'

# Función para contar archivos en un directorio
def count_files(directory):
    return len(os.listdir(directory))

# Directorios de interés
directories = {
    'train/plagio': os.path.join(new_base_dir, 'train', 'plagio'),
    'train/noplag': os.path.join(new_base_dir, 'train', 'noplag'),
    'validation/plagio': os.path.join(new_base_dir, 'validation', 'plagio'),
    'validation/noplag': os.path.join(new_base_dir, 'validation', 'noplag'),
    'test/plagio': os.path.join(new_base_dir, 'test', 'plagio'),
    'test/noplag': os.path.join(new_base_dir, 'test', 'noplag'),
}

# Contar archivos y mostrar resultados
for name, path in directories.items():
    file_count = count_files(path)
    print(f'Hay {file_count} archivos en la carpeta {name}')