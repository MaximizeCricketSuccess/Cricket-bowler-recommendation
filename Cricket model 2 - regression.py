import pandas as pd
import statsmodels.api as sm

unique_bowlers = pd.read_csv('/Users/sakarth/Downloads/unique_bowlers_data.csv')
current_over = int(input("Enter the current over: "))

# Prepare the features (X) and target variable (y)
y = unique_bowlers[f'runs_{current_over}']
X = unique_bowlers[[f'economy_{current_over}', f'SR_{current_over}', f'wickets_{current_over}', f'boundary_{current_over}', f'dot_{current_over}']]
# Add a constant to the features matrix
X = sm.add_constant(X)
# Create a linear regression model
model = sm.OLS(y, X)
# Fit the model
results = model.fit()

# Get user input for the feature values
economy = float(input("Enter current economy: "))
SR = float(input("Enter current SR: "))
wickets = int(input("Enter current total number of wickets: "))
boundary = int(input("Enter number of boundaries conceded until now: "))
dot = int(input("Enter number of dot balls conceded until now: "))
# Create a DataFrame with the user input
user_input = pd.DataFrame({
    'const': [1],  # Constant term
    'economy': [economy],
    'SR': [SR],
    'wickets': [wickets],
    'boundary': [boundary],
    'dot': [dot]
})

# Make predictions
prediction = results.predict(user_input)
# Print the predicted value
print(f'Predicted Runs: {prediction.values[0]}')