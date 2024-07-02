import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import conexion_procesado_cluster as conexion

df = conexion.df

# Descargar stopwords
nltk.download('stopwords')

# Función de preprocesamiento
def preprocesar_texto(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar caracteres especiales y números
    texto = re.sub(r'\W', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto)
    # Eliminar stopwords
    stop_words = set(stopwords.words('spanish'))
    palabras = texto.split()
    palabras = [word for word in palabras if word not in stop_words]
    return ' '.join(palabras)

# Aplicar preprocesamiento a los comentarios
df['comentarios_procesados'] = df['comentario'].apply(preprocesar_texto)
