import joblib
from sklearn.cluster import KMeans

# Cargar los vectores y el vectorizador
X = joblib.load(r'C:\Users\Flavio Ruvalcaba\Documents\Escuela\Universidad\8Semestre\PlagiarismDetector\Preprocessing\data_vectors.pkl')

# Aplicar K-Means
num_clusters = 10  # Número de clusters (hiperparámetro a ajustar)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Resultados del clustering
clusters = defaultdict(list)
for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(all_files_content[idx])

# Imprimir un ejemplo de clusters
for cluster_id, files in clusters.items():
    print(f"Cluster {cluster_id}: {len(files)} files")

# Guardar modelo para uso futuro
joblib.dump(kmeans, 'kmeans_model.pkl')
