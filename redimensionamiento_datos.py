from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import clustering

df = clustering.df
X = clustering.X

# Aplicar PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())

# Visualizar los datos
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['cluster'])
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('Clustering Visualization with PCA')
plt.show()