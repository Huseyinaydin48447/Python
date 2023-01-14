import urllib.request
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Veri setini indirme
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
urllib.request.urlretrieve(url, "adult.data")

# Read the dataset into a Pandas DataFrame
df = pd.read_csv("adult.data", names=[
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"])

# Veri kümesini bir Pandas DataFrame'e okumak için:
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

# Özellikleri ve hedefi çıkarmak için:
X = df[["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week"]].values
y = df["income"].values

# MinMaxScaler kullanarak özellikleri normalleştirme:
scaler = MinMaxScaler()
scaler.fit(X)
X_normalized = scaler.transform(X)
print(X_normalized)
 # çıktısı ise aşağıda vermektedir:
#[[0.30136986 0.875      0.0443019  ... 0.02174022 0.         0.39795918]
#[0.45205479 0.75       0.0482376  ... 0.         0.         0.12244898]
# [0.28767123 0.5        0.13811345 ... 0.         0.         0.39795918]
# ...
# [0.56164384 0.5        0.09482688 ... 0.         0.         0.39795918]
# [0.06849315 0.5        0.12849934 ... 0.         0.         0.19387755]
# [0.47945205 0.625      0.18720338 ... 0.1502415  0.         0.39795918]]