# Importing a machine learning library for building an AI model
from sklearn.neural_network import MLPClassifier

# Sample dataset for training the AI model
X = [[0., 0.], [1., 1.]]
y = [0, 1]

# Creating and training the AI model
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)

# Using the AI model to make a prediction
print("AI prediction for input [2., 2.]:", clf.predict([[2., 2.]]))


222