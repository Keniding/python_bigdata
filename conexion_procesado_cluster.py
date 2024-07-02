import pymongo
import pandas as pd
import conexion #modulo local

# URL de conexión de MongoDB Atlas
#formato: mongodb+srv://user:pass@cluster0.hwlpkz2.mongodb.net/
url_conexion = conexion.url_conexion

# Conectar a MongoDB Atlas
cliente = pymongo.MongoClient(url_conexion)

# Seleccionar la base de datos y la colección
base_de_datos = cliente["comentarios"]
coleccion = base_de_datos["resultados_clustering"]

# Cargar los datos en un DataFrame de pandas
datos = list(coleccion.find())
df = pd.json_normalize(datos)

# Mostrar las primeras filas del DataFrame
print(df.head())