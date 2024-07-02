from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import preprocesamiento_cluster as preprocesamiento
import nltk
from nltk.corpus import stopwords

# Descargar stopwords
nltk.download('stopwords')

# Obtener las stopwords en español
stop_words_spanish = stopwords.words('spanish')

df = preprocesamiento.df

# Vectorizar comentarios
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words=stop_words_spanish)
X = vectorizer.fit_transform(df['comentarios_procesados'])

# Aplicar LDA
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X)

# Mostrar los temas
def mostrar_palabras_clave(modelo, feature_names, n_top_words):
    for idx, topic in enumerate(modelo.components_):
        print(f"Tema {idx}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

n_top_words = 10
tf_feature_names = vectorizer.get_feature_names_out()
mostrar_palabras_clave(lda, tf_feature_names, n_top_words)
