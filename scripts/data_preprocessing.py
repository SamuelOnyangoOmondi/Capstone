# data_preprocessing.py

# Import necessary modules
import pandas as pd

def load_and_preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    print(f"Loading dataset from {file_path}")
    print(f"Data loaded successfully with shape: {data.shape}")
    print(f"First few rows of the dataset:\n{data.head()}")

    # Define feature columns and target
    X = data[['Plastic_Waste_Input_kg', 'Operating_Cost_USD', 'Time_of_Production_minutes']]
    y = data['Gas_Output_liters']

    print(f"Features (X) shape: {X.shape}")
    print(f"Target (y) shape: {y.shape}")

    return X, y
