import joblib
import re
import javalang
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

# Función para predecir el plagio para un nuevo par de archivos Java usando un modelo entrenado de Random Forest
def predict_new_sample(file1_path, file2_path):
    # Cargar el modelo Random Forest y el vectorizador TF-IDF entrenado
    rf_model, tfidf_vectorizer = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\random_forest_model_with_features.pkl')

    # Leer y preprocesar las nuevas muestras de código
    code1 = read_java_file(file1_path)
    code2 = read_java_file(file2_path)
    ast_nodes1 = extract_ast_nodes(code1)
    ast_nodes2 = extract_ast_nodes(code2)
    
    if ast_nodes1 and ast_nodes2:  # Solo combinar si ambos no están vacíos
        # Combinar los nodos AST de ambos archivos
        combined_ast_nodes = ast_nodes1 + ' ' + ast_nodes2
        
        # Transformar la nueva muestra usando el vectorizador TF-IDF
        sample_vector = tfidf_vectorizer.transform([combined_ast_nodes]).toarray()[0]
        
        # Calcular características adicionales
        ast_set1 = set(ast_nodes1.split())
        ast_set2 = set(ast_nodes2.split())
        jaccard_sim = jaccard_similarity(ast_set1, ast_set2)
        vec1 = tfidf_vectorizer.transform([ast_nodes1]).toarray()[0]
        vec2 = tfidf_vectorizer.transform([ast_nodes2]).toarray()[0]
        manhattan_dist = manhattan_distance(vec1, vec2)
        
        # Combinar todas las características
        sample_vector = np.hstack((sample_vector, [manhattan_dist, jaccard_sim]))
        
        # Hacer predicciones usando el modelo Random Forest
        prediction = rf_model.predict([sample_vector])
        prediction_prob = rf_model.predict_proba([sample_vector])
        
        return 'Plagio' if prediction[0] == 1 else 'No Plagio', prediction_prob
    else:
        return 'Error en la extracción de nodos AST', None

if __name__ == "__main__":
    file1_path = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\OriginalJava.java'
    file2_path = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\PlagiarizedJava.java'
    prediction, prediction_prob = predict_new_sample(file1_path, file2_path)
    print(f"La predicción para la nueva muestra es: {prediction}")
    if prediction_prob is not None:
        print(f"Probabilidades de predicción: {prediction_prob}")
