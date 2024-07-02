from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

import analisis_sentimiento as anasi

df = anasi.df

# Vectorización
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['comentario_procesado'])

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, df['categoria'], test_size=0.2, random_state=42)

# Entrenar modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# Predecir y evaluar
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
