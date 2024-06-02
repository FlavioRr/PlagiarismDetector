import pandas as pd

# Ruta al archivo de etiquetas
labels_file = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\data\conplag_version_2\versions\labels.csv'  # Actualiza con la ruta real del archivo de etiquetas

# Leer el archivo de etiquetas
labels = pd.read_csv(labels_file)

# Conjuntos para almacenar identificadores únicos de archivos
plagio_files = set()
noplag_files = set()

# Recorrer el archivo de etiquetas y agregar identificadores únicos a los conjuntos
for _, row in labels.iterrows():
    sub1 = row['sub1']
    sub2 = row['sub2']
    verdict = row['verdict']

    # Agregar sub1 y sub2 a los conjuntos correspondientes
    if verdict == 1:
        plagio_files.add(sub1)
        plagio_files.add(sub2)
    else:
        noplag_files.add(sub1)
        noplag_files.add(sub2)

# Contar los archivos únicos en cada conjunto
num_plagio_files = len(plagio_files)
num_noplag_files = len(noplag_files)

print(f'Cantidad de archivos únicos que deberían estar en plagio: {num_plagio_files}')
print(f'Cantidad de archivos únicos que deberían estar en no plagio: {num_noplag_files}')
