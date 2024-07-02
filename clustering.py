from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
import clasificacion

df = clasificacion.df

# Vectorización
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['comentario_procesado'])

# Aplicar K-Means
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(X)
