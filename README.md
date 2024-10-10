# Plas-tech Prediction API

## Project Description

Plas-tech is an innovative solution that leverages machine learning to predict gas output based on key production factors. The model is trained using data on plastic waste input, operating cost, and production time, helping to optimize gas production efficiency. This solution is crucial for industries aiming to improve energy production efficiency from waste materials, reducing environmental impact.

The solution includes:

- A machine learning model using Gradient Boosting to predict gas output.
- A Flask-based web interface that allows users to input production parameters and receive real-time gas output predictions.
- Deployed via Docker, making it accessible and easy to scale.

---

## Features

- **Data Visualization**: Displays visualizations of input features and their relationships with the target (gas output).
- **Model Architecture**: Gradient Boosting model with hyperparameter tuning (learning_rate, max_depth, n_estimators, subsample).
- **Performance Metrics**: Model evaluation metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score.
- **Deployment**: The solution is containerized using Docker, with a REST API and web form interface for user input.

---

## Installation and Setup

### Prerequisites

- Python 3.9+
- Docker
- Flask
- Scikit-learn

### Environment Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/plas-tech-api.git
   cd plas-tech-api
   ```

2. **Install dependencies**:

   - Using Docker, build the image and run the container:

   ```bash
   docker build -t plas-tech-api .
   docker run -p 5000:5000 plas-tech-api
   ```

3. **Access the app**:
   Open a web browser and navigate to `http://localhost:5000`. You'll be able to input the production data (Plastic Waste Input, Operating Cost, and Production Time) to get gas output predictions.

### Local Setup (without Docker)

1. **Install dependencies**:
   Inside your virtual environment, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask app**:

   ```bash
   flask run --host=0.0.0.0
   ```

3. **Access the app**:
   Open a web browser and navigate to `http://localhost:5000`.

---

## Project Structure

```bash
├── api/
│   ├── app.py              # Flask web application
│   ├── Dockerfile          # Docker configuration file
│   ├── model/              # Directory containing the machine learning model
│   │   └── gradient_boosting_model_tuned.joblib
│   ├── requirements.txt    # Python dependencies
│   ├── static/             # Static files (CSS, images)
│   └── templates/
│       └── index.html      # HTML template for the web interface
├── data/
│   └── plas_tech_complex_gas_production.csv  # Dataset used for training and evaluation
├── scripts/
│   ├── data_preprocessing.py # Script for data preprocessing
│   ├── train_model.py        # Script to train the ML model
│   └── evaluate_model.py     # Script to evaluate the trained model
├── README.md
```

---

## Design

- **Data Engineering**: The dataset includes variables like plastic waste input, operating cost, and time of production to predict gas output. Visualizations of the dataset show the relationships between the input features and target variable.
- **Model Architecture**: The model is a **Gradient Boosting** regressor, tuned with hyperparameters (`learning_rate`, `max_depth`, `n_estimators`, and `subsample`). The model was chosen due to its ability to handle complex relationships and minimize prediction errors.

- **User Interface**: A simple form where users input production parameters, and the model predicts gas output. The form is displayed via a Flask app, which returns results dynamically.

---

## Model Performance

- **Mean Absolute Error (MAE)**: 4.43
- **Mean Squared Error (MSE)**: 39.11
- **R² Score**: 0.999

The model provides accurate predictions based on production inputs, helping to optimize gas output in real-world scenarios.

---

## Deployment

### Docker Deployment Plan

- The application is containerized using Docker to ensure consistent environments for running the Flask app and the machine learning model.
- After building the Docker image, the app can be run locally or deployed on cloud services that support containerized apps, such as Google Cloud, AWS, or Heroku.

To deploy:

1. **Build the Docker image**:

   ```bash
   docker build -t plas-tech-api .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 5000:5000 plas-tech-api
   ```

3. **Access the app**:
   Open a browser and go to `http://localhost:5000`.

---

## Video Demo

- The video demonstration shows the setup process, how to input data into the web interface, and how predictions are made based on model output.
- **LINK** to demo: [https://drive.google.com/file/d/1BndliCpyx_fXTH1HONldjeTxEjmA2N6V/view?usp=sharing](#)

---

## GitHub Repository

- **Repository Link**: [Plas-tech API GitHub Repo](#)

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### Contact

For any queries, contact **Samuel Omondi** at [s.omondi@alustudent.com].
