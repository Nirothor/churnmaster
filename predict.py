import pandas as pd
import joblib

# Load the trained model
model = joblib.load('best_model.pkl')  # Update with the actual path

def make_prediction(input_data):
    """
    Function to preprocess input data and make predictions with the loaded model.
    Adjust preprocessing as per your model's training requirements.
    """
    # Example preprocessing, adjust according to how the model was trained
    new_data = pd.DataFrame([input_data], columns=input_data.keys())
    
    # Predicting with the model
    prediction = model.predict(new_data)
    probability = model.predict_proba(new_data)
    
    return prediction, probability

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
    
    prediction, probability = make_prediction(new_customer)
    print("Prediction:", prediction)
    print("Probability:", probability)
