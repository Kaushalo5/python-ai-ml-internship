import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y = np.array([0,0,0,0,1,1,1,1,1,1])

# deeper network
model = MLPClassifier(hidden_layer_sizes=(16,8), activation='relu', max_iter=3000)

model.fit(X, y)

pred = model.predict(X)
print("Accuracy:", accuracy_score(y, pred))

print("Prediction for 2 hours:", model.predict([[2]]))
print("Prediction for 8 hours:", model.predict([[8]]))