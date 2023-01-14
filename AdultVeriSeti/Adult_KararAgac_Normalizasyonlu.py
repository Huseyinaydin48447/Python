import urllib.request
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Veri setini indirir:
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
urllib.request.urlretrieve(url, "adult.data")

# Veri kümesini bir Pandas DataFrame'e okur:
df = pd.read_csv("adult.data", names=[
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
])



from sklearn.preprocessing import LabelEncoder

# Kategorik özellikleri sayısal değerlere dönüştürme:
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



# Özellikleri ve hedefi çıkarmak:
X = df[["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week"]].values
y = df["income"].values


from sklearn.preprocessing import MinMaxScaler

# MinMaxScaler kullanarak özellikleri normalleştirme:
scaler = MinMaxScaler()
scaler.fit(X)
X_normalized = scaler.transform(X)

from sklearn.model_selection import train_test_split

# Verileri eğitim ve test setlerine ayırma:
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2)
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

plt.figure(figsize=(20, 10))
plot_tree(clf)

