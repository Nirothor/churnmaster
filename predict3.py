import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import classification_report, roc_auc_score, roc_curve, auc, precision_recall_curve, f1_score
import matplotlib.pyplot as plt

# Load the test data, ensuring only the features used in the model are present
X_test = pd.read_csv('C:/dev/Output/X_test.csv').drop(['CustomerID', 'ChurnRiskReason'], axis=1, errors='ignore')
y_test = pd.read_csv('C:/dev/Output/y_test.csv')['Churned']

# Load the trained model
model = joblib.load('best_model2.pkl')  # Update with the actual path

def evaluate_model(X_test, y_test, model):
    """
    Evaluate the model using various metrics and plot ROC and Precision-Recall curves.
    """
    # Predicting probabilities and classes
    probabilities = model.predict_proba(X_test)[:, 1]
    predictions = model.predict(X_test)

    # Printing classification report
    print("Classification Report:\n", classification_report(y_test, predictions))

    # Calculating ROC AUC Score
    roc_auc = roc_auc_score(y_test, probabilities)
    print("ROC AUC Score:", roc_auc)

    # Plotting ROC Curve
    fpr, tpr, _ = roc_curve(y_test, probabilities)
    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()

    # Calculating and plotting Precision-Recall curve
    precision, recall, thresholds = precision_recall_curve(y_test, probabilities)
    plt.figure()
    plt.plot(recall, precision, label='Precision-Recall curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall curve')
    plt.legend(loc="lower left")
    plt.show()

    # Calculating the best F1 Score
    f1_scores = 2*recall*precision / (np.maximum(recall + precision, np.finfo(float).eps))
    print('Best F1-Score:', np.max(f1_scores))

# Call the evaluate_model function to evaluate the model on the test data
evaluate_model(X_test, y_test, model)
