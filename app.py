# app.py
"""
Hospital Readmission Prediction Web App
- Browser form for input
- Shows prediction result directly
"""

from flask import Flask, request, render_template_string
import pandas as pd
import joblib

# 1. Load the trained model
model = joblib.load("readmission_model.pkl")

# 2. Initialize Flask
app = Flask(__name__)

# 3. HTML template for form + results
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hospital Readmission Prediction</title>
</head>
<body>
    <h2>🏥 Hospital Readmission Prediction</h2>
    <form method="POST">
        Age: <input type="number" name="age" required><br><br>
        Number of Previous Visits: <input type="number" name="num_previous_visits" required><br><br>
        Average Stay Days: <input type="number" step="0.1" name="avg_stay_days" required><br><br>
        Diagnosis - Diabetes (1=yes, 0=no): <input type="number" min="0" max="1" name="diagnosis_diabetes" required><br><br>
        Diagnosis - Hypertension (1=yes, 0=no): <input type="number" min="0" max="1" name="diagnosis_hypertension" required><br><br>
        Diagnosis - Infection (1=yes, 0=no): <input type="number" min="0" max="1" name="diagnosis_infection" required><br><br>
        <input type="submit" value="Predict">
    </form>

    {% if prediction is not none %}
        <h3>Prediction Result:</h3>
        <p>Readmission Risk: <strong>{{ prediction }}</strong></p>
        <p>Meaning: <strong>{{ meaning }}</strong></p>
    {% endif %}
</body>
</html>
"""

# 4. Route for home & prediction
@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    meaning = None

    if request.method == "POST":
        try:
            # Collect and convert form data
            data = {
                "age": float(request.form["age"]),
                "num_previous_visits": int(request.form["num_previous_visits"]),
                "avg_stay_days": float(request.form["avg_stay_days"]),
                "diagnosis_diabetes": int(request.form["diagnosis_diabetes"]),
                "diagnosis_hypertension": int(request.form["diagnosis_hypertension"]),
                "diagnosis_infection": int(request.form["diagnosis_infection"])
            }

            # Convert to DataFrame
            df = pd.DataFrame([data])

            # Make prediction
            pred = model.predict(df)[0]
            prediction = int(pred)
            meaning = "High Risk" if pred == 1 else "Low Risk"

        except Exception as e:
            prediction = "Error"
            meaning = str(e)

    return render_template_string(HTML_TEMPLATE, prediction=prediction, meaning=meaning)

# 5. Run the app
if __name__ == "__main__":
    app.run(debug=True)
