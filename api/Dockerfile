# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Ensure the model directory exists before copying the model
RUN mkdir -p /app/model

# Copy the model into the container
COPY model/gradient_boosting_model_tuned.joblib /app/model/

# Install necessary dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the world outside this container
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask app when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
