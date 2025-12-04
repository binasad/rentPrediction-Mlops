from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# 1. Load the Brains 🧠
# We load these once when the server starts so it's fast
print("Loading model...")
model = joblib.load('model.pkl')
model_columns = joblib.load('model_columns.pkl')
print("Model loaded!")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Receive Data (JSON)
        # Expected format: {"Location": "F-6", "Area": 20.0, "Beds": 4}
        json_ = request.json
        query_df = pd.DataFrame([json_])

        # 2. Convert Categories to Numbers (One-Hot Encoding)
        # This turns "Location: F-6" into "Location_F-6: 1"
        query = pd.get_dummies(query_df)

        # 3. Align Columns (The MLOps Magic ✨)
        # We ensure the input has the EXACT same columns as the model expects.
        # If "Location_G-13" is missing in input, we create it and set it to 0.
        query = query.reindex(columns=model_columns, fill_value=0)

        # 4. Ask the Model
        prediction = model.predict(query)

        # 5. Send Answer
        return jsonify({
            'prediction': prediction[0],
            'status': 'success'
        })

    except Exception as e:
        return jsonify({'error': str(e), 'trace': str(e)})

if __name__ == '__main__':
    # host='0.0.0.0' tells Flask to accept connections from outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)