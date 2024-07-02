import analisis_clave_word as analisis

clusters = analisis.clusters
df = analisis.df

# Muestra de comentarios por cluster
for cluster in clusters:
    print(f"Cluster {cluster}:")
    muestra = df[df['cluster'] == cluster]['comentario'].sample(5)
    for comentario in muestra:
        print(comentario)
    print("\n")
