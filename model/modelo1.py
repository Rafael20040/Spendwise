import pandas as pd
import sklearn as skl
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(
    "dataset/compras_limpo.csv",
    sep=",",
    decimal="."
)

y = df["categoria_spendwise"]
X=df['produto']   

modelo = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classificador", LogisticRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

modelo.fit(X_train.squeeze(), y_train)

modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)
accuracy = accuracy_score(y_test, previsoes)

print("Previsões:", previsoes)
print("\nCategorias reais:", y_test.values)
print("\nAccuracy:", accuracy)
