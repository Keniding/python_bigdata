import matplotlib.pyplot as plt
import seaborn as sns
import levantar

df = levantar.df

# Distribución de géneros
sns.countplot(x='datos_entrevistado.genero', data=df)
plt.title('Distribución de Géneros')
plt.show()

# Distribución de edades
sns.histplot(df['datos_entrevistado.edad'], bins=10)
plt.title('Distribución de Edades')
plt.show()

# Interés en servicios de HelloFresh
sns.countplot(x='preguntas_filtro.interes_servicios_hellofresh', data=df)
plt.title('Interés en Servicios de HelloFresh')
plt.show()
