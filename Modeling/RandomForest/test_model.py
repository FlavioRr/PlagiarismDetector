import joblib
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
        print(f"Error parsing Java code: {e}")
        return ''

# Función para probar el modelo usando archivos externos
def test_model_on_external_files(file1_path, file2_path, model_path):
    model, tfidf_vectorizer = joblib.load(model_path)
    
    code1 = read_java_file(file1_path)
    code2 = read_java_file(file2_path)
    ast_nodes1 = extract_ast_nodes(code1)
    ast_nodes2 = extract_ast_nodes(code2)

    if ast_nodes1 and ast_nodes2:
        combined_ast_nodes = ast_nodes1 + ' ' + ast_nodes2
        combined_features = tfidf_vectorizer.transform([combined_ast_nodes])
        
        ast_set1 = set(ast_nodes1.split())
        ast_set2 = set(ast_nodes2.split())

        # Calcular características adicionales
        jaccard_similarity = len(ast_set1.intersection(ast_set2)) / len(ast_set1.union(ast_set2)) if len(ast_set1.union(ast_set2)) != 0 else 0
        vec1 = tfidf_vectorizer.transform([ast_nodes1]).toarray()[0]
        vec2 = tfidf_vectorizer.transform([ast_nodes2]).toarray()[0]
        manhattan_distance = np.sum(np.abs(vec1 - vec2))

        # Combinar todas las características
        additional_features = np.array([[manhattan_distance, jaccard_similarity]])
        combined_features = np.hstack((combined_features.toarray(), additional_features))

        # Predecir usando el modelo
        prediction = model.predict(combined_features)
        return prediction[0]
    else:
        print("Error: AST extraction failed for one or both files.")
        return None

# Ejemplo de uso de la función de prueba
file1 = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\TestFiles\case-05\original\T5.java'
file2 = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\TestFiles\case-05\non-plagiarized\02\T05.java'
model_path = r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\random_forest_model_with_features.pkl'

result = test_model_on_external_files(file1, file2, model_path)
print(f"Prediction for the external files: {result}")
