import pandas as pd
import joblib
from sklearn.metrics import classification_report, roc_auc_score, roc_curve, auc
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load('best_model2.pkl')  # Update with the actual path
def make_prediction(input_data):
    new_data = pd.DataFrame([input_data], columns=input_data.keys())
    prediction = model.predict(new_data)
    probability = model.predict_proba(new_data)
    return prediction, probability

def evaluate_model(X_test, y_test):
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    print("Classification Report:\n", classification_report(y_test, predictions))
    roc_auc = roc_auc_score(y_test, probabilities)
    print("ROC AUC Score:", roc_auc)
    fpr, tpr, _ = roc_curve(y_test, probabilities)
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample new customer data
    new_customer = {
        'ProductCustomerFitScore': 0.5,
        'OnboardingCompletion': 0.8,
        'CustomerServiceRating': 3.5,
        'ValueForMoneyRating': 4.0,
        'ReportedBugs': 1,
        'PaymentIssuesLastYear': 0,
        'FeatureRequests': 2
    }

    # Predicting a single customer
    prediction, probability = make_prediction(new_customer)
    print("Prediction:", prediction)
    print("Probability:", probability)

    # Load your test data here for evaluation, e.g., X_test, y_test
    X_test = pd.read_csv('C:/dev/Output/X_test.csv')
    y_test = pd.read_csv('C:/dev/Output/y_test.csv')['Churned']
    
    # Drop columns that were not used during the model training
if 'CustomerID' in X_test.columns:
    X_test.drop(['CustomerID'], axis=1, inplace=True)
if 'ChurnRiskReason' in X_test.columns:
    X_test.drop(['ChurnRiskReason'], axis=1, inplace=True)

    # Uncomment below to evaluate model on the test data
    evaluate_model(X_test, y_test)
