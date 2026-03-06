from collections import Counter
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = """
Artificial Intelligence and Machine Learning are transforming technology.
AI helps automate tasks and analyze large amounts of data.
"""

tokens = word_tokenize(text.lower())

# word frequency
word_freq = Counter(tokens)

print("Top Words:")
for word,count in word_freq.most_common(5):
    print(word, count)

# text length stats
print("\nTotal Words:",len(tokens))
print("Unique Words:",len(set(tokens)))