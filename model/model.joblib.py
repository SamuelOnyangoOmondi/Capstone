# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load and preprocess data (assuming your dataset is in CSV format)
def load_and_preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Assuming the target variable is the last column
    X = data.iloc[:, :-1]  # Features (all columns except the last one)
    y = data.iloc[:, -1]   # Target (last column)
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test

# Train a model and save it
def train_and_save_model(X_train, y_train, model_path):
    # Initialize the RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Save the model to a .joblib file
    joblib.dump(model, model_path)
    
    return model

# Load the saved model
def load_model(model_path):
    return joblib.load(model_path)

if __name__ == "__main__":
    # Define the file paths
    dataset_path = "D:/Capstone/plas_tech_dataset.csv"
    model_path = "D:/Capstone/model/model.joblib"
    
    # Load and preprocess the data
    X_train, X_test, y_train, y_test = load_and_preprocess_data(dataset_path)
    
    # Train the model and save it
    model = train_and_save_model(X_train, y_train, model_path)
    
    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"Model trained and saved as {model_path}")
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
