import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

nltk.download('punkt')
nltk.download('stopwords')

data = {
    "text":[
        "I love this product",
        "This is terrible",
        "Amazing experience",
        "Worst service ever",
        "I am very happy",
        "I hate this",
        "Great support team",
        "Very bad quality"
    ],
    "label":[1,0,1,0,1,0,1,0]
}

df = pd.DataFrame(data)

stop_words=set(stopwords.words('english'))

def preprocess(text):
    tokens=word_tokenize(text)
    tokens=[w.lower() for w in tokens if w not in string.punctuation]
    tokens=[w for w in tokens if w not in stop_words]
    return " ".join(tokens)

df["clean"]=df["text"].apply(preprocess)

# CountVectorizer
count_vectorizer = CountVectorizer()
X_count = count_vectorizer.fit_transform(df["clean"])

# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(df["clean"])

y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X_count,y,test_size=0.3,random_state=42)

model1 = LogisticRegression()
model1.fit(X_train,y_train)
pred1=model1.predict(X_test)

print("CountVectorizer Accuracy:",accuracy_score(y_test,pred1))

X_train, X_test, y_train, y_test = train_test_split(X_tfidf,y,test_size=0.3,random_state=42)

model2 = LogisticRegression()
model2.fit(X_train,y_train)
pred2=model2.predict(X_test)

print("TF-IDF Accuracy:",accuracy_score(y_test,pred2))