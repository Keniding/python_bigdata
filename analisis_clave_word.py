from wordcloud import WordCloud
import matplotlib.pyplot as plt
import analisis_topico

df = analisis_topico.df

# Generar nube de palabras para cada cluster
clusters = df['cluster'].unique()
for cluster in clusters:
    comentarios_cluster = df[df['cluster'] == cluster]['comentarios_procesados']
    texto_cluster = ' '.join(comentarios_cluster)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_cluster)
    
    # Mostrar nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Nube de Palabras - Cluster {cluster}')
    plt.show()
