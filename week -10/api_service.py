from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from logger_config import logger

nltk.download("punkt")
nltk.download("stopwords")

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

stop_words = set(stopwords.words("english"))

class TextInput(BaseModel):
    text: str

def preprocess(text):

    tokens = word_tokenize(text.lower())

    tokens = [w for w in tokens if w not in string.punctuation]

    tokens = [w for w in tokens if w not in stop_words]

    return " ".join(tokens)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sentiment API running"}

@app.post("/predict")
def predict(data: TextInput):

    text = data.text

    logger.info(f"Request received: {text}")

    clean = preprocess(text)

    vector = vectorizer.transform([clean])

    prediction = model.predict(vector)[0]

    sentiment = "Positive" if prediction == 1 else "Negative"

    logger.info(f"Prediction returned: {sentiment}")

    return {"sentiment": sentiment}