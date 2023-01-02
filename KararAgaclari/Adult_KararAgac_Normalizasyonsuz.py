
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
df = pd.read_csv(url, names=[
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
])
# Daha sonra, kategorik özellikleri numerik değerlere dönüştürün. Bunun için scikit learn kütü#phanesinden LabelEncoder sınıfını kullanabiliriz:
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["workclass"] = le.fit_transform(df["workclass"])
df["education"] = le.fit_transform(df["education"])
df["marital-status"] = le.fit_transform(df["marital-status"])
df["occupation"] = le.fit_transform(df["occupation"])
df["relationship"] = le.fit_transform(df["relationship"])
df["race"] = le.fit_transform(df["race"])
df["sex"] = le.fit_transform(df["sex"])
df["native-country"] = le.fit_transform(df["native-country"])
df["income"] = le.fit_transform(df["income"])
# Veri setini eğitim ve test verileri olarak bölmek için:
from sklearn.model_selection import train_test_split
X = df.drop("income", axis=1)
y = df["income"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Eğitim verilerini kullanarak karar ağacı oluşturun ve bu ağacı görselleştirmek içinde:
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
plt.figure(figsize=(20, 10))
plot_tree(clf)

