import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, log_loss, classification_report

def train_random_forest():
    # Cargar los datos preprocesados
    X, y, tfidf_vectorizer = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest\preprocessed_data_with_features.pkl')

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar un modelo de Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)  # You can tune these parameters
    rf_model.fit(X_train, y_train)

    # Evaluar el modelo en el conjunto de entrenamiento
    train_preds = rf_model.predict(X_train)
    train_accuracy = accuracy_score(y_train, train_preds)
    train_loss = log_loss(y_train, rf_model.predict_proba(X_train))

    print(f"Train Accuracy: {train_accuracy * 100:.2f}%")
    print(f"Train Loss: {train_loss:.4f}")

    # Evaluar el modelo en el conjunto de prueba
    test_preds = rf_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, test_preds)
    test_loss = log_loss(y_test, rf_model.predict_proba(X_test))

    print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
    print(f"Test Loss: {test_loss:.4f}")

    # Guardar el modelo entrenado y el vectorizador TF-IDF
    joblib.dump((rf_model, tfidf_vectorizer), r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\random_forest_model_with_features.pkl')

if __name__ == "__main__":
    train_random_forest()
    print("Model training completed and model saved.")
