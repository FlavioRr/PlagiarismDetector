import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, log_loss, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Función para entrenar un modelo de Random Forest utilizando datos preprocesados y guardar el modelo
def train_random_forest():
    # Cargar los datos preprocesados
    X, y, tfidf_vectorizer = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\preprocessed_all_data.pkl')

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Definir el modelo de Random Forest
    rf_model = RandomForestClassifier(random_state=42)

    # Definir los parámetros para GridSearchCV
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Configurar GridSearchCV para encontrar los mejores hiperparámetros
    grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

    # Ajustar GridSearchCV al conjunto de entrenamiento
    grid_search.fit(X_train, y_train)

    # Mejor conjunto de hiperparámetros
    print(f"Mejores parámetros: {grid_search.best_params_}")

    # Evaluar el mejor modelo encontrado por GridSearchCV
    best_model = grid_search.best_estimator_
    train_preds = best_model.predict(X_train)
    train_accuracy = accuracy_score(y_train, train_preds)
    train_loss = log_loss(y_train, best_model.predict_proba(X_train))

    print(f"Train Accuracy: {train_accuracy * 100:.2f}%")
    print(f"Train Loss: {train_loss:.4f}")

    test_preds = best_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, test_preds)
    test_loss = log_loss(y_test, best_model.predict_proba(X_test))

    print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
    print(f"Test Loss: {test_loss:.4f}")

    # Generar el reporte de clasificación
    classification_rep = classification_report(y_test, test_preds, output_dict=True)
    classification_df = pd.DataFrame(classification_rep).transpose()
    print(f"Classification Report:\n{classification_df}")

    # Guardar el reporte de clasificación como archivo CSV
    classification_df.to_csv(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\classification_report.csv', index=True)

    # Generar la matriz de confusión
    conf_matrix = confusion_matrix(y_test, test_preds)

    # Plotear la matriz de confusión
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['No Plagiarism', 'Plagiarism'], yticklabels=['No Plagiarism', 'Plagiarism'])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')
    plt.savefig(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\confusion_matrix.png')
    plt.show()

    # Guardar el modelo entrenado y el vectorizador TF-IDF
    joblib.dump((best_model, tfidf_vectorizer), r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\random_forest_model_with_features.pkl')

if __name__ == "__main__":
    train_random_forest()
    print("Model training completed and model saved.")
