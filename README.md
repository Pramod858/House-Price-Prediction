# House Price Prediction

![House Price](https://github.com/Pramod858/House-Price-Prediction/assets/80105491/a313c7f9-bc82-4e7a-b378-8ee9221031cd)

## Overview

This project is a simple web application for predicting house prices based on various features. It uses a machine learning model trained on a dataset of house prices. The web interface allows users to input details about a house, and the system will predict the price.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python (version 3.9.18)
- Docker

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Pramod858/House-Price-Prediction.git
   cd House-Price-Prediction
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App Locally:**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/` in your browser.

## Using Docker

Alternatively, you can run the application using Docker.

1. **Build the Docker Image:**

   ```bash
   docker build -t house_price_prediction -f Dockerfile.txt .
   ```

2. **Run the Docker Container:**

   ```bash
   docker run -p 5000:5000 house_price_prediction
   ```

   The application will be available at `http://127.0.0.1:5000/` in your browser.

## Extra : 

Here is the [link](https://github.com/Pramod858/House-Price-Prediction-MLflow.git) for House Price Prediction with MLflow. 

## Usage

- Open your browser and navigate to `http://127.0.0.1:5000/`.
- Input the details for the house (bedrooms, bathrooms, etc.).
- Click the "Predict Price" button to get the predicted house price.
