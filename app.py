import pandas as pd
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load your trained model
model = pickle.load(open("random_forest_model.pkl", "rb"))

# Render the HTML form
@app.route("/")
def index():
    return render_template("index.html")

# Handle prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from the request
        data = request.get_json()

        # Define feature names based on your dataset
        feature_names = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
                         'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement',
                         'yr_built', 'city', 'statezip']

        # Process input data and perform prediction using your model
        # Ensure that the order of features matches the order used during training
        input_data = pd.DataFrame({feature: [data[feature]] for feature in feature_names})
        predicted_price = model.predict(input_data)

        # Return the predicted price as JSON
        return jsonify({"predicted_price": predicted_price[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0',port=5000)
