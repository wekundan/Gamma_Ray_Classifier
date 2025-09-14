from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open('Knn_model.pkl', 'rb'))

# Route for homepage (GET + POST)
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            features = request.form['features']
            features = [float(x) for x in features.split(',')]
            features = np.array(features).reshape(1, -1)

            # Raw prediction (0 or 1)
            pred_value = model.predict(features)[0]

            # Map prediction to user-friendly label
            if pred_value == 1:
                prediction = "Gamma Ray Event (Signal detected ✨)"
            else:
                prediction = "Hadron Event (Background noise 🌌)"
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)


