import numpy as np
import pandas as pd
from faker import Faker
from scipy.stats import truncnorm

fake = Faker()

# Set a random seed for reproducibility
np.random.seed(42)

# Define the number of samples
n_samples = 500000

# Helper function to generate normally distributed data within specified range
def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

# Generate synthetic data
data = {
    'CustomerID': [fake.uuid4() for _ in range(n_samples)],
    'ProductCustomerFitScore': get_truncated_normal(mean=0.5, sd=0.2, low=0, upp=1).rvs(n_samples),
    'OnboardingCompletion': get_truncated_normal(mean=0.7, sd=0.15, low=0, upp=1).rvs(n_samples),
    'CustomerServiceRating': get_truncated_normal(mean=3, sd=1.5, low=0, upp=5).rvs(n_samples),
    'ValueForMoneyRating': get_truncated_normal(mean=3.5, sd=1, low=0, upp=5).rvs(n_samples),
    'ReportedBugs': np.random.poisson(2, n_samples),  # Average number of bugs reported
    'PaymentIssuesLastYear': np.random.poisson(0.5, n_samples),  # Average payment issues
    'FeatureRequests': np.random.poisson(1, n_samples),  # Feature requests by the customer
    'Churned': np.random.binomial(1, p=[0.85, 0.15][np.random.beta(2, 5, n_samples) > 0.3])
}

# Generate reasons for churn dynamically based on risk factors
reasons_for_churn = [
    'Bad product-customer fit', 'Ineffective onboarding', 'Poor customer service',
    'Lack of perceived value', 'Unresolved product bugs', 'Payment issues',
    'Lack of necessary features', 'Poor user experience', 'Competitor offers',
    'Pricing concerns'
]

data['ChurnRiskReason'] = [np.random.choice(reasons_for_churn, p=[0.2 if x else 0.05 for x in np.random.rand(10) < 0.5])
                           for _ in range(n_samples)]

# Creating DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
output_file_path = 'C:/dev/Output/Churn_Data1.csv'
df.to_csv(output_file_path, index=False)
print(f"Synthetic data file saved to {output_file_path}")
