import joblib

def predict_new_sample(sample):
    # Cargar el vectorizador y el modelo entrenado
    vectorizer = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest\vectorizer.pkl')
    model = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\XGBoost\random_forest_model.pkl')

    # Transformar la nueva muestra
    sample_transformed = vectorizer.transform([sample])
    prediction = model.predict(sample_transformed)
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
