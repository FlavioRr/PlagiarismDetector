import os
import re
import pandas as pd
import javalang
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
import joblib
import numpy as np

def read_java_file(file_path):
    """Function to read a Java file and return its content as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def extract_ast_nodes(code):
    """Extract AST nodes from Java code."""
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

def jaccard_similarity(set1, set2):
    """Compute Jaccard similarity between two sets."""
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def manhattan_distance(v1, v2):
    """Compute Manhattan distance between two vectors."""
    return np.sum(np.abs(v1 - v2))

def preprocess_data_with_ast(directory):
    """Preprocess all Java files in the specified directory and return a DataFrame."""
    data = []
    labels_path = os.path.join(directory, 'versions', 'labels.csv')  # Correct path to labels.csv
    labels = pd.read_csv(labels_path)
    
    # Verificar las columnas del archivo CSV
    print("Columnas disponibles en labels.csv:", labels.columns)
    
    # Asegurarse de que la columna correcta está presente
    label_column = 'veredict'  # Cambia esto si el nombre de la columna es diferente
    if label_column not in labels.columns:
        raise KeyError(f"La columna '{label_column}' no se encuentra en labels.csv")
    
    for index, row in labels.iterrows():
        sub1 = row['sub1']
        sub2 = row['sub2']
        label = row[label_column]  # Use the correct label column
        pair_id = f"{sub1}_{sub2}"  # Construct pair_id from sub1 and sub2
        pair_folder = os.path.join(directory, 'versions', 'version_2', pair_id)
        
        # Paths to the two Java files in the pair folder
        file1_path = os.path.join(pair_folder, f"{sub1}.java")
        file2_path = os.path.join(pair_folder, f"{sub2}.java")
        
        # Read and extract AST nodes from both files
        if os.path.exists(file1_path) and os.path.exists(file2_path):
            code1 = read_java_file(file1_path)
            code2 = read_java_file(file2_path)
            ast_nodes1 = extract_ast_nodes(code1)
            ast_nodes2 = extract_ast_nodes(code2)
            
            if ast_nodes1 and ast_nodes2:  # Only combine if both are non-empty
                # Combine the AST nodes from both files
                combined_ast_nodes = ast_nodes1 + ' ' + ast_nodes2
                data.append([combined_ast_nodes, label, ast_nodes1, ast_nodes2])
    
    return pd.DataFrame(data, columns=['code', 'label', 'ast_nodes1', 'ast_nodes2'])

def save_preprocessed_data(data, output_path):
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust max_features as needed
    X = tfidf_vectorizer.fit_transform(data['code'])
    y = data['label']
    
    # Compute additional features
    manhattan_distances = []
    jaccard_similarities = []

    for _, row in data.iterrows():
        ast_set1 = set(row['ast_nodes1'].split())
        ast_set2 = set(row['ast_nodes2'].split())
        jaccard_similarities.append(jaccard_similarity(ast_set1, ast_set2))
        
        vec1 = tfidf_vectorizer.transform([row['ast_nodes1']]).toarray()[0]
        vec2 = tfidf_vectorizer.transform([row['ast_nodes2']]).toarray()[0]
        manhattan_distances.append(manhattan_distance(vec1, vec2))
    
    # Combine features
    X_additional = np.array([manhattan_distances, jaccard_similarities]).T
    X_combined = np.hstack((X.toarray(), X_additional))
    
    joblib.dump((X_combined, y, tfidf_vectorizer), output_path)

if __name__ == "__main__":
    data_directory = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\data\conplag_version_2'
    processed_data = preprocess_data_with_ast(data_directory)
    save_preprocessed_data(processed_data, r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest\preprocessed_data_with_features.pkl')
    print("Preprocessing completed and data saved.")
