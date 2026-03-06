from sentiment_pipeline import predict_sentiment

print("Mini Sentiment Analyzer")
print("Type 'exit' to stop\n")

while True:
    text = input("Enter sentence: ")
    if text.lower() == "exit":
        break

    print("Sentiment:", predict_sentiment(text))
    print()