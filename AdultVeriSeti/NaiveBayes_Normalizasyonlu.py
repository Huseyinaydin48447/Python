import pandas as pd

# Burada verileri okuması ve hedef olarak "income" sütununu seçmesi:
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", 
                 names=["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", 
                        "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"])
X = df.drop("income", axis=1)
y = df["income"]

# kategorik sütunları sayısal veri olarak kodlamak: X = pd.get_dummies(X, columns=["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "native-country"])

# verileri normalleştirme:
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
# verileri tren ve test setlerine ayırma:

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

# bir Naive Bayes sınıflandırıcısı eğitmek için bu kodu kullanılır:
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train, y_train)

# test setinde tahminler yapmak için bu kullanılır.
predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score
print("Model accuracy:", accuracy_score(y_test, predictions))

