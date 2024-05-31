import os
import shutil
from sklearn.model_selection import train_test_split

# Paths base
base_dir = 'C:\\Users\\Flavio Ruvalcaba\\Documents\\Escuela\\Universidad\\8Semestre\\PlagiarismDetector\\finalDataset'
new_base_dir = 'C:\\Users\\Flavio Ruvalcaba\\Documents\\Escuela\\Universidad\\8Semestre\\PlagiarismDetector\\finalDataset\\split'

# Crear la nueva estructura de directorios
os.makedirs(new_base_dir, exist_ok=True)
train_dir = os.path.join(new_base_dir, 'train')
validation_dir = os.path.join(new_base_dir, 'validation')
test_dir = os.path.join(new_base_dir, 'test')

for dir in [train_dir, validation_dir, test_dir]:
    os.makedirs(os.path.join(dir, 'plagio'), exist_ok=True)
    os.makedirs(os.path.join(dir, 'noplag'), exist_ok=True)

# Función para copiar archivos a la nueva estructura
def copy_files(file_list, source_dir, target_dir):
    for file in file_list:
        shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir, file))

# Leer documentos
plagio_docs = os.listdir(os.path.join(base_dir, 'plagio'))
noplag_docs = os.listdir(os.path.join(base_dir, 'noplag'))

# Dividir documentos en train, validation y test
plagio_train, plagio_temp = train_test_split(plagio_docs, test_size=0.3, random_state=42)
plagio_val, plagio_test = train_test_split(plagio_temp, test_size=1/3, random_state=42) # 0.3 * 1/3 = 0.1

noplag_train, noplag_temp = train_test_split(noplag_docs, test_size=0.3, random_state=42)
noplag_val, noplag_test = train_test_split(noplag_temp, test_size=1/3, random_state=42) # 0.3 * 1/3 = 0.1

# Copiar los documentos a los directorios correspondientes
copy_files(plagio_train, os.path.join(base_dir, 'plagio'), os.path.join(train_dir, 'plagio'))
copy_files(plagio_val, os.path.join(base_dir, 'plagio'), os.path.join(validation_dir, 'plagio'))
copy_files(plagio_test, os.path.join(base_dir, 'plagio'), os.path.join(test_dir, 'plagio'))

copy_files(noplag_train, os.path.join(base_dir, 'noplag'), os.path.join(train_dir, 'noplag'))
copy_files(noplag_val, os.path.join(base_dir, 'noplag'), os.path.join(validation_dir, 'noplag'))
copy_files(noplag_test, os.path.join(base_dir, 'noplag'), os.path.join(test_dir, 'noplag'))

print("Los documentos se han copiado y distribuido en la nueva estructura de directorios.")