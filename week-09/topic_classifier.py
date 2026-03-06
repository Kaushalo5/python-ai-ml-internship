import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# sample dataset
data = {
"text":[
"Python is great for data science",
"Machine learning and AI are powerful",
"Football world cup is exciting",
"Cricket match was thrilling",
"Technology is evolving rapidly",
"Basketball is a popular sport"
],
"category":[
"Technology",
"Technology",
"Sports",
"Sports",
"Technology",
"Sports"
]
}

df = pd.DataFrame(data)

# convert text to numeric vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

y = df["category"]

# train model
model = LogisticRegression()
model.fit(X,y)

# prediction
while True:

    text = input("Enter text (or type exit): ")

    if text.lower() == "exit":
        break

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)

    print("Category:",prediction[0])