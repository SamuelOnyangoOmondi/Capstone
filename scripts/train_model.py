import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, make_scorer
from sklearn.model_selection import cross_val_score
import joblib
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load and preprocess data
def load_and_preprocess_data(dataset_path):
    logging.info(f"Loading dataset from {dataset_path}")
    data = pd.read_csv(dataset_path)
    logging.info(f"Data loaded successfully with shape: {data.shape}")
    
    # Select features and target
    X = data[['Plastic_Waste_Input_kg', 'Operating_Cost_USD', 'Time_of_Production_minutes']]
    y = data['Gas_Output_liters']
    
    logging.info(f"Features (X) shape: {X.shape}")
    logging.info(f"Target (y) shape: {y.shape}")
    
    return X, y

# Train model with cross-validation and hyperparameter tuning
def train_model(X, y):
    logging.info("Training the model...")

    # Hyperparameters to tune
    param_grid = {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 4, 5],
        'subsample': [0.8, 0.9, 1.0]
    }

    # GradientBoostingRegressor with GridSearchCV
    model = GradientBoostingRegressor()
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, scoring=make_scorer(mean_absolute_error, greater_is_better=False))
    grid_search.fit(X, y)

    # Best model after hyperparameter tuning
    best_model = grid_search.best_estimator_
    logging.info(f"Best parameters found: {grid_search.best_params_}")

    # Evaluate cross-validation score
    cv_scores = cross_val_score(best_model, X, y, cv=5, scoring=make_scorer(mean_absolute_error))
    logging.info(f"Cross-Validation MAE: {cv_scores.mean()}")

    # Save the best model
    model_path = "D:/Capstone/model/gradient_boosting_model_tuned.joblib"
    joblib.dump(best_model, model_path)
    logging.info(f"Model saved successfully at {model_path}")

    return best_model

if __name__ == "__main__":
    # Define dataset path
    dataset_path = "D:/Capstone/data/plas_tech_complex_gas_production.csv"

    # Load data
    X, y = load_and_preprocess_data(dataset_path)

    # Train model with tuning
    best_model = train_model(X, y)
