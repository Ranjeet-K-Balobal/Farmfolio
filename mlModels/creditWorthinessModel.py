import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
df = pd.read_csv('/content/credit.csv')

# Drop non-numeric columns and the target variable for features
features = df.drop(['SSN', 'Creditworthiness'], axis=1)

# Target variable
target = df['Creditworthiness']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# User input
user_input = pd.DataFrame(columns=features.columns)
user_input.loc[0] = [user_turnover, user_yield, user_demand, user_ownership, user_size, user_weather, user_subsidy, user_expenses, user_inventory, user_education, user_debts, user_feedback]

# Make prediction
predicted_credit = model.predict(user_input)

# Add the predicted credit score to the dataset
df.loc[len(df)] = [user_turnover, user_yield, user_demand, user_ownership, user_size, user_weather, user_subsidy, user_expenses, user_inventory, user_education, user_debts, user_feedback, predicted_credit[0]]

# Save the updated dataset
df.to_csv('/content/credit.csv', index=False)
