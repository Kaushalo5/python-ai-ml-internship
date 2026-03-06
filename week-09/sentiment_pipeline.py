import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ---------------- NLTK SAFE SETUP ----------------
def setup_nltk():
    resources = [
        ("tokenizers/punkt", "punkt"),
        ("tokenizers/punkt_tab", "punkt_tab"),
        ("corpora/stopwords", "stopwords")
    ]
    for path, name in resources:
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(name)

setup_nltk()
# -------------------------------------------------

# dataset
data = {
    "text": [
        "I love this product",
        "This is terrible",
        "Amazing experience",
        "Worst service ever",
        "I am very happy",
        "I hate this",
        "Great support team",
        "Very bad quality",
        "Absolutely fantastic",
        "Not good at all"
    ],
    "label": [1,0,1,0,1,0,1,0,1,0]
}

df = pd.DataFrame(data)

# preprocessing
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens if w not in string.punctuation]
    tokens = [w for w in tokens if w not in stop_words]
    return " ".join(tokens)

df["cleaned"] = df["text"].apply(preprocess)

# vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned"])
y = df["label"]

# train model
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test,pred))

# prediction function
def predict_sentiment(text):
    clean = preprocess(text)
    vector = vectorizer.transform([clean])
    prediction = model.predict(vector)
    return "Positive" if prediction[0]==1 else "Negative"


# test
if __name__ == "__main__":
    print("\nTesting predictions:")
    print("I love this service ->", predict_sentiment("I love this service"))
    print("This is worst ->", predict_sentiment("This is worst"))