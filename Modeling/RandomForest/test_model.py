import joblib
import re
import javalang

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

def predict_new_sample(file1_path, file2_path):
    # Cargar el modelo Random Forest y el vectorizador TF-IDF entrenado
    rf_model, tfidf_vectorizer = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\random_forest_model.pkl')

    # Leer y preprocesar las nuevas muestras de código
    code1 = read_java_file(file1_path)
    code2 = read_java_file(file2_path)
    ast_nodes1 = extract_ast_nodes(code1)
    ast_nodes2 = extract_ast_nodes(code2)
    
    if ast_nodes1 and ast_nodes2:  # Solo combinar si ambos no están vacíos
        # Combinar los nodos AST de ambos archivos
        combined_ast_nodes = ast_nodes1 + ' ' + ast_nodes2
        
        # Transformar la nueva muestra usando el vectorizador TF-IDF
        sample_vector = tfidf_vectorizer.transform([combined_ast_nodes])
        
        # Hacer predicciones usando el modelo Random Forest
        prediction = rf_model.predict(sample_vector)
        prediction_prob = rf_model.predict_proba(sample_vector)
        
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
