import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
import pickle

# Load model and categorical column info
model = pickle.load(open('financial_inclusion_model.pkl', 'rb'))
cat_col = pickle.load(open('fin_col_model.pkl', 'rb'))  # List of categorical columns

# Define column names
columns = ['year', 'uniqueid', 'location_type',
           'cellphone_access', 'household_size', 'age_of_respondent',
           'gender_of_respondent', 'relationship_with_head', 'marital_status',
           'education_level', 'job_type']

def prediction(data):
    # Create DataFrame
    df = pd.DataFrame([data], columns=columns)

    # Separate categorical and numerical columns
    categorical_cols = [col for col in columns if df[col].dtype == 'object']
    numerical_cols = [col for col in columns if col not in categorical_cols]

    # Encode categorical values
    if categorical_cols:
        encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
        df[categorical_cols] = encoder.fit_transform(df[categorical_cols])

    # Encode numerical values (convert to categorical encoding)
    if numerical_cols:
        df[numerical_cols] = df[numerical_cols].rank(method='dense', ascending=True).astype(int)

    # Print transformed DataFrame
    print(df)

    # Make prediction
    pred = model.predict(df.values)  # No need to reshape

    if pred[0] == 1:
        return "The Customer don't have a Bank account"
    else:
        return "The Customer has a Bank account"

# Example Prediction
print(prediction([
 2018,
 'uniqueid_3',
 'Urban',
 'Yes',
 5,
 26,
 'Male',
 'Other relative',
 'Single/Never Married',
 'Vocational/Specialised training',
 'Self employed']))
