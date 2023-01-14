import urllib.request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Veri setini indirme:
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
urllib.request.urlretrieve(url, "adult.data")

# Veri kümesini bir Pandas DataFrame'e okuma:
df = pd.read_csv("adult.data", names=[
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
])

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



# Özellikleri ve hedefi çıkarma:
X = df[["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week"]].values
y = df["income"].values

# Verileri eğitim ve test setlerine ayırma: X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Karar ağacı sınıflandırıcısını oluşturun ve eğitim verileri üzerinde eğitme:
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)

# Test verileri üzerinde tahminler yapma:
y_pred = clf.predict(X_test)

# Modelin doğruluğunu hesaplayın ve yazdırma:
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ",accuracy)
