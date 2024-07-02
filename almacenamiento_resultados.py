import redimensionamiento_datos
import redes_conexion

df = redimensionamiento_datos.df
base_de_datos = redes_conexion.base_de_datos

# Crear una nueva colección para los resultados
coleccion_resultados = base_de_datos["resultados_clustering"]

# Convertir DataFrame a diccionario y almacenar en MongoDB
resultados = df.to_dict(orient='records')
coleccion_resultados.insert_many(resultados)
