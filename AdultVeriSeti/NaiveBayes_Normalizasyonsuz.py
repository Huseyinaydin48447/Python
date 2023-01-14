import pandas as pd
# verileri okumak ve hedef olarak "income" sütununu seçme : df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", 
                 names=["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation","relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-  week", "native-country", "income"])
X = df.drop("income", axis=1)
y = df["income"]

# kategorik sütunları sayısal veri olarak kodlama:
X = pd.get_dummies(X, columns=["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "native-country"])

# verileri tren ve test setlerine ayırma:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# bir Naive Bayes sınıflandırıcısı eğitme:
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train, y_train)

# test setinde tahminler yapma:
predictions = clf.predict(X_test)


from sklearn.metrics import accuracy_score
print("Model accuracy: ", accuracy_score(y_test, predictions))
