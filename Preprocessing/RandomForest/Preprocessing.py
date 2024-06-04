import os
import re
import pandas as pd
import javalang
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import numpy as np

# Función para leer un archivo Java y devolver su contenido como una cadena
def read_java_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Función para extraer nodos AST del código Java
def extract_ast_nodes(code):
    try:
        tokens = list(javalang.tokenizer.tokenize(code))
        parser = javalang.parser.Parser(tokens)
        tree = parser.parse()

        ast_nodes = []
        for path, node in tree:
            if isinstance(node, javalang.tree.Node):
                ast_nodes.append(node.__class__.__name__)
        return ' '.join(ast_nodes)
    except (javalang.parser.JavaSyntaxError, javalang.tokenizer.LexerError) as e:
        print(f"Error al analizar el código Java: {e}")
        return ''

# Función para calcular la similitud de Jaccard entre dos conjuntos
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Función para calcular la distancia de Manhattan entre dos vectores
def manhattan_distance(v1, v2):
    return np.sum(np.abs(v1 - v2))

# Función para preprocesar todos los archivos Java en el directorio especificado y devolver un DataFrame
def preprocess_data_with_ast(directory):
    data = []
    labels_path = os.path.join(directory, 'versions', 'labels.csv')  # Ruta correcta a labels.csv
    labels = pd.read_csv(labels_path)
    
    print("Columnas disponibles en labels.csv:", labels.columns)
    
    label_column = 'veredict'  # Asegúrate de que la columna correcta está presente
    if label_column not in labels.columns:
        raise KeyError(f"La columna '{label_column}' no se encuentra en labels.csv")
    
    for index, row in labels.iterrows():
        sub1 = row['sub1']
        sub2 = row['sub2']
        label = row[label_column]  # Usa la columna de etiquetas correcta
        pair_id = f"{sub1}_{sub2}"  # Construye pair_id desde sub1 y sub2
        pair_folder = os.path.join(directory, 'versions', 'version_2', pair_id)
        
        # Rutas a los dos archivos Java en la carpeta del par
        file1_path = os.path.join(pair_folder, f"{sub1}.java")
        file2_path = os.path.join(pair_folder, f"{sub2}.java")
        
        if os.path.exists(file1_path) and os.path.exists(file2_path):
            code1 = read_java_file(file1_path)
            code2 = read_java_file(file2_path)
            ast_nodes1 = extract_ast_nodes(code1)
            ast_nodes2 = extract_ast_nodes(code2)
            
            if ast_nodes1 and ast_nodes2:  # Solo combinar si ambos no están vacíos
                combined_ast_nodes = ast_nodes1 + ' ' + ast_nodes2
                data.append([combined_ast_nodes, label, ast_nodes1, ast_nodes2])
    
    return pd.DataFrame(data, columns=['code', 'label', 'ast_nodes1', 'ast_nodes2'])

# Función para guardar los datos preprocesados con características adicionales en un archivo
def save_preprocessed_data(data, output_path):
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # Puedes ajustar max_features según sea necesario
    X = tfidf_vectorizer.fit_transform(data['code'])
    y = data['label']
    
    # Calcular características adicionales
    manhattan_distances = []
    jaccard_similarities = []

    for _, row in data.iterrows():
        ast_set1 = set(row['ast_nodes1'].split())
        ast_set2 = set(row['ast_nodes2'].split())
        jaccard_similarities.append(jaccard_similarity(ast_set1, ast_set2))
        
        vec1 = tfidf_vectorizer.transform([row['ast_nodes1']]).toarray()[0]
        vec2 = tfidf_vectorizer.transform([row['ast_nodes2']]).toarray()[0]
        manhattan_distances.append(manhattan_distance(vec1, vec2))
    
    # Combinar características
    X_additional = np.array([manhattan_distances, jaccard_similarities]).T
    X_combined = np.hstack((X.toarray(), X_additional))
    
    joblib.dump((X_combined, y, tfidf_vectorizer), output_path)

if __name__ == "__main__":
    data_directory = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\data\conplag_version_2'
    processed_data = preprocess_data_with_ast(data_directory)
    save_preprocessed_data(processed_data, r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest\preprocessed_data_with_features.pkl')
    print("Preprocessing completed and data saved.")
