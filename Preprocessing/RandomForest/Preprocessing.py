import os
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
import joblib

def load_files_from_directory(directory):
    files = []
    labels = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            with open(os.path.join(root, filename), 'r', encoding='utf-8') as f:
                files.append(f.read())
                if 'plagio' in root:
                    labels.append(1)
                else:
                    labels.append(0)
    return files, labels

def preprocess_data():
    # Paths de las carpetas de datos
    test_noplag_path = r"C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\test\noplag"
    test_plagio_path = r"C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\test\plagio"
    train_noplag_path = r"C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\train\noplag"
    train_plagio_path = r"C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\finalDataset\split\train\plagio"

    # Cargar datos de entrenamiento y prueba
    train_files_noplag, train_labels_noplag = load_files_from_directory(train_noplag_path)
    train_files_plagio, train_labels_plagio = load_files_from_directory(train_plagio_path)
    test_files_noplag, test_labels_noplag = load_files_from_directory(test_noplag_path)
    test_files_plagio, test_labels_plagio = load_files_from_directory(test_plagio_path)

    # Combinar datos de entrenamiento y prueba
    train_files = train_files_noplag + train_files_plagio
    train_labels = train_labels_noplag + train_labels_plagio
    test_files = test_files_noplag + test_files_plagio
    test_labels = test_labels_noplag + test_labels_plagio

    # Transformación TF-IDF con bigramas y eliminación de stopwords
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
    X_train = vectorizer.fit_transform(train_files)
    X_test = vectorizer.transform(test_files)

    # Balancear los datos de entrenamiento usando SMOTE
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train, train_labels)

    # Guardar los datos preprocesados y el vectorizador
    joblib.dump((X_train_balanced, y_train_balanced, X_test, test_labels), r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest/preprocessed_data.pkl')
    joblib.dump(vectorizer, r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest/vectorizer.pkl')

if __name__ == "__main__":
    preprocess_data()
