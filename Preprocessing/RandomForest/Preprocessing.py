import os
import re
import joblib
#pip install gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

def load_files_from_directory(directory):
    files = []
    labels = []
    filenames = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            with open(os.path.join(root, filename), 'r', encoding='utf-8') as f:
                code = f.read()
                # Eliminar comentarios
                code = re.sub(r'//.*|/\*[\s\S]*?\*/', '', code)
                # Normalizar nombres de variables (esto puede ser más complejo dependiendo del lenguaje)
                code = re.sub(r'\b[_a-zA-Z][_a-zA-Z0-9]*\b', 'VAR', code)
                files.append(code)
                filenames.append(filename)
                if 'plagio' in root:
                    labels.append(1)
                else:
                    labels.append(0)
    return files, labels, filenames

def preprocess_data():
    # Paths de las carpetas de datos
    test_noplag_path = r"C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\test\noplag"
    test_plagio_path = r"C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\test\plagio"
    train_noplag_path = r"C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\train\noplag"
    train_plagio_path = r"C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\train\plagio"

    # Cargar datos de entrenamiento y prueba
    train_files_noplag, train_labels_noplag, _ = load_files_from_directory(train_noplag_path)
    train_files_plagio, train_labels_plagio, _ = load_files_from_directory(train_plagio_path)
    test_files_noplag, test_labels_noplag, test_filenames_noplag = load_files_from_directory(test_noplag_path)
    test_files_plagio, test_labels_plagio, test_filenames_plagio = load_files_from_directory(test_plagio_path)

    # Combinar datos de entrenamiento y prueba
    train_files = train_files_noplag + train_files_plagio
    train_labels = train_labels_noplag + train_labels_plagio
    test_files = test_files_noplag + test_files_plagio
    test_labels = test_labels_noplag + test_labels_plagio
    test_filenames = test_filenames_noplag + test_filenames_plagio

    # Vectorización con Doc2Vec
    tagged_data = [TaggedDocument(words=file.split(), tags=[str(i)]) for i, file in enumerate(train_files)]
    model = Doc2Vec(vector_size=100, window=5, min_count=1, workers=4, epochs=100)
    model.build_vocab(tagged_data)
    model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)

    # Transformar datos de entrenamiento y prueba
    X_train = [model.infer_vector(file.split()) for file in train_files]
    X_test = [model.infer_vector(file.split()) for file in test_files]

    # Guardar los datos preprocesados, el modelo Doc2Vec y las etiquetas
    joblib.dump((X_train, train_labels, X_test, test_labels), r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest\preprocessed_data_doc2vec.pkl')
    model.save(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest/doc2vec_model.d2v')

if __name__ == "__main__":
    preprocess_data()
