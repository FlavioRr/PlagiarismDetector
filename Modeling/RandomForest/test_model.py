import joblib
from gensim.models.doc2vec import Doc2Vec

def predict_new_sample(sample):
    # Cargar el modelo Doc2Vec y el modelo entrenado
    doc2vec_model = Doc2Vec.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest\doc2vec_model.d2v')
    model = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\random_forest_model.pkl')

    # Preprocesar la nueva muestra
    sample_preprocessed = sample.replaceAll("/\*[\s\S]*?\*/", "").replaceAll("//.*", "")
    sample_preprocessed = re.sub(r'\b[_a-zA-Z][_a-zA-Z0-9]*\b', 'VAR', sample_preprocessed)
    
    # Transformar la nueva muestra
    sample_vector = doc2vec_model.infer_vector(sample_preprocessed.split())
    prediction = model.predict([sample_vector])
    return 'Plagio' if prediction[0] == 1 else 'No Plagio'

if __name__ == "__main__":
    new_sample = """
    public class FactorialCalculator {
        public static int getFactorial(int n) {
            if (n == 0) {
                return 1;
            } else {
                return n * getFactorial(n - 1);
            }
        }

        public static void main(String[] args) {
            int number = 5;
            System.out.println("Factorial of " + number + " is " + getFactorial(number));
        }
    }
    """
    prediction = predict_new_sample(new_sample)
    print(f"La predicción para la nueva muestra es: {prediction}")
