import nltk
import pandas as pd
import string
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

# download required datasets
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

# load dataset
documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        text = movie_reviews.raw(fileid)
        label = 1 if category == "pos" else 0
        documents.append((text, label))

df = pd.DataFrame(documents, columns=["text", "label"])

print("Dataset size:", len(df))

stop_words = set(stopwords.words("english"))

# preprocessing function
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [w for w in tokens if w not in string.punctuation]
    tokens = [w for w in tokens if w not in stop_words]
    return " ".join(tokens)

print("Cleaning text...")
df["clean"] = df["text"].apply(preprocess)

# TF-IDF with bigrams
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))

X = vectorizer.fit_transform(df["clean"])
y = df["label"]

# train/test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)

# models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "NaiveBayes": MultinomialNB(),
    "SVM": LinearSVC()
}

print("\nModel Comparison:\n")

for name,model in models.items():

    model.fit(X_train,y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test,pred)

    print(name,"Accuracy:",round(acc,3))