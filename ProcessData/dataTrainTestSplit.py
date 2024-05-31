

import os
import pandas as pd
import shutil

# Define paths
data_path = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\data\conplag_version_2\versions\bplag_version_1'
labels_file = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\data\conplag_version_2\versions\labels.csv' 

# Leer el archivo de etiquetas
labels = pd.read_csv(labels_file)

# Crear estructura de directorios
os.makedirs('plagio', exist_ok=True)
os.makedirs('noplag', exist_ok=True)

missing_files = []
plagio_files = set()
noplag_files = set()

def move_files(labels):
    for _, row in labels.iterrows():
        sub1 = row['sub1']
        sub2 = row['sub2']
        verdict = row['verdict']

        src_sub1 = os.path.join(data_path, f'{sub1}_{sub2}', sub1, f'{sub1}.java')
        src_sub2 = os.path.join(data_path, f'{sub1}_{sub2}', sub2, f'{sub2}.java')
        
        if verdict == 1:
            dest_dir = 'plagio'
            plagio_files.update([sub1, sub2])
        else:
            dest_dir = 'noplag'
            noplag_files.update([sub1, sub2])
        
        # Verificar si los archivos existen antes de copiarlos
        if os.path.exists(src_sub1):
            shutil.copy(src_sub1, dest_dir)
        else:
            missing_files.append(src_sub1)
        
        if os.path.exists(src_sub2):
            shutil.copy(src_sub2, dest_dir)
        else:
            missing_files.append(src_sub2)

# Mover los archivos
move_files(labels)

# Contar archivos en cada directorio
def count_files(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

plagio_count = count_files('plagio')
noplag_count = count_files('noplag')

# Contar archivos únicos en los conjuntos registrados
unique_plagio_files = len(plagio_files)
unique_noplag_files = len(noplag_files)

print(f'Cantidad de archivos que deberían estar en "plagio": {labels[labels["verdict"] == 1].shape[0] * 2}')
print(f'Cantidad de archivos que deberían estar en "noplag": {labels[labels["verdict"] == 0].shape[0] * 2}')
print(f'Cantidad de archivos en "plagio": {plagio_count}')
print(f'Cantidad de archivos en "noplag": {noplag_count}')
print(f'Cantidad de archivos únicos movidos a "plagio": {unique_plagio_files}')
print(f'Cantidad de archivos únicos movidos a "noplag": {unique_noplag_files}')

if missing_files:
    print(f'Archivos faltantes ({len(missing_files)}):')
    for file in missing_files:
        print(file)
else:
    print('No faltan archivos.')
