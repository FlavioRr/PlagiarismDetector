import os

# Rutas de las carpetas
train_noplag_dir = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\train\noplag'
train_plagio_dir = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\train\plagio'
test_noplag_dir = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\test\noplag'
test_plagio_dir = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\test\plagio'

# Función para contar archivos en una carpeta
def count_files(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

# Contar archivos
num_train_noplag = count_files(train_noplag_dir)
num_train_plagio = count_files(train_plagio_dir)
num_test_noplag = count_files(test_noplag_dir)
num_test_plagio = count_files(test_plagio_dir)

# Imprimir resultados
print(f"Número de archivos en train/noplag: {num_train_noplag}")
print(f"Número de archivos en train/plagio: {num_train_plagio}")
print(f"Número de archivos en test/noplag: {num_test_noplag}")
print(f"Número de archivos en test/plagio: {num_test_plagio}")
