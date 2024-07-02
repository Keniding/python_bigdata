from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import preprocesamiento

df = preprocesamiento.df

analyzer = SentimentIntensityAnalyzer()

# Función para obtener el sentimiento
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores['compound']

df['sentimiento'] = df['comentario_procesado'].apply(get_sentiment)

# Asignar categorías basadas en el sentimiento
def categorize_sentiment(score):
    if score >= 0.05:
        return 'positiva'
    elif score <= -0.05:
        return 'negativa'
    else:
        return 'neutral'

df['categoria'] = df['sentimiento'].apply(categorize_sentiment)

# Mostrar resultados
print(df)
