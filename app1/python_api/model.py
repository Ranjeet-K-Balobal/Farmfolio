

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Define X globally
X = None

def load_and_preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Mapping values
    mapping = {
        'Market_Demand': {'High': 2, 'Medium': 1, 'Low': 0},
        'Land_Ownership': {'Leased': 1, 'Owned': 2},
        'Weather_Data': {'Normal': 2, 'Unpredictable': 0, 'Variable': 1},
        'Government_Subsidy': {'Yes': 1, 'No': 0},
        'Livestock_Inventory': {'Sheep': 2, 'Pigs': 1, 'Chicken': 0, 'Cattle': 3},
        'Education': {'High School': 2, 'College Degree': 3, 'None': 1},
        'Community_Feedback': {'Low': 0, 'Medium': 1, 'High': 2},
        'Creditworthiness': {'Excellent': 5, 'Very Good': 4, 'Good': 3, 'Average': 2, 'Poor': 1}
    }

    # Apply mapping to the dataframe
    df.replace(mapping, inplace=True)
    
    return df

def train_logistic_regression_model(df):
    global X  # Use the global X

    # Assuming 'Creditworthiness' is your target variable
    X = df.drop('Creditworthiness', axis=1)
    y = df['Creditworthiness']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Logistic Regression model
    model = LogisticRegression()

    # Train the model
    model.fit(X_train, y_train)

    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    # Print the results
    print(f"Accuracy: {accuracy}")
    print("Confusion Matrix:")
    print(conf_matrix)
    print("Classification Report:")
    print(class_report)

def predict_creditworthiness(model, new_data):
    # Load the mapping
    mapping = {
        'Market_Demand': {'High': 2, 'Medium': 1, 'Low': 0},
        'Land_Ownership': {'Leased': 1, 'Owned': 2},
        'Weather_Data': {'Normal': 2, 'Unpredictable': 0, 'Variable': 1},
        'Government_Subsidy': {'Yes': 1, 'No': 0},
        'Livestock_Inventory': {'Sheep': 2, 'Pigs': 1, 'Chicken': 0, 'Cattle': 3},
        'Education': {'High School': 2, 'College Degree': 3, 'None': 1},
        'Community_Feedback': {'Low': 0, 'Medium': 1, 'High': 2},
        'Creditworthiness': {'Excellent': 5, 'Very Good': 4, 'Good': 3, 'Average': 2, 'Poor': 1}
    }

    # Convert input data to DataFrame
    new_df = pd.DataFrame([new_data])

    # Apply the same mapping to the new input data
    new_df.replace(mapping, inplace=True)
    new_df.fillna(999, inplace=True)

    # Ensure that the columns are in the same order as during training
    new_df = new_df[X.columns]

    # Make prediction
    prediction = model.predict(new_df)

    # Convert numeric prediction to Python data type
    prediction_value = int(prediction[0])

    # Map numeric predictions to categories
    creditworthiness_mapping = {
        5: 'Excellent',
        4: 'Very Good',
        3: 'Good',
        2: 'Average',
        1: 'Poor'
    }

    # Map the numeric prediction to the corresponding category
    predicted_category = creditworthiness_mapping.get(prediction_value, 'Unknown')

    # Return the prediction and interpreted prediction
    return prediction_value, predicted_category

    # Load the mapping
    mapping = {
        'Market_Demand': {'High': 2, 'Medium': 1, 'Low': 0},
        'Land_Ownership': {'Leased': 1, 'Owned': 2},
        'Weather_Data': {'Normal': 2, 'Unpredictable': 0, 'Variable': 1},
        'Government_Subsidy': {'Yes': 1, 'No': 0},
        'Livestock_Inventory': {'Sheep': 2, 'Pigs': 1, 'Chicken': 0, 'Cattle': 3},
        'Education': {'High School': 2, 'College Degree': 3, 'None': 1},
        'Community_Feedback': {'Low': 0, 'Medium': 1, 'High': 2},
        'Creditworthiness': {'Excellent': 5, 'Very Good': 4, 'Good': 3, 'Average': 2, 'Poor': 1}
    }

    # Convert input data to DataFrame
    new_df = pd.DataFrame([new_data])

    # Apply the same mapping to the new input data
    new_df.replace(mapping, inplace=True)
    new_df.fillna(999, inplace=True)

    # Ensure that the columns are in the same order as during training
    new_df = new_df[X.columns]

    # Make prediction
    prediction = model.predict(new_df)

    # Map numeric predictions to categories
    creditworthiness_mapping = {
        5: 'Excellent',
        4: 'Very Good',
        3: 'Good',
        2: 'Average',
        1: 'Poor'
    }

    # Map the numeric prediction to the corresponding category
    predicted_category = creditworthiness_mapping.get(prediction[0], 'Unknown')

    # Return the prediction and interpreted prediction
    return prediction[0], predicted_category

    # Convert input data to DataFrame
    new_df = pd.DataFrame([new_data])

    # Apply the same mapping to the new input data
    new_df.replace(mapping, inplace=True)
    new_df.fillna(999, inplace=True)

    # Ensure that the columns are in the same order as during training
    new_df = new_df[X.columns]

    # Make prediction
    prediction = model.predict(new_df)

    # Map numeric predictions to categories
    creditworthiness_mapping = {
        5: 'Excellent',
        4: 'Very Good',
        3: 'Good',
        2: 'Average',
        1: 'Poor'
    }

    # Map the numeric prediction to the corresponding category
    predicted_category = creditworthiness_mapping.get(prediction[0], 'Unknown')

    # Print the interpreted prediction
    print("Predicted Creditworthiness:", prediction)
    print("Interpreted Creditworthiness:", predicted_category)

if __name__ == "__main__":
    file_path = 'data\credit.csv'
    df = load_and_preprocess_data(file_path)
    model, X_test, y_test = train_logistic_regression_model(df)
    evaluate_model(model, X_test, y_test)

    # Example for predicting new data
    new_data = {
        'Farming_Turnover': 50000,
        'Crop_Yields': 1500,
        'Land_Size': 10,
        'Expenses': 20000,
        'Debts_Liabilities': 5000,
        'Market_Demand': 'High',
        'Land_Ownership': 'Owned',
        'Weather_Data': 'Normal',
        'Government_Subsidy': 'Yes',
        'Livestock_Inventory': 'Sheep',
        'Education': 'College Degree',
        'Community_Feedback': 'Medium'
    }
    mapping = {
        'Market_Demand': {'High': 2, 'Medium': 1, 'Low': 0},
        'Land_Ownership': {'Leased': 1, 'Owned': 2},
        'Weather_Data': {'Normal': 2, 'Unpredictable': 0, 'Variable': 1},
        'Government_Subsidy': {'Yes': 1, 'No': 0},
        'Livestock_Inventory': {'Sheep': 2, 'Pigs': 1, 'Chicken': 0, 'Cattle': 3},
        'Education': {'High School': 2, 'College Degree': 3, 'None': 1},
        'Community_Feedback': {'Low': 0, 'Medium': 1, 'High': 2},
        'Creditworthiness': {'Excellent': 5, 'Very Good': 4, 'Good': 3, 'Average': 2, 'Poor': 1}
    }
    predict_creditworthiness(model, new_data, mapping)
