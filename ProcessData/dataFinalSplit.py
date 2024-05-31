import os
import shutil
from sklearn.model_selection import train_test_split

# Paths base
base_dir_noplag = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\noplag'
base_dir_plagio = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\plagio'
new_base_dir = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split'

# Crear la nueva estructura de directorios
os.makedirs(new_base_dir, exist_ok=True)
train_dir = os.path.join(new_base_dir, 'train')
test_dir = os.path.join(new_base_dir, 'test')

for dir in [train_dir, test_dir]:
    os.makedirs(os.path.join(dir, 'noplag'), exist_ok=True)
    os.makedirs(os.path.join(dir, 'plagio'), exist_ok=True)

# Función para copiar archivos a la nueva estructura
def copy_files(file_list, source_dir, target_dir):
    for file in file_list:
        shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir, file))

# Leer imágenes
noplag_images = os.listdir(base_dir_noplag)
plagio_images = os.listdir(base_dir_plagio)

# Dividir imágenes en train y test
noplag_train, noplag_test = train_test_split(noplag_images, test_size=0.3, random_state=42)
plagio_train, plagio_test = train_test_split(plagio_images, test_size=0.3, random_state=42)

# Copiar las imágenes a los directorios correspondientes
copy_files(noplag_train, base_dir_noplag, os.path.join(train_dir, 'noplag'))
copy_files(noplag_test, base_dir_noplag, os.path.join(test_dir, 'noplag'))

copy_files(plagio_train, base_dir_plagio, os.path.join(train_dir, 'plagio'))
copy_files(plagio_test, base_dir_plagio, os.path.join(test_dir, 'plagio'))

print("Las imágenes se han copiado y distribuido en la nueva estructura de directorios.")
