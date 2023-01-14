import urllib.request
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Veri setini indirme:
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
urllib.request.urlretrieve(url, "adult.data")

#Veri kümesini bir Pandas DataFrame'e okuma:
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

#Özellikleri normalleştirme:
scaler = StandardScaler()
df[["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]] = scaler.fit_transform(df[["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]])

# Özellikleri ve hedefi çıkarma:
X = df[["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week"]].values
y = df["income"].values

# Verileri eğitim ve test setlerine ayırma:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# k-NN sınıflandırıcısını oluşturma:
knn = KNeighborsClassifier(n_neighbors=3)
# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Sınıflandırmak için bir örnek seçme:
sample = X_test[0]

# FNumunenin en yakın k komşusunu bulma:
k = 5
neighbors = knn.kneighbors(sample.reshape(1, -1), n_neighbors=k, return_distance=False)

#En yakın k komşunun indislerini yazdırma:
print(f"The {k} nearest neighbors of the sample are:")
for i, index in enumerate(neighbors[0]):
    print(f"{i+1}. Index {index}")
