import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# simple dataset
data = {
"text":[
"I love this movie",
"This film is amazing",
"Great acting and story",
"I hate this movie",
"Terrible film",
"Worst acting ever"
],
"label":[1,1,1,0,0,0]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = LogisticRegression()

model.fit(X,y)

joblib.dump(model,"model.pkl")
joblib.dump(vectorizer,"vectorizer.pkl")

print("Model files created successfully")