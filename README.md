# Churn Prediction Application

This repository contains the code for a Flask-based web application that predicts customer churn. The application uses a machine learning model trained on customer data to predict the likelihood of churn based on various features.

## Overview

The Churn Prediction Application is designed to help businesses understand and predict customer behavior, particularly the likelihood of customers discontinuing their use of a service. The application takes in customer data through a web form and returns a churn prediction along with the associated probability.

## Features

- **Churn Prediction Form**: A user-friendly web form where users can input customer data.
- **Prediction Results**: Displays the churn prediction and probability after processing the input data.
- **Machine Learning Model**: Utilizes a pre-trained model to make predictions based on the input data.

## Installation

To set up the application locally, follow these steps:

1. Clone the repository

Navigate to the project directory:
cd your-repository-name

Install the required dependencies (ensure you have Python and pip installed):
pip install -r requirements.txt

Run the Flask application:
python app.py

**Usage**
Once the application is running, you can access it by navigating to http://127.0.0.1:5000 in your web browser. Fill out the churn prediction form with the relevant customer data and submit it to receive a prediction.

**Code Structure**
app.py: The main Flask application file that contains the routes and prediction logic.
best_model2.pkl: The pre-trained machine learning model used for making predictions.
preprocessor.pkl: The preprocessing pipeline used to process input data before making predictions.
templates/: Contains the HTML templates for the web application.
index2.html: The HTML template for the churn prediction form.
static/: Contains static files such as CSS and JavaScript (if applicable).
Contributing
Contributions to improve the application are welcome. Please follow the standard GitHub pull request process to submit your changes.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.
**
Contact**
For any queries or further assistance, please contact Your Name.
**
Acknowledgments**
Thanks to all the contributors who have helped with the development of this application.
Special thanks to the open-source community for providing the tools and libraries used in this project.

### My GitHub Stats
!GitHub stats

### Weekly Development Breakdown
<!--START_SECTION:waka-->
```text
Python       7 hrs 30 mins   ██████████████████░░░░░░░   72.00 %
SQL          1 hr 30 mins    ███░░░░░░░░░░░░░░░░░░░░░░   14.50 %
Other        1 hr            ███░░░░░░░░░░░░░░░░░░░░░░   9.50 %

**Feel free to reach out if you have any questions or need assistance with your projects!**
