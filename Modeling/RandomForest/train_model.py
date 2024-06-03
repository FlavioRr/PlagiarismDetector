import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    # Cargar los datos preprocesados
    X_train, y_train, X_test, y_test = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\RandomForest\preprocessed_data_doc2vec.pkl')

    # Definir el modelo
    model = RandomForestClassifier(random_state=42)

    # Definir los parámetros para el grid search
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Configurar GridSearchCV para encontrar los mejores hiperparámetros
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

    # Ajustar el grid search al conjunto de entrenamiento balanceado
    grid_search.fit(X_train, y_train)

    # Mejor conjunto de hiperparámetros
    print(f"Mejores parámetros: {grid_search.best_params_}")

    # Evaluar el mejor modelo encontrado por GridSearchCV
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print(classification_report(y_test, y_pred))

    # Guardar el modelo entrenado
    joblib.dump(best_model, r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Modeling\RandomForest\random_forest_model.pkl')

if __name__ == "__main__":
    train_model()
