from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("mtcars_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Expects JSON with the same features as mtcars.csv (except mpg), e.g.:
    {
      "cyl": 6,
      "disp": 160.0,
      "hp": 110,
      "drat": 3.90,
      "wt": 2.620,
      "qsec": 16.46,
      "vs": 0,
      "am": 1,
      "gear": 4,
      "carb": 4
    }
    """
    data = request.get_json()
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    return jsonify({"predicted_mpg": pred})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
